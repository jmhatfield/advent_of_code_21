class Day1:
    def __init__(self):
        pass

    def part_1(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        prev = input[0]
        counter = 0

        for curr in input:
            diff = int(curr) - int(prev)
            if diff > 0:
                counter += 1
            prev = curr

        file.close()

        return counter

    def part_2(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        prev_sum = int(input[0]) + int(input[1]) + int(input[2])
        counter = 0

        for i in range(len(input)):
            if i + 2 < len(input):
                curr_sum = int(input[i]) + int(input[i+1]) + int(input[i+2])
                diff = curr_sum - prev_sum
                if diff > 0:
                    counter += 1
                prev_sum = curr_sum

        file.close()

        return counter

if __name__ == '__main__':
    instance = Day1()
    print(instance.part_1('input_1.txt'))
    print(instance.part_2('input_1.txt'))
