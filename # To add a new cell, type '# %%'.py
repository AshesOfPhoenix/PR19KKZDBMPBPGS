# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd 
from pandas import DataFrame
import matplotlib.pyplot as plt
baza=pd.read_csv("Netflix_all.csv")


# %%
seznam={}
for jak,avg in baza[["listed_in"]].iterrows():
    for name in avg:
        splitansez=name.split(", ")
        for sp in splitansez:
            if sp not in seznam:
                seznam[sp]=[]



# %%
len(seznam.keys())

# %%
