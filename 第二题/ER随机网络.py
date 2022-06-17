import networkx as nx
import matplotlib.pyplot as plt
#总计500点，重连边概率0.25
n,p=500,0.25

G=nx.gnp_random_graph(n,p)
plt.figure(figsize=(32,32))



nx.draw(G,pos=nx.circular_layout(G),node_size=100,node_color="red",with_labels=False)
nx.write_gexf(G,'ER.gexf')
plt.title("G(N,P)")
plt.show()

#度
d=nx.degree(G)
d=dict(nx.degree(G))
print(d)

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
