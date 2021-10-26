def bruh(s,c,i):
    for j in range(len(s)):
        if G.nodes[s[j]]['colour']==str(c):
            return True
        """elif s[j]>=i:
            return False"""
    return False
def find_smallest_colour(G,i):
    n = len(G.nodes())
    c=1
    b=True
    s=list(G.adj[i])
    while b==True:
        if bruh(s,c,i)==False:
            b=False
        else:
            c+=1
    return str(c)
def greedy(G):
    global kmax
    kmax=1
    for i in range(1,len(G.nodes())+1):
        c=find_smallest_colour(G,i)
        G.nodes[i]['colour']=c
        if int(c)>kmax:
            kmax=int(c)
    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colours that Greedy computed is:', kmax)