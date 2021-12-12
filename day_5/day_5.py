import numpy as np

class Day5:
    def __init__(self):
        pass

    def get_max(self, input):
        all_nums = []
        for line in input:
            split = line.split('->')
            for point in split:
                split2 = point.split(',')
                all_nums.append(int(split2[0]))
                all_nums.append(int(split2[1]))

        return max(all_nums) + 1

    def part_1(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        # initialize the grid
        max_num = Day5.get_max(self, input)
        grid = np.zeros((max_num, max_num))

        # plot the points
        for line in input:
            split = line.split('->')
            point1 = (int(split[0].split(',')[0]), int(split[0].split(',')[1]))
            point2 = (int(split[1].split(',')[0]), int(split[1].split(',')[1]))

            line_points = []

            # horizontal
            if point1[0] == point2[0]:
                min_x = min((point1[1], point2[1]))
                max_x = max((point1[1], point2[1]))
                xs = list(range(min_x, max_x + 1))
                line_points = list(map(lambda x: (x, point1[0]), xs))

            # vertical
            elif point1[1] == point2[1]:
                min_y = min((point1[0], point2[0]))
                max_y = max((point1[0], point2[0]))
                ys = list(range(min_y, max_y + 1))
                line_points = list(map(lambda y: (point1[1], y), ys))

            for point in line_points:
                grid[point] += 1

            overlaps = np.count_nonzero(grid >= 2)

        file.close()

        return overlaps

    def part_2(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        # initialize the grid
        max_num = Day5.get_max(self, input)
        grid = np.zeros((max_num, max_num))

        # plot the points
        for line in input:
            split = line.split('->')
            point1 = (int(split[0].split(',')[0]), int(split[0].split(',')[1]))
            point2 = (int(split[1].split(',')[0]), int(split[1].split(',')[1]))

            line_points = []

            # horizontal
            if point1[0] == point2[0]:
                min_x = min((point1[1], point2[1]))
                max_x = max((point1[1], point2[1]))
                xs = list(range(min_x, max_x + 1))
                line_points = list(map(lambda x: (x, point1[0]), xs))

            # vertical
            elif point1[1] == point2[1]:
                min_y = min((point1[0], point2[0]))
                max_y = max((point1[0], point2[0]))
                ys = list(range(min_y, max_y + 1))
                line_points = list(map(lambda y: (point1[1], y), ys))

            # diagonal
            else:
                x_step = y_step = 1
                x_stop = point2[1] + 1
                y_stop = point2[0] + 1
                if point1[1] > point2[1]:
                    x_step = -1
                    x_stop = point2[1] - 1
                if point1[0] > point2[0]:
                    y_step = -1
                    y_stop = point2[0] - 1

                xs = list(range(point1[1], x_stop, x_step))
                ys = list(range(point1[0], y_stop, y_step))

                line_points = list(map(lambda x: (x, ys[xs.index(x)]), xs))

            for point in line_points:
                grid[point] += 1

        overlaps = np.count_nonzero(grid >= 2)

        file.close()

        return overlaps

if __name__ == '__main__':
    instance = Day5()
    print(instance.part_1('input_5.txt'))
    print(instance.part_2('input_5.txt'))
