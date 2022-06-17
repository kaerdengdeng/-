from networkx.algorithms.community import girvan_newman
import pandas as pd
import networkx as nx
import itertools

df = pd.read_csv('demo.csv')
G = nx.from_pandas_edgelist(df, source="source", target='target')
k = 6
comp = girvan_newman(G)
limited = itertools.takewhile(lambda c: len(c) <= k, comp)
for communities in limited:
    a = list(tuple(sorted(c) for c in communities))
    print("社团数量：", len(a))
    print(a)




