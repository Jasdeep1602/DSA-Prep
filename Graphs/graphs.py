#el=edge list
#am=adjacency matrix
#al=adjacency list

el=[[0,1],[1,2],[0,3],[3,4],[3,6],[3,7],[4,2],[4,5],[5,2]]

am=[]
al={}

n=8
#adjacency matrix

for i in range(n):
    am.append([0]*n)
print(am)

for u,v in el:
    am[u][v]=1
    
print(am)

#adjacency list
for u,v in el:
    if u not in al:
        al[u]=[v]
    else:
        al[u].append(v)
print(al)
    
    
    
    
    
