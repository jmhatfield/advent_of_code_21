import numpy as np

class Day6:
    def __init__(self):
        pass

    def part_1(self, filename, days):
        file = open(filename, 'r')
        input = file.readline()

        states = list(map(lambda x: int(x), input.split(',')))

        for day in range(days):
            new_fish = 0
            for index in range(len(states)):
                if states[index] == 0:
                    new_fish += 1
                    states[index] = 6
                else:
                    states[index] -= 1

            states.extend(np.repeat(8, new_fish))

        file.close()

        return len(states)

    def part_2(self, filename, days):
        file = open(filename, 'r')
        input = file.readline()

        states = np.array(list(map(lambda x: int(x), input.split(','))))

        num_fish = []
        for i in range(9):
            num_fish.append(np.count_nonzero(states == i))

        for day in range(days):
            copy = np.array(num_fish)
            copy[8] = num_fish[0]
            copy[7] = num_fish[8]
            copy[6] = num_fish[0] + num_fish[7]
            copy[5] = num_fish[6]
            copy[4] = num_fish[5]
            copy[3] = num_fish[4]
            copy[2] = num_fish[3]
            copy[1] = num_fish[2]
            copy[0] = num_fish[1]
            num_fish = copy

        total_fish = np.sum(num_fish)

        file.close()

        return total_fish

if __name__ == '__main__':
    instance = Day6()
    # print(instance.part_1('input_6.txt', 80))
    print(instance.part_2('input_6.txt', 256))
