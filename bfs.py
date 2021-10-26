import networkx as nx
def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.nodes[a]['label'] = 0
    i=0
    while G.nodes[b]['label']==-1:
        for u in list(G.nodes):
            if G.nodes[u]['label'] == i:
                for v in G.adj[u]:
                    if G.nodes[v]['label']==-1:
                        G.nodes[v]['label']=i+1
        i+=1
    return G.nodes[b]['label']