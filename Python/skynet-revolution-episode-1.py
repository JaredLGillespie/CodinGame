# https://www.codingame.com/training/medium/skynet-revolution-episode-1


from collections import deque


def find_closest_exit_link(start_node, links, exit_nodes):
    visited = {start_node}
    queue = deque([(None, start_node)])

    while queue:
        prev_node, node = queue.popleft()

        if node in exit_nodes:
            return prev_node, node

        for neighbor in links[node]:
            if neighbor in visited: continue
            queue.append((node, neighbor))


def solution():
    num_nodes, num_links, num_exits = map(int, input().split())
    links = {l: set() for l in range(num_nodes)}
    for _ in range(num_links):
        node_1, node_2 = map(int, input().split())
        links[node_1].add(node_2)
        links[node_2].add(node_1)

    exit_nodes = {int(input()) for _ in range(num_exits)}

    while True:
        skynet_node = int(input())
        node_1, node_2 = find_closest_exit_link(skynet_node, links, exit_nodes)
        links[node_1].remove(node_2)
        links[node_2].remove(node_1)
        print('{} {}'.format(node_1, node_2))


solution()
