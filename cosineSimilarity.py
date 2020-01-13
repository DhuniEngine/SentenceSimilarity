import re
import math
from collections import Counter

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):

    # gives the intersection between two words
    intersection = set(vec1.keys()) & set(vec2.keys())
    for x in intersection:
        print(vec1['model'])

    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    # gets all the words in the sentences in terms of a list
    words = WORD.findall(text)
    # returns the counter of the words, or counts all the words in a given sentence
    return Counter(words)


text1 = 'This model is   vague'
text2 = 'I do  not understand this model'

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print("The similarity between the two sentences are:{0}".format(cosine))
