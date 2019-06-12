import time

graph_size = 10
counter = 0

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def recursive_print(dis, pre):
    global graph_size

    def print_helper(index, destination):
        if pre[index] == index:
            print("Route : {} -> ".format(index), end="")
            return
        print_helper(pre[index], destination)
        if index == destination:
            print("{} Distance = {}".format(destination, dis[destination]), end="")
        else:
            print("{} -> ".format(index), end="")

    for i in range(graph_size):
        if pre[i] == i:
            print("Route : {} Distance = 0".format(i), end="")
        else:
            print_helper(i, i)
        print("")


def bellman_ford(edges, source):
    global graph_size, counter
    begin = time.perf_counter()
    dis = []  # distance from source to the node
    pre = []  # predecessor of node
    error = False
    for i in range(graph_size):
        dis.append(float('inf'))
        pre.append(i)
    dis[source] = 0
    # Initialize the graph
    for i in range(graph_size - 1):   # |V| - 1 times
        counter += 1
        # change = False
        for edge in edges:
            if dis[edge.u] != float("inf") and dis[edge.v] > (dis[edge.u] + edge.w):
                dis[edge.v] = dis[edge.u] + edge.w
                pre[edge.v] = edge.u
                # change = True
        # if not change:
        #     break
    # check for the negative-weight cycle
    for edge in edges:
        if (dis[edge.u] + edge.w) < dis[edge.v]:
            print("dis[{}] ({}) < dis[{}] ({}) + {}".format(edge.u, dis[edge.u], edge.v, dis[edge.v], edge.w))
            error = True
    end = time.perf_counter()
    return error, dis, pre, end-begin


def main():
    global counter
    edges = []
    edges.append(Edge(0, 9, 9))
    edges.append(Edge(0, 2, 3))
    edges.append(Edge(0, 5, 5))
    edges.append(Edge(7, 9, 2))
    edges.append(Edge(7, 3, 0))
    edges.append(Edge(2, 7, 1))
    edges.append(Edge(9, 4, 3))
    edges.append(Edge(3, 4, 2))
    edges.append(Edge(3, 8, 1))
    edges.append(Edge(8, 2, 8))
    edges.append(Edge(8, 6, 2))
    edges.append(Edge(4, 8, -8))
    edges.append(Edge(6, 1, 0))
    edges.append(Edge(5, 1, 2))
    edges.append(Edge(1, 4, 9))

    err, dis, pre, time_consumption = bellman_ford(edges, 0)
    if err:
        print("Negative-weight cycle exist")
    else:
        print("Time consumption = ", time_consumption)
        recursive_print(dis, pre)
    print("Counter = ", counter)


if __name__ == "__main__":
    main()