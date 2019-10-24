import os
import pickle
import re
import sys

import matplotlib.pyplot as plt
from sklearn.decomposition import pca
from sklearn.feature_extraction.text import TfidfVectorizer

from machinelearn import parse

import joblib


class Analyzer:
    # this function takes in the model path, and data input source, the data input
    # source can be a string or a path
    def __init__(self, model_path, data_input, vectorizer_path, cluster_mapping):
        self.model_path = model_path
        self.cluster_mapping = cluster_mapping
        self.vectorizer_path = vectorizer_path
        # data input path will remain a
        self.data_path = data_input
        self.ANALYZE_MAX_SIZE = 1000

    def find_d_format(self,isprint):
        check_file = re.compile("^(\/+\w{0,}){0,}\.\w{1,}$")
        check_directory = re.compile("^(\/+\w{0,}){0,}$")
        data_input = ""
        #suppress printing
        if not isprint:
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")
        if check_file.match(self.data_path) or check_directory.match(self.data_path):
            with open(self.data_path, 'r') as reader:
                for line in reader:
                    # if too much data is received it will cause issues, therefore cutting it to be under a certain -
                    # volume is good (analyze_data_size)
                    if len(data_input) > self.ANALYZE_MAX_SIZE:
                        break
                    data_input += line
        else:
            raise Exception("Data input should be a path")

        vectorizer = pickle.load(open(self.vectorizer_path, 'rb'))
        model = joblib.load(self.model_path)

        print("Prediction")

        # predict data type
        print(data_input)
        y = vectorizer.transform(parse(data_input))
        score = model.score(y)
        print(vectorizer.vocabulary_)
        print(y)
        print(score)

        prediction = model.predict(y)
        print(prediction)
        prediction = prediction[0]
        if not isprint:
            sys.stdout = old_stdout
        return self.cluster_mapping[prediction]

    # def json_analyze(self):
    #     matches = 0
    #     json_data = ""
    #     with open(self.data_path, 'r') as reader:
    #         for line in reader:
    #             json_data += ''.join(line)
    #             open_bracket = len(tuple(re.finditer(r'{',json_data)))
    #             close_bracket = len(tuple(re.finditer(r'}', json_data)))
    #             if close_bracket > open_bracket:
    #
    #                 matches+=1
    #                 open_bracket-= cl
    #     print(matches)


