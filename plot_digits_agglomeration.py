#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import collections
import seaborn as sns
import numpy as np
from sklearn import metrics
from sklearn.cluster import KMeans

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

def GetCompatibility(df1,df2):
    maxdifference = 65
    dist = np.linalg.norm(df1 - df2)
    compatibility=100 - (dist/maxdifference*100)
    return compatibility
