import numpy as np
import pandas as pd
#该函数用来求网站数目，参数为通过read_csv读入的数据，即df
def NumofWeb(date):
    #获取source和target两列的点的集合
    s1 = set(list(df.iloc[:,0]))
    s2 = set(list(df.iloc[:,1]))
    #合并两个集合
    s = s1|s2
    return len(s)
#该函数用于获取数据中边的数量,参数同NumofWeb函数
def NumofLine(date):
    return len(list(df.iloc[:,0]))
#该函数用于求概率转移矩阵
def ProbabilityTransitionMatrix(date):
    #通过NumofWeb函数获得数据中网站的个数并创建一个零矩阵
    n = NumofWeb(date)
    p = np.zeros((NumofWeb(date),NumofWeb(date)))
    for i in range(NumofLine(date)):
        p[df.iloc[i,0]-1,df.iloc[i,1]-1] = 1
    p = np.mat(p)
    #定义一个一维矩阵，获得p每行值的和
    Nump = np.sum(p,axis = 1)
    for i in range(n):
        for j in range(n):
            # 这里判断p中每一行的和是否为0
            if Nump[i,0]:
                p[i, j] = p[i, j] / Nump[i,0]
    return p.transpose()
def PR(A,X,R):
    c = float(input("请输入阈值："))
    while float(np.linalg.norm(np.array(X-R)))>c:
        (X,R) = (R,A*X)
    else:
        print(R)
df = pd.read_csv("demolist.csv")
#阻尼系数
q = 0.85
X = np.mat(np.ones((NumofWeb(df),1)))
eet = np.mat(np.ones((NumofWeb(df),NumofWeb(df))))/NumofWeb(df)
p=ProbabilityTransitionMatrix(df)
A = q*p + (1-q)*eet
R = A*X
PR(A,X,R)


