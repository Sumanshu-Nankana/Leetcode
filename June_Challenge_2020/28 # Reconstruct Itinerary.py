# Given a list of airline tickets represented by pairs of departure and arrival 
# airports [from, to], reconstruct the itinerary in order. 
# All of the tickets belong to a man who departs from JFK. 
# Thus, the itinerary must begin with JFK.

# Note:

#     If there are multiple valid itineraries, you should return the 
#     itinerary that has the smallest lexical order when read as a single string. 
#     For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than 
#     ["JFK", "LGB"].
#     All airports are represented by three capital letters (IATA code).
#     You may assume all tickets form at least one valid itinerary.
#     One must use all the tickets once and only once.

# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.

# ==============================================================================
# Accepted in Leetcode

import collections
class Solution(object):
    def findItinerary(self, tickets):
        if len(tickets)==0:
            return
        dic = collections.defaultdict(list)
        for src,dest in tickets:
            dic[src].append(dest)

        
        output = ["JFK"]
        def dfs(src):
            if len(output) == len(tickets)+1:
                return True
            
            destinations = sorted(dic[src])
            for destination in destinations:
                # perform bracktracking
                output.append(destination)
                dic[src].remove(destination)
                
                if dfs(destination):
                    return True
                dic[src].append(destination)
                output.pop()
        
        dfs("JFK")
        return output

# =================================================================
# Accepted in Leetcode

class Solution(object):
    def findItinerary(self, tickets):
        self.adj = {}
        tickets.sort(key = lambda x: x[1])
        
        for u,v in tickets:
            if u in self.adj: self.adj[u].append(v)
            else: self.adj[u] = [v]
        
        self.result = []
        self.dfs("JFK")
        
        return self.result[::-1]
    
    
    def dfs(self, s):
        while s in self.adj and len(self.adj[s]) > 0:
            v = self.adj[s][0]
            self.adj[s].pop(0)
            self.dfs(v)
        
        self.result.append(s)
# ==============================================================================