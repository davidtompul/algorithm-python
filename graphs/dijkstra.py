from queue import PriorityQueue


def dijkstra(adj_list_local, start):
    dist = [float('inf') for x in range(len(adj_list_local))]
    dist[0] = 0
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        current_node = pq.get()
        if current_node[0] > dist[current_node[1]]:
            continue
        for node in adj_list_local[current_node[1]]:
            if dist[current_node[1]] + node[1] < dist[node[0]]:
                dist[node[0]] = dist[current_node[1]] + node[1]
                pq.put((dist[node[0]], node[0]))
    return dist


def test_priority_queue():
    pq = PriorityQueue()
    pq.put((1, 2, 3))
    pq.put((4, 3))
    pq.put((2, 0))
    while not pq.empty():
        print(pq.get())


if __name__ == '__main__':
    adj_list = [[] for x in range(5)]
    adj_list[0] = [(1, 3), (2, 12)]
    adj_list[1] = [(3, 2), (4, 4)]
    adj_list[4] = [(0, 12)]
    print("dfs() output: ")
    # test_priority_queue()
    dist = dijkstra(adj_list, 0)
    for dist_i in range(len(dist)):
        print(" 0 to {} = {}".format(dist_i, dist[dist_i]))
