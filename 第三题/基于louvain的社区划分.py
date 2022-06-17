import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import community.community_louvain

def FindsameValue(dict):
    values_list = list(set(dict.values()))
    club = []
    for i in range(len(values_list)):
        club.append([])

    for k,v in dict.items():
        club[values_list.index(v)].append(k)
    print('社团数目：', len(club))
    print('社团划分：', club)

df = pd.read_csv('demo.csv')
G = nx.from_pandas_edgelist(df,source = "source",target = 'target')


partition = community.community_louvain.best_partition(G)
FindsameValue(partition)

# size = float(len(set(partition.values())))
# pos = nx.spring_layout(G)
# count = 0.
# for com in set(partition.values()) :
#     count = count + 1.
#     list_nodes = [nodes for nodes in partition.keys()
#                                 if partition[nodes] == com]
#     nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 20,
#                                 node_color = str(count / size))
#
#
# nx.draw_networkx_edges(G,pos, alpha=0.5)
# plt.show()
