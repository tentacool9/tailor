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
    def __init__(self, data_input, data_type):
        # data input path will remain a
        self.data_path = data_input
        self.data_type = data_type

    def analyze_data(self):
        supported_data = {"JSON": self.json_analyze(),"YAML": self.yaml_analyze() }

    # format supported: {"field":data,"field":data}
    def json_analyze(self):
        print("analyze")


    def yaml_analyze(self):
        print("analyze")

