import re
import matplotlib.pyplot as plt
import pandas as pd
pop_text: str
votes_text: str
with open("pop_size.txt") as f:
	pop_text = f.read()
with open("votes.txt") as f:
	votes_text = f.read()
pop_pat = r"[0-9]+.*?.([a-zA-Z]+[\s]?[A-Za-z]+).*?([0-9,]+)"
pop_dat = [(state,int(pop.replace(",","")))for state,pop in re.findall(pop_pat,pop_text)]

votes_pat = r"([a-zA-Z]+[\s]?[a-zA-Z]+?) - ([0-9]+)"
votes_dat = [(state, int(votes)) for (state,votes) in re.findall(votes_pat,votes_text)]
pop_dat = dict(pop_dat)
votes_dat = dict(votes_dat)

byWorth = []
#print(pop_dat.keys())
#print(votes_dat.keys())
for state in set.union(set(pop_dat.keys()), set(votes_dat.keys())):
	#print(state)
	byWorth.append((state,votes_dat[state]/pop_dat[state]))

byWorth.sort(key=lambda p: p[1])
byWorth = [(state, worth) for state, worth in byWorth]
byWorth = dict(byWorth)
df = pd.DataFrame({"state":byWorth.keys(),"voting_power":byWorth.values(),"population":map(lambda x: pop_dat[x],byWorth.keys())})
fig, ax = plt.subplots()
df.plot(x='population',y='voting_power',kind='scatter',ax=ax,title="Voting Power By Population Size")
for i,data in df.iterrows():
    print(data.population)
    ax.annotate(data.state,(data.population,data.voting_power),fontsize=5)
plt.show()