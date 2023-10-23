def bellman_ford(adj_list_local, start):
    dist = [float('inf') for x in range(len(adj_list_local))]
    dist[start] = 0
    for i in range(len(adj_list_local) - 1):
        for u in range(len(adj_list_local)):
            for cur_node in adj_list_local[u]:
                dist[cur_node[0]] = min(dist[cur_node[0]], dist[u] + cur_node[1])
    has_negative_cycle = False
    for u in range(len(adj_list_local)):
        for cur_node in adj_list_local[u]:
            if dist[cur_node[0]] > dist[u] + cur_node[1]:
                has_negative_cycle = True
    return dist, has_negative_cycle


if __name__ == '__main__':
    adj_list = [[] for x in range(5)]
    adj_list[0] = [(1, 3), (2, 12)]
    adj_list[1] = [(3, 2), (4, 4)]
    adj_list[4] = [(0, 12)]
    print("bellman_ford() output: ")
    # test_priority_queue()
    dists, has_neg_cycle = bellman_ford(adj_list, 0)
    print("has negative cycle {}".format(has_neg_cycle))
    for dist_i in range(len(dists)):
        print(" 0 to {} = {}".format(dist_i, dists[dist_i]))

    adj_list[4] = [(0, -8)]
    print("bellman_ford() output: ")
    dists, has_neg_cycle = bellman_ford(adj_list, 0)
    print("has negative cycle {}".format(has_neg_cycle))
    for dist_i in range(len(dists)):
        print(" 0 to {} = {}".format(dist_i, dists[dist_i]))
