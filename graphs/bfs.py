def bfs(adj_list_local, visited_node, start):
    node_queue = [start]

    while node_queue:
        cur_node = node_queue.pop()
        visited_node[cur_node] = True
        print(cur_node)
        for node in adj_list_local[cur_node]:
            if not visited_node[node]:
                node_queue.insert(0, node)


if __name__ == '__main__':
    adj_list = [[] for x in range(5)]
    visited = [False for x in range(5)]
    adj_list[0] = [1, 2]
    adj_list[1] = [3, 4]
    adj_list[4] = [0]
    print("dfs() output: ")
    bfs(adj_list, visited, 0)
