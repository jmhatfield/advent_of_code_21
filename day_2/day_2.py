class Day2:
    def __init__(self):
        pass

    def part_1(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        horizontal_position = 0
        depth = 0

        for line in input:
            direction = line.split()[0]
            value = int(line.split()[1])

            if direction == 'forward':
                horizontal_position += value
            elif direction == 'down':
                depth += value
            elif direction == 'up':
                depth -= value

        file.close()

        return horizontal_position * depth

    def part_2(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        aim = 0
        horizontal_position = 0
        depth = 0

        for line in input:
            direction = line.split()[0]
            value = int(line.split()[1])

            if direction == 'forward':
                horizontal_position += value
                if aim > 0:
                    depth += (aim * value)
            elif direction == 'down':
                aim += value
            elif direction == 'up':
                aim -= value

        file.close()

        return horizontal_position * depth

if __name__ == '__main__':
    instance = Day2()
    print(instance.part_1('input_2.txt'))
    print(instance.part_2('input_2.txt'))
