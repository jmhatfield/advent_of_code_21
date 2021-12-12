class Day4:
    def __init__(self):
        pass

    def part_1(self, filename):
        file = open(filename, 'r')

        numbers = file.readline()
        numbers = list(map(lambda x: int(x), numbers.split(',')))
        boards = []
        board_index = -1
        bingo_number = -1
        bingo_board = -1

        # setup boards
        for line in file.readlines():
            if line == '\n':
                boards.append([])
                board_index += 1
            else:
                line = list(map(lambda x: int(x), line.split()))
                boards[board_index].append(line)

        def check_rows(self, boards):
            for index in range(len(boards)):
                for i in range(5):
                    bingo = True
                    for j in range(5):
                        if boards[index][i][j] != 'X':
                            bingo = False
                    if bingo:
                        return index
            return -1

        def check_cols(self, boards):
            for index in range(len(boards)):
                for i in range(5):
                    bingo = True
                    for j in range(5):
                        if boards[index][j][i] != 'X':
                            bingo = False
                    if bingo:
                        return index
            return -1

        # look for numbers
        for number in numbers:
            for board in boards:
                for row in board:
                    if number in row:
                        index = row.index(number)
                        row[index] = 'X'

            # check if a board got bingo
            row_bingo = check_rows(self, boards)
            if row_bingo >= 0:
                bingo_number = number
                bingo_board = row_bingo
                break
            else:
                col_bingo = check_cols(self, boards)
                if col_bingo >= 0:
                    bingo_numnber = number
                    bingo_board = col_bingo
                    break

        sum = 0
        for row in boards[bingo_board]:
            for number in row:
                if number != 'X':
                    sum += number

        file.close()

        return sum * bingo_number

    def part_2(self, filename):
        file = open(filename, 'r')

        numbers = file.readline()
        numbers = list(map(lambda x: int(x), numbers.split(',')))
        boards = []
        board_index = -1

        # setup boards
        for line in file.readlines():
            if line == '\n':
                boards.append([])
                board_index += 1
            else:
                line = list(map(lambda x: int(x), line.split()))
                boards[board_index].append(line)

        def check_rows(self, board):
            for i in range(len(board)):
                bingo = True
                for j in range(len(board)):
                    if board[i][j] != 'X':
                        bingo = False
                if bingo:
                    return True
            return False

        def check_cols(self, board):
            for i in range(len(board)):
                bingo = True
                for j in range(len(board)):
                    if board[j][i] != 'X':
                        bingo = False
                if bingo:
                    return True
            return False

        board_wins = []

        for board in boards:
            numbers_called = 0
            for number in numbers:
                numbers_called += 1
                for row in board:
                    if number in row:
                        index = row.index(number)
                        row[index] = 'X'
                row_bingo = check_rows(self, board)
                col_bingo = check_cols(self, board)
                if row_bingo or col_bingo:
                    board_wins.append(numbers_called)
                    break

        most_numbers_called = max(board_wins)
        losing_board = board_wins.index(most_numbers_called)
        last_number_called = numbers[most_numbers_called - 1]

        sum = 0
        for row in boards[losing_board]:
            for number in row:
                if number != 'X':
                    sum += number

        file.close()

        return sum * last_number_called

if __name__ == '__main__':
    instance = Day4()
    #print(instance.part_1('input_4.txt'))
    print(instance.part_2('input_4.txt'))
