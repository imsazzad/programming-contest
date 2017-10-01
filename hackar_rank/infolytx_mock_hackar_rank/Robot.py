class Bot:
    # rotating_direction = ['N', 'E', 'S', 'W'];
    next_direction = {
        'N': {'R': 'E',
              'L': 'W',
              'F': [0, 1]},
        'S': {'R': 'W',
              'L': 'E',
              'F': [0, -1]},
        'E': {'R': 'S',
              'L': 'N'
            , 'F': [1, 0]},
        'W': {'R': 'N',
              'L': 'S'
            , 'F': [-1, 0]},
    }

    def handle_rotation(self, instrucion):
        # if(instrucion == 'R' or instrucion == 'L'):
        self.direction = Bot.next_direction[self.direction][instrucion];

    def handle_forward(self, instrucion):
        # if (instrucion == 'F'):
        add_pos = Bot.next_direction[self.direction][instrucion];
        new_x_postion = self.x_cor + add_pos[0];
        new_y_postion = self.y_cor + add_pos[1];

        if (new_x_postion > len(World.matrix) or new_x_postion < 0):
            self.status = 'LOST';
            World.matrix[self.x_cor][self.y_cor] = 'LOST';
            return;

        if (new_y_postion > len(World.matrix[0]) or new_y_postion < 0):
            self.status = 'LOST';
            World.matrix[self.x_cor][self.y_cor] = 'LOST';
            return;
        # print(new_x_postion, new_y_postion)
        if (World.matrix[new_x_postion][new_y_postion] == 'LOST'):
            return;

        self.x_cor = new_x_postion;
        self.y_cor = new_y_postion;

    def __init__(self, x_cor, y_cor, direction, track):
        self.x_cor = x_cor;
        self.y_cor = y_cor;
        self.direction = direction;
        self.track = track;
        self.status = None;

    def getCurrentPosition(self):
        for c in track:
            if (c == 'F'):
                self.handle_forward(c);
            else:
                self.handle_rotation(c);
        if (self.status == 'LOST'):
            return self.x_cor, self.y_cor, self.direction, self.status;
        else:
            return self.x_cor, self.y_cor, self.direction;


class World:
    matrix = [[]]

    def __init__(self, w, h):
        pass


if __name__ == "__main__":
    width, height = input().strip().split(' ')
    width, height = [int(width), int(height)]
    World.matrix = [[0 for x in range(width + 1)] for y in range(height + 1)]
    # print("mat", World.matrix);
    while (True):
        line = input();
        if (line):
            pos_x, pos_y, direction = line.strip().split(' ')
            pos_x, pos_y, direction = int(pos_x), int(pos_y), str(direction)
            track = input();
            bot1 = Bot(pos_x, pos_y, direction, track);
            print(" ".join(map(str, bot1.getCurrentPosition())))
            # print();
        else:
            break;


            # Sample input
            # 5 3
            # 1 1 E
            # RFRFRFRF
            # 3 2 N
            # FRRFLLFFRRFLL
            # 0 3 W
            # LLFFFLFLFL

            # Sample Output
            # 1 1 E
            # 3 3 N LOST
            # 2 3 S
