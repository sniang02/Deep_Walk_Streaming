# coding: utf-8
import numpy as np

from LoadData import streaming
import dgl
from dgl import DGLGraph
from DeepWalk import DeepWalk_streaming
import matplotlib.pyplot as plt

import networkx as nx

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

if __name__ == '__main__':
    G = DGLGraph()
    iterator = streaming()
    deepwalk = DeepWalk_streaming(G, 3, embedding_size=64, walks_per_vertex=2, walk_length=8)
    deepwalk(iterator=iterator, unit_iter=5, showLoss=False)
    lst_phi = []


    g = dgl.to_networkx(G)

    phi = np.empty((len(g) + 1, 64))
    for i in range(len(g) + 1):
        a, phi_ = deepwalk.skipgram.get_Nodes_and_Phis(i)
        phi[i,:] = phi_[-1]

    nx.draw(g)
    print("phi = ", phi)
    plt.figure()
    phi_scaled = StandardScaler().fit_transform(phi)
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(phi_scaled)
    print(principalComponents.shape)
    plt.scatter(x=principalComponents[:, 0], y=principalComponents[:, 1])
    for i in range(phi.shape[0]):
        plt.annotate(i, (principalComponents[i, 0], principalComponents[i, 1]), fontsize=10)
    plt.xlabel("Principal Component 1", fontweight='bold')
    plt.ylabel("Principal Component 2", fontweight='bold')
    plt.title("2 Component PCA", fontweight='bold')
    plt.show()

    print(phi.shape)

    print('Done.')

