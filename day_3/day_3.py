class Day3:
    def __init__(self):
        pass

    def part_1(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        gamma_rate = []
        epsilon_rate = []

        for i in range(len(input[0]) - 1):
            zero_bit_count = 0
            one_bit_count = 0
            for line in input:
                bit = line[i]
                if bit == '0':
                    zero_bit_count += 1
                elif bit == '1':
                    one_bit_count += 1
            if zero_bit_count > one_bit_count:
                gamma_rate.append('0')
                epsilon_rate.append('1')
            elif one_bit_count > zero_bit_count:
                gamma_rate.append('1')
                epsilon_rate.append('0')

        gamma_rate = ''.join(gamma_rate)
        epsilon_rate = ''.join(epsilon_rate)

        gamma_rate = int(gamma_rate, 2)
        epsilon_rate = int(epsilon_rate, 2)

        file.close()

        return gamma_rate * epsilon_rate

    def part_2(self, filename):
        file = open(filename, 'r')
        input = file.readlines()

        oxygen_rating = 0
        co2_rating = 0
        filtered_oxygen = input
        filtered_co2 = input

        for i in range(len(input[0]) - 1):
            if len(filtered_oxygen) == 1:
                break

            zero_bit_count = 0
            one_bit_count = 0
            most_common = ''
            for line in filtered_oxygen:
                bit = line[i]
                if bit == '0':
                    zero_bit_count += 1
                elif bit == '1':
                    one_bit_count += 1

            if zero_bit_count > one_bit_count:
                most_common = '0'
            elif one_bit_count >= zero_bit_count:
                most_common = '1'

            filtered_oxygen = list(filter(lambda x: x[i] == most_common, filtered_oxygen))

        for i in range(len(input[0]) - 1):
            if len(filtered_co2) == 1:
                break

            zero_bit_count = 0
            one_bit_count = 0
            least_common = ''
            for line in filtered_co2:
                bit = line[i]
                if bit == '0':
                    zero_bit_count += 1
                elif bit == '1':
                    one_bit_count += 1

            if zero_bit_count <= one_bit_count:
                least_common = '0'
            elif one_bit_count < zero_bit_count:
                least_common = '1'

            filtered_co2 = list(filter(lambda x: x[i] == least_common, filtered_co2))

        oxygen_rating = int(filtered_oxygen[0], 2)
        co2_rating = int(filtered_co2[0], 2)

        file.close()

        return oxygen_rating * co2_rating

if __name__ == '__main__':
    instance = Day3()
    print(instance.part_1('input_3.txt'))
    print(instance.part_2('input_3.txt'))
