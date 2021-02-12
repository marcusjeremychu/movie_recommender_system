import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import os

class Recommender():

    def __init__(self, root_fp, nrows=1000):
        print("Initializing...")
        self.genome_scores = pd.read_csv(os.path.join(root_fp, "genome-scores.csv"), nrows=nrows)
        self.genome_tags = pd.read_csv(os.path.join(root_fp, "genome-tags.csv"), nrows=nrows)
        self.links = pd.read_csv(os.path.join(root_fp, "links.csv"), nrows=nrows)
        self.movies = pd.read_csv(os.path.join(root_fp, "movies.csv"), nrows=nrows)
        self.ratings = pd.read_csv(os.path.join(root_fp, "ratings.csv"), nrows=nrows)
        self.tags = pd.read_csv(os.path.join(root_fp, "tags.csv"), nrows=nrows)

        print(self.movies.head)