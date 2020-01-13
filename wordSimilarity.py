from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')


def penn_to_wn(tag):
    """ Convert between a Penn Treebank tag to a simplified Wordnet tag """
    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('R'):
        return 'r'

    return None


def tagged_to_synset(word, tag):
    wn_tag = penn_to_wn(tag)
    if wn_tag is None:
        return None

    try:

        return wn.synsets(word, wn_tag)[0]
    except:

        return None


def sentence_similarity(sentence1, sentence2):
    """ compute the sentence similarity using Wordnet """
    # Tokenize and tag
    sentence1 = pos_tag(word_tokenize(sentence1))
    sentence2 = pos_tag(word_tokenize(sentence2))

    # Get the synsets for the tagged words
    synsets1 = [tagged_to_synset(*tagged_word) for tagged_word in sentence1]
    synsets2 = [tagged_to_synset(*tagged_word) for tagged_word in sentence2]

    # Filter out the Nones
    synsets1 = [ss for ss in synsets1 if ss]
    synsets2 = [ss for ss in synsets2 if ss]

    total_score = 0.00
    count = 0

    # For each word in the first sentence
    for synset in synsets1:
        # Get the similarity value of the most similar word in the other sentence
        best_score = ([synset.wup_similarity(ss, brown_ic) for ss in synsets2])
        best_score_curated = []
        for score in best_score:
            if score is not None:
                best_score_curated.append(score)
        try:
            max_score = max(best_score_curated)

        except:
            max_score = 0.00

        # Check that the similarity could have been computed

        total_score = max_score + total_score
        count += 1

    # Average the values
    total_score /= count
    return total_score


sentences = [
    "3T bioscience got acquired by Gilead"
]
focus_sentence = "Gilead bought 3T bioscience"


def symmetric_sentence_similarity(sentence1, sentence2):
    """ compute the symmetric sentence similarity using Wordnet """
    return (sentence_similarity(sentence1, sentence2) + sentence_similarity(sentence2, sentence1)) / 2


for sentence in sentences:
    # print ("SymmetricSimilarity(\"%s\", \"%s\") = %s" % (
    print(symmetric_sentence_similarity(focus_sentence, sentence))
