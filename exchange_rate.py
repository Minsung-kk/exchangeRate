import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# load file
path = './data/2020_2019.csv'
pd = pd.read_csv(path)
print(pd.head())

