import operator

while True:
    node, edge = input().strip().split(' ');  # python 2 raw input
    node, edge = [int(node), int(edge)];
    if (node == 0 and edge == 0):
        break;
    sorted_edge = {};
    for i in range(edge):
        x, y, z = input().strip().split(' ');
        x, y, z = [int(x), int(y), int(z)];
        sorted_edge[str(x) + "#" + str(y)] = z;
    sorted_edge = sorted(sorted_edge.values());
    sorted_edge = sorted(sorted_edge.items(), key=operator.itemgetter(1))
    print(sorted_edge);
#
# 7 11
# 0 1 7
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11
# 0 0
