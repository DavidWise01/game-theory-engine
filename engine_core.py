def quorum(votes):
 c={}
 for v in votes:c[v]=c.get(v,0)+1
 return max(c,key=c.get)
