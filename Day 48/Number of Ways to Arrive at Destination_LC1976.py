import heapq

def countPaths(self, n: int, roads) -> int:
    mod = 1e9 + 7
    heap = []
    dist = [float("inf")]*n
    ways = [0]*n
    dist[0] = 0
    ways[0] = 1
    heapq.heappush(heap,(0,0)) #[dist,node]

    adj = {}
    for i in range(n):
        adj[i] = []
    for a,b,t in roads:
        adj[a].append([b,t])
        adj[b].append([a,t])

    while heap:
        cur_dist , cur_node = heapq.heappop(heap)
        for new_node,new_dist in adj[cur_node]:
            if cur_dist + new_dist < dist[new_node]:
                dist[new_node] = cur_dist + new_dist
                heapq.heappush(heap,(dist[new_node],new_node))
                ways[new_node] = ways[cur_node]
            elif cur_dist + new_dist == dist[new_node]:
                ways[new_node] += ways[cur_node]
                ways[new_node] = int(ways[new_node]%mod)
    
    return int(ways[n-1]%mod)