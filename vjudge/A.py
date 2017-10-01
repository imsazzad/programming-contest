x, y = [int(a) for a in input().split()]
print(x, y)

i = 0

while (True):
    line = input()
    if (line):
        current_status = [a for a in line.split()]
        track = input()
        print(current_status)
        print(track)
    else:
        break;

#
# N = [0, 1];
# S = [0, -1];
# E = [1, 0];
# W = [-1, 0];
D = ['N', ]


def next_position(current_pos, direction, track):
    for i in track:
        if (i == 'F'):
            if (direction == 'E'):
                current_pos[0] += 1;
            if (direction == 'W'):
                current_pos[0] += -1;
            if (direction == 'N'):
                current_pos[1] += 1;
            if (direction == 'S'):
                current_pos[1] += 1;
        elif (i == 'R'):
            5;
        elif (i == 'L'):
            5;
