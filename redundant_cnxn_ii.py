# https://leetcode.com/problems/redundant-connection-ii/description/
class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    def find(self,x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,u,v):
        pu,pv = self.find(u),self.find(v)
        if pu == pv:
            return False
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv] = pu
            self.rank[pu]+=self.rank[pv]
        else:
            self.parent[pu] = pv
            self.rank[pv]+=self.rank[pu]
        return True
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n+1)
        parent = defaultdict(int)
        candidate1 = candidate2= None
        # 3 cases: i) 2 parent ii) Cycle iii) 2 parent + cycle
        # find edges contributing to 2-parent case
        for u,v in edges:
            if parent[v]:
                candidate1 = [parent[v],v]
                candidate2 = [u,v]
                break
            parent[v] = u
        # Now find if there is a cycle
        for u,v in edges:
            if [u,v] == candidate2:
                continue
            if not uf.union(u,v):
                # case iii: has cycle and 2 parent
                if candidate1:
                    return candidate1
                else:
                # case ii: has cylce
                    return [u,v]
        # case i: 2 parent only
        return candidate2
