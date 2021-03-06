# There are n cities connected by m flights. 
# Each flight starts from city u and arrives at v with a price w.

# Now given all the cities and flights, 
# together with starting city src and the destination dst, 
# your task is to find the cheapest price from src to dst with up to k stops. 
# If there is no such route, output -1.

# Example 1:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, 
# as marked red in the picture.

# Example 2:
# Input: 
# n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation: 
# The graph looks like this:


# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, 
# as marked blue in the picture.

 

# Constraints:

#     The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
#     The size of flights will be in range [0, n * (n - 1) / 2].
#     The format of each flight will be (src, dst, price).
#     The price of each flight will be in the range [1, 10000].
#     k is in the range of [0, n - 1].
#     There will not be any duplicated flights or self cycles.

# ===============================================================================

# We will create a Adjacency matrix
# and we will use min priority queue (based on price - the first parameter)
# and will insert the source into that , and edges which is K+1
# as 1 Stop means 2 edges
# we will pop every node from queue 
# and check if we get destination node and with in K limit - we return it
# else, we will push its nearest node

# we will use a graph

# Accepted in Leetcode
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        # build the adjacency list
        adj_list = {u : [] for u in range(n)}
        for f in flights:
            adj_list[f[0]].append((f[1], f[2]))
        
        # Now we will use the priority queue
        queue = []
        queue.append((0, src, K+1))

        while len(queue) > 0:
            top = heapq.heappop(queue)
            d, u, e = top
            if dst == u: return d
            if e > 0:
                for v in adj_list[u]:
                    heapq.heappush(queue, (d + v[1], v[0], e-1))
        
        return -1

# =====================================================================================