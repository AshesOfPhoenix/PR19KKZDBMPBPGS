# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd 
from pandas import DataFrame
import matplotlib.pyplot as plt
# %%
baza=pd.read_csv("Netflix_all.csv")
# %%
najboljpopularni=baza.sort_values(by=['averageRating'] , ascending=False).head(1000)
razmerje=najboljpopularni["type"].value_counts()
# %%
df=DataFrame([razmerje[0],razmerje[1]],columns=["type"],index=['Movie',"TV Show"])
# %%
df.plot.pie(subplots=True , figsize=(5,5),autopct='%1.1f%%', startangle=90, colors = ['red', 'pink'])
plt.show()
# %%
slovar={}
for kr in baza['country']:
    if(kr!="0"):
        split=kr.split(", ")
        for s in split:
            if s not in slovar:
                slovar[s]=1
            else:
                num=slovar[s]
                slovar[s]=num+1
# %%
df=pd.DataFrame.from_dict(slovar,orient='index',columns=["num"])
df=df.sort_values("num",ascending=False)
df[df["num"]>10].plot(y="num", kind='barh',figsize=(30,15))
# %%
slovar={}
stevec=0
splitano=""
skip=0
for jak,avg in baza[["director","averageRating"]].iterrows():
    for name in avg:
        if(name!="-1"):
            if(skip!=1):
                if(stevec==0):
                    splitano=name.split(",")
                    for na in splitano:
                        if na not in slovar:
                            slovar[na]=[]
                    stevec+=1
                else:
                    for na in splitano:
                        seznam=slovar[na]
                        seznam.append(name)
                        slovar[na]=seznam
                    stevec=0
            else:
                skip=0
        else:
            skip=1
# %%
def Average(lst): 
    return sum(lst) / len(lst) 

# %%
drugislovar={}
for key in slovar.keys():
        seznam=slovar[key]
        if -1.0 in seznam:
            seznam.remove(-1.0)
        if(len(seznam)>2):
            if Average(seznam)>0:
                drugislovar[key]=Average(seznam)
drugislovar

# %%
import matplotlib.pyplot as plt

# %%
drugislovar={k: v for k, v in sorted(drugislovar.items(), key=lambda item: item[1])}

# %%
from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

# %%
prvih20={}
stevec=0
zadnjih20={}
for key in drugislovar.keys():
    stevec+=1
    if len(drugislovar)-stevec<=5:
        zadnjih20[key]=drugislovar[key]
stevec=0
for key in drugislovar.keys():
    stevec+=1
    if stevec<=5:
        prvih20[key]=drugislovar[key]



# %%
prvih20
# %%

# libraries
import numpy as np
import matplotlib.pyplot as plt
 
# Make fake dataset
height = prvih20.values()
bars = prvih20.keys()
y_pos = np.arange(len(bars))
 
# Create horizontal bars
plt.barh(y_pos, height)
 
# Create names on the y-axis
plt.yticks(y_pos, bars)
 
# Show graphic
plt.show()


# %%

# %%
stevec=0
splitano=""
skip=0
slovardrzave={}
for jak,avg in baza[["director","country",]].iterrows():
     for name in avg:
        if(name!="-1"):
            if(skip!=1):
                if(stevec==0):
                    splitano=name.split(",")
                    for na in splitano:
                        if na not in slovardrzave:
                            slovardrzave[na]=[]
                    stevec+=1
                else:
                    for na in splitano:
                        seznam=slovardrzave[na]
                        for co in name.split(","):
                            if co!="":
                                if co not in seznam and co!="0":
                                    if co[0]==" ":
                                        co=co[1:]
                                    seznam.append(co)
                                slovardrzave[na]=seznam
                    stevec=0
            else:
                skip=0
        else:
            skip=1

# %%
slovardrzave

# %%
usa={}
fra={}
uk={}
som={}
aze={}
for director in drugislovar.keys():
    if "Germany" in slovardrzave[director]:
        if director not in aze.keys():
            aze[director]=drugislovar[director]
    if "India" in slovardrzave[director]:
        if director not in som.keys():
            som[director]=drugislovar[director]
    if "United Kingdom" in slovardrzave[director]:
        if director not in uk.keys():
            uk[director]=drugislovar[director]
    if "France" in slovardrzave[director]:
        if director not in fra.keys():
            fra[director]=drugislovar[director]
    if "United States" in slovardrzave[director]:
        if director not in usa.keys():
            usa[director]=drugislovar[director]
# %%
usa={k: v for k, v in sorted(usa.items(), key=lambda item: item[1])}
#slo={k: v for k, v in sorted(slo.items(), key=lambda item: item[1])}
#sr={k: v for k, v in sorted(sr.items(), key=lambda item: item[1])}
uk={k: v for k, v in sorted(uk.items(), key=lambda item: item[1])}
fra={k: v for k, v in sorted(fra.items(), key=lambda item: item[1])}

# %%
def vrnislovarje(slova):
    prvih20={}
    stevec=0
    zadnjih20={}
    for key in slova.keys():
        stevec+=1
        if len(slova)-stevec<=5:
            zadnjih20[key]=slova[key]
    stevec=0
    for key in slova.keys():
        stevec+=1
        if stevec<=5:
            prvih20[key]=slova[key]
    return prvih20,zadnjih20
# %%
usap,usaz=vrnislovarje(usa)
gerp,gerz=vrnislovarje(aze)
indip,indiz=vrnislovarje(som)
ukp,ukz=vrnislovarje(uk)
frap,praz=vrnislovarje(fra)

# %%
def narisigraf(slovar):
    import numpy as np
    import matplotlib.pyplot as plt
    
    # Make fake dataset
    height = slovar.values()
    bars = slovar.keys()
    y_pos = np.arange(len(bars))
    
    # Create horizontal bars
    plt.barh(y_pos, height)
    
    # Create names on the y-axis
    plt.yticks(y_pos, bars)
    
    # Show graphic
    plt.show()


# %%
drugislovar.keys()

# %%
narisigraf(usap)
narisigraf(usaz)

narisigraf(ukp)
narisigraf(ukz)

narisigraf(frap)
narisigraf(praz)

narisigraf(gerp)
narisigraf(gerz)

narisigraf(indip)
narisigraf(indiz)

# %%
som

# %%
