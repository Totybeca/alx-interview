#!/usr/bin/python3
from collections import deque

def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n  # initialize all boxes as unvisited
    visited[0] = True  # mark the first box as visited
    queue = deque([0])  # start BFS from the first box

    while queue:
        box = queue.popleft()
        for key in boxes[box]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

