import sys
from collections import defaultdict
from aoc_tools import read_input_to_grid
from heapq import heappop, heappush


# def read_input_to_grid(in_file):
#     f = open(in_file)
#     result = [[c for c in line.strip()] for line in f]
#     f.close()
#     return result

def create_graph_from_grid(grid):
    g = defaultdict(list)  # create graph from matrix, the node is the (r, c) coordinates
    nrows = len(grid)
    ncols = len(grid[0])
    srcs = []

    for r in range(nrows):
        for c in range(ncols):
            for nr, nc in ((r, c + 1), (r + 1, c), (r, c - 1), (r - 1, c)):
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    if grid[r][c] == 'S':
                        srcs.append((r, c))
                        if grid[nr][nc] == 'a':
                            g[(r, c)].append((nr, nc))
                    elif grid[r][c] == 'E':
                        tgt = (r, c)
                    elif grid[r][c] == 'z':
                        if grid[nr][nc] == 'E':
                            g[(r, c)].append((nr, nc))
                        elif grid[nr][nc] == 'S':
                            continue
                        elif ord(grid[nr][nc]) <= ord(grid[r][c]) + 1:
                            g[(r, c)].append((nr, nc))
                    else:
                        if ord(grid[nr][nc]) <= ord(grid[r][c]) + 1:
                            g[(r, c)].append((nr, nc))
                            if grid[r][c] == 'a':
                                srcs.append((r, c))
    return g, srcs, tgt


def dijkstra(g, src, tgt):
    dists = {}  # distances
    for v in g.keys():
        dists[v] = sys.maxsize
    dists[src] = 0
    minq = [(0, src, [src])]  # minimum priority queue

    while minq:
        estimate_dist, v, path = heappop(minq)
        for nb in g[v]:  # breadth-first search
            if nb == tgt:
                return estimate_dist + 1
            estimate_dist = dists[v] + 1
            if estimate_dist < dists[nb]:  # relaxation
                dists[nb] = estimate_dist
                heappush(minq, (estimate_dist, nb, path + [nb]))
    # return path


if __name__ == '__main__':
    # grid = read_input_to_grid('aoc_12_test_data1.txt')
    grid = read_input_to_grid('aoc_12_data1.txt')
    for e in grid:
        print(e)

    g, srcs, tgt = create_graph_from_grid(grid)
    for k, v in g.items():
        print(k, v)
    print(srcs, tgt)

    min_dist = sys.maxsize
    for src in srcs:
        dist = dijkstra(g, src, tgt)
        if dist:
            min_dist = min(min_dist, dist)
    print(min_dist)
