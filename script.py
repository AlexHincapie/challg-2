import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

import scipy.cluster.hierarchy as sch
from scipy.linalg import lu_factor
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

##----------------------------------------------
#
# Functions
#


def sum_Challenges(m1,m2,m3,m4,m5,m6):

    if len(m1) == len(m2) == len(m3) == len(m4) == len(m5) == len(m6):
        df_Challenges=[]

        for i in range(len(m1)):
            df_Challenges.append([])
            for j in range(len(m1[0])):
                df_Challenges[i].append(0)

        for i in range(len(df_Challenges)):
            for j in range(len(df_Challenges[0])):
                df_Challenges[i][j] = m1[i][j] + m2[i][j]  + m3[i][j] + m4[i][j]+ m5[i][j] + m6[i][j]

        return df_Challenges
    else:
        return None


def normalize(dataframe):
    result = dataframe.copy()
    for feature_name in dataframe.columns:
        max_value = dataframe[feature_name].max()
        min_value = dataframe[feature_name].min()
        result[feature_name] = (dataframe[feature_name] - min_value) / (max_value - min_value)
    return result

###############
#
# Step 1
#
###############

# Read data source
df_Challenges = pd.read_excel("C:/Users/steff/OneDrive/Documents/Python Scripts/ChLL CSV dinamic proff.xlsx")

# Print debug info
df_Challenges.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 99 entries, 0 to 98
# Columns: 101 entries, User_ID to Ch_100
# dtypes: int64(100), object(1)
# memory usage: 78.2+ KB

# Define matrixes
m1 = ["User_ID", "ChallengeID", "Reviews_counter"]
m2 = ["User_ID", "ChallengeID", "Comments_counter_report"]
m3 = ["User_ID", "ChallengeID", "Follow_Report"]
m4 = ["User_ID", "ChallengeID", "Share_report_counter"]
m5 = ["User_ID", "ChallengeID", "Accept_report"]
m6 = ["User_ID", "ChallengeID", "Test video_report"]

# Define timeframe
df_time = ["ChallengeID", "Days_ago_counter"]

###############
#
# Step 2
#
###############

# Note: Array + Array concatinates and will not add so df_Challenges = [[...m1, ...m2, ...m3, ...m4, ...m5, ...m6]]
df_Challenges = [m1+m2+m3+m4+m5+m6] # len = 1

# Sum matrixes
df_Challenges = sum_Challenges(m1,m2,m3,m4,m5,m6)

if df_Challenges == None:
    print("Not updated")
else:
    for row in df_Challenges:
        print("[", end=" ")
        for element in row:
            print(element, end= "")
        print("]")


###############
#
# Step 3
#
# Note that Step 3 shows exactly the same output as my architecture diagram in the initial google document
###############

print(df_Challenges.head(25))

###############
#
# Step 4
#
###############

m7 = df_Challenges.to_numpy()

print(m7)

print(df_Challenges.mean())

cv = CountVectorizer();
min_max_scaler = preprocessing.MinMaxScaler();

similar_to_Ch_1 = df_Challenges.corrwith(Ch_1_User_ID_values)
query_index = np.random.choice(df_Challenges.shape[1])
print(query_index)