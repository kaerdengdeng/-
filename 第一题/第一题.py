import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("thefirstquestion.csv")
G = nx.from_pandas_edgelist(df,"source","target",create_using= nx.Graph)

nx.draw(G, with_labels = True, node_size = 5,node_color="y")
plt.show()

#度
d=nx.degree(G)
d=dict(nx.degree(G))
print(d)

n = len(G.nodes)
#获取平均度
d=dict(nx.degree(G))
print("平均度为：",sum(d.values())/len(G.nodes))
#获取所有可能的度值对应的概率
x=list(range(max(d.values())+1))
y=[i/n for i in nx.degree_histogram(G)]
#绘制度分布
plt.plot(x,y,'ro-')
plt.xlabel("$k$")
plt.ylabel("$p_k$")
plt.title("Degree distribution")
plt.show()

#求平均最短路径
print("平均最短路径：",nx.average_shortest_path_length(G))

#集聚系数
print("集聚系数：",nx.clustering(G))
#平均集聚系数
print("平均集聚系数:",nx.average_clustering(G))

#全局集聚系数
print("全局集聚系数:",nx.transitivity(G))
