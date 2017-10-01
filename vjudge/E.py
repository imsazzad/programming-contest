test_case = input().strip();
test_case = int(test_case);

parent_node_dict = {};
num_of_children_for_parent_array = [0] * 1;

node_number_with_max_children = 0;
max_children_number = 0;


def parent_children_update(parent, children, very_first_children):
    try:
        parent_node_dict[str(children)] = parent;
        if (parent == very_first_children):
            return;

        num_of_children_for_parent_array[parent] += 1;
        parent_of_current_parent = parent_node_dict[parent];
        parent_children_update(parent_of_current_parent, parent);

    except:
        return;


for i in range(1, test_case):
    total_edge_or_total_nodes = input().strip();
    total_edge_or_total_nodes = int(total_edge_or_total_nodes);

    parent_node_dict = {};
    num_of_children_for_parent_array = [0] * (total_edge_or_total_nodes + 1)

    for j in range(total_edge_or_total_nodes):
        a, b = input().strip().split(" ")
        a, b = int(a), int(b);
        very_first_children = a;
        parent_children_update(a, b, very_first_children);

        if (max_children_number < num_of_children_for_parent_array[a]):
            max_children_number = num_of_children_for_parent_array[a];
            node_number_with_max_children = a;

        elif (max_children_number == num_of_children_for_parent_array[a]):
            if (node_number_with_max_children > a):
                node_number_with_max_children = a;

    print("Case", str(i) + ":", node_number_with_max_children);
#
# 3
# 3
# 1 2
# 2 3
# 3 1
# 4
# 1 2
# 2 1
# 4 3
# 3 2
# 5
# 1 2
# 2 1
# 5 3
# 3 4
# 4 5
