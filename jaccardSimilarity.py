'''The Jaccard index, also known as Intersection over Union and the Jaccard similarity coefficient 
(originally given the French name coefficient de communauté by Paul Jaccard), is a statistic used 
for gauging the similarity and diversity of sample sets.'''

'''This function gives the jaccard similarity gives 2 sentences. Lets say we have sentence A and sentence B,
the jaccard similarity is (A intersect B /AUB).'''


def get_jaccard_sim(str1, str2):
    a = set(str1.split())
    b = set(str2.split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))


if __name__ == "__main__":
    sentence_1 = "This sentences is vague"
    sentence_2 = "This sentence is not clear"
    print(get_jaccard_sim(sentence_1, sentence_2))
