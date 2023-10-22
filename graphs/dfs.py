def dfs(adj_list_local, visited_node, cur_node):
    if visited_node[cur_node]:
        return
    visited_node[cur_node] = True
    print(cur_node)
    for node in adj_list_local[cur_node]:
        dfs(adj_list_local, visited_node, node)


def dfs_loop(adj_list_local, visited_node, start):
    node_stack = [start]

    while node_stack:
        cur_node = node_stack.pop()
        visited_node[cur_node] = True
        print(cur_node)
        for nodeIdx in range(len(adj_list_local[cur_node]) - 1, -1, -1):
            if not visited_node[adj_list_local[cur_node][nodeIdx]]:
                node_stack.append(adj_list_local[cur_node][nodeIdx])


if __name__ == '__main__':
    adj_list = [[] for x in range(5)]
    visited = [False for x in range(5)]
    adj_list[0] = [1, 2]
    adj_list[1] = [3, 4]
    adj_list[4] = [0]
    print("dfs() output: ")
    dfs(adj_list, visited, 0)

    visited = [False for x in range(5)]
    print("dfs_loop() output: ")
    dfs_loop(adj_list, visited, 0)
