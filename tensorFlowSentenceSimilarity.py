
from numpy import dot
from numpy.linalg import norm
import seaborn as sns
import re
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.spatial.distance import cdist

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
model = hub.load(module_url)
print("module %s loaded" % module_url)


def embed(input):
    return model(input)


messages = ["Reports that the NSA eavesdropped on world leaders have severely shaken relations between Europe and the U.S., German Chancellor Angela Merkel said.",
            "Germany and France are to seek talks with the US to settle a row over spying, as espionage claims continue to overshadow an EU summit in Brussels."]


def calculate_sentence_similarity(vectors):
    c = vectors.numpy()
    cos_sim = 1 - cdist(c, c, 'cosine')
    print(cos_sim)


def plot_similarity(labels, features, rotation):
    corr = np.inner(features, features)
    print(corr)
    sns.set(font_scale=1.2)
    g = sns.heatmap(
        corr,
        xticklabels=labels,
        yticklabels=labels,
        vmin=0,
        vmax=1,
        cmap="YlOrRd")
    g.set_xticklabels(labels, rotation=rotation)
    g.set_title("Semantic Textual Similarity")


def run_and_plot(messages_):
    message_embeddings_ = embed(messages)

    calculate_sentence_similarity(message_embeddings_)


run_and_plot(messages)
