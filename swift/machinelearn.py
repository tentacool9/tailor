import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re
import pickle
import joblib
import Analyzer

import matplotlib.pyplot as plt
from sklearn.decomposition import pca, PCA
from sklearn.metrics import adjusted_rand_score


# parse the data, so actual characters are ignored and replaced with a dummy char,
# as well as marking spaces with a dummy char
# the idea is to be agnostic to the data in the document,
# therefore getting tid of all english letters and numbers is a good starting point
# json example: { "name" : "david", "id": 8472422, "ip": "10.0.0.1" } => {"c":"c", "c":"c", "c":"c"}
def parse(raw_documents):
    parsed_documents = []
    temp_doc = ""
    # REFACTOR?
    # single document
    if type(raw_documents) is str:
        temp_doc = re.sub(r'[a-zA-Z_0-9@!?\",]', '', raw_documents)
        return [temp_doc]
    # a few documents in an array to be parsed
    for document in raw_documents:
        temp_doc = re.sub(r'[a-zA-Z_0-9@!?\",]', '', document)
        parsed_documents.append(temp_doc)
    # check that the data is not only a single message in the array
    if len(parsed_documents) < 2:
        return parsed_documents[0]
    print(parsed_documents)
    return parsed_documents


def train_model():
    documents = []
    # training data
    lines = ""
    with open('/home/david/Documents/xml', 'r') as reader:
        for line in reader:
            if line != 'sep\n' and line != 'sep':
                lines += line
            else:
                documents.append(lines)
                lines = ""
    documents.append(lines)
    # print out raw training data
    print(documents)

    vectorizer = TfidfVectorizer(analyzer='char')

    X = vectorizer.fit_transform(parse(documents))

    true_k = 3
    model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model.fit(X)

    # save the trained model
    joblib.dump(model, '/home/david/Documents/trained_clustering.pkl')
    print("im here")
    print("Top terms per cluster:")
    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names()
    for i in range(true_k):
        print("Cluster %d:" % i),
        for ind in order_centroids[i, :10]:
            print(ind)
            print(' %s' % terms[ind]),
        print

    print("\n")
    pickle.dump(vectorizer, open("/home/david/Documents/trained_vectorizer.pkl", "wb"))


def test_clustering(k, isprint):
    filelist = ["json_yaml", "xml", "csv_tsv"]
    cluster_map = []
    cluster_names = [0 for i in range(k)]
    for eltype in filelist:
        analyzer = Analyzer.Analyzer('/home/david/Documents/trained_clustering.pkl',
                                     '/home/david/Documents/testfolder/' + eltype,
                                     '/home/david/Documents/trained_vectorizer.pkl', [i for i in range(k)])
        index = analyzer.find_d_format(isprint)
        cluster_map.append(index)
        cluster_names[index] = eltype
        if len(cluster_map) != len(set(cluster_map)):
            if isprint:
                print(cluster_map)
                print("failed on %s" % (eltype))
            return ["ml error"]
    return cluster_names
