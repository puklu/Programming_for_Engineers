# hw01

# Vivek Punia

import sys


# calculates parity of a number
def calculate_parity(x):
    if x % 2 == 0:
        return 0
    else:
        return 1


def make_parity_matrix_right(array):
    rows = len(array)
    cols = len(array[0])
    right_matrix = [['?'] * cols for i in range(rows)]

    for i in range(0, rows):
        second_last_col = cols - 3
        parity_of_last_element = calculate_parity(array[i][len(array[0]) - 1])
        parity_of_second_last_element = calculate_parity(array[i][len(array[0]) - 2])

        if parity_of_last_element == parity_of_second_last_element:
            if parity_of_last_element == 1:
                right_matrix[i][second_last_col] = 'odd'

            else:
                right_matrix[i][second_last_col] = 'even'

        else:
            right_matrix[i][second_last_col] = 'mixed'

    for row in range(0, rows):
        for col in range(cols - 4, -1, -1):
            if right_matrix[row][col + 1] == 'odd':
                if array[row][col + 1] == 1:
                    right_matrix[row][col] = 'odd'
                if array[row][col + 1] == 0:
                    right_matrix[row][col] = 'mixed'

            elif right_matrix[row][col + 1] == 'even':
                if array[row][col + 1] == 1:
                    right_matrix[row][col] = 'mixed'
                if array[row][col + 1] == 0:
                    right_matrix[row][col] = 'even'

            else:
                right_matrix[row][col] = 'mixed'

    # print_matrix(right_matrix)
    return right_matrix


def make_parity_matrix_left(array):
    rows = len(array)
    cols = len(array[0])
    left_matrix = [['?'] * cols for i in range(rows)]

    for i in range(0, rows):
        parity_of_first_element = calculate_parity(array[i][0])
        parity_of_second_element = calculate_parity(array[i][1])

        if parity_of_first_element == parity_of_second_element:
            if parity_of_first_element == 1:
                left_matrix[i][2] = 'odd'

            else:
                left_matrix[i][2] = 'even'

        else:
            left_matrix[i][2] = 'mixed'

    for row in range(0, rows):
        for col in range(3, cols):
            if left_matrix[row][col - 1] == 'odd':
                if array[row][col - 1] == 1:
                    left_matrix[row][col] = 'odd'
                if array[row][col - 1] == 0:
                    left_matrix[row][col] = 'mixed'

            elif left_matrix[row][col - 1] == 'even':
                if array[row][col - 1] == 1:
                    left_matrix[row][col] = 'mixed'
                if array[row][col - 1] == 0:
                    left_matrix[row][col] = 'even'

            else:
                left_matrix[row][col] = 'mixed'

    # print_matrix(left_matrix)
    return left_matrix


def make_parity_matrix_above(array):
    rows = len(array)
    cols = len(array[0])
    above_matrix = [['?'] * cols for i in range(rows)]

    for i in range(0, rows):
        parity_of_first_element = calculate_parity(array[i][0])
        parity_of_second_element = calculate_parity(array[i][1])

        if parity_of_first_element == parity_of_second_element:
            if parity_of_first_element == 1:
                above_matrix[i][2] = 'odd'

            else:
                above_matrix[i][2] = 'even'

        else:
            above_matrix[i][2] = 'mixed'

    for row in range(0, rows):
        for col in range(3, cols):
            if above_matrix[row][col - 1] == 'odd':
                if array[row][col - 1] == 1:
                    above_matrix[row][col] = 'odd'
                if array[row][col - 1] == 0:
                    above_matrix[row][col] = 'mixed'

            elif above_matrix[row][col - 1] == 'even':
                if array[row][col - 1] == 1:
                    above_matrix[row][col] = 'mixed'
                if array[row][col - 1] == 0:
                    above_matrix[row][col] = 'even'

            else:
                above_matrix[row][col] = 'mixed'

    # print_matrix(above_matrix)
    return above_matrix


def make_parity_matrix_below(array):
    rows = len(array)
    cols = len(array[0])
    below_matrix = [['?'] * cols for i in range(rows)]

    for i in range(0, rows):
        second_last_col = cols - 3
        parity_of_last_element = calculate_parity(array[i][len(array[0]) - 1])
        parity_of_second_last_element = calculate_parity(array[i][len(array[0]) - 2])

        if parity_of_last_element == parity_of_second_last_element:
            if parity_of_last_element == 1:
                below_matrix[i][second_last_col] = 'odd'

            else:
                below_matrix[i][second_last_col] = 'even'

        else:
            below_matrix[i][second_last_col] = 'mixed'

    for row in range(0, rows):
        for col in range(cols - 4, -1, -1):
            if below_matrix[row][col + 1] == 'odd':
                if array[row][col + 1] == 1:
                    below_matrix[row][col] = 'odd'
                if array[row][col + 1] == 0:
                    below_matrix[row][col] = 'mixed'

            elif below_matrix[row][col + 1] == 'even':
                if array[row][col + 1] == 1:
                    below_matrix[row][col] = 'mixed'
                if array[row][col + 1] == 0:
                    below_matrix[row][col] = 'even'

            else:
                below_matrix[row][col] = 'mixed'

    # print_matrix(below_matrix)
    return below_matrix


# to print a matrix in readable format
def print_matrix(array):
    # print(array)
    for row in range(len(array)):
        print(array[row])
    print()


# to create the parity sensitive matrix
def create_parity_matrix(M, N, input1):
    # the final matrix that will contain the parity sensitivity of elements
    result_matrix = [['.'] * N for i in range(M)]
    # a matrix that contains the parity value of each element
    parity_matrix = [['.'] * N for i in range(M)]
    # print_matrix(parity_matrix)

    # creating the parity matrix
    for i in range(0, M):
        for j in range(0, N):
            parity_matrix[i][j] = calculate_parity(input1[i][j])

    # print_matrix(parity_matrix)

    # transposing the parity matrix, makes it easy to check parity of elements above and below an index
    tr_parity_matrix = list(zip(*parity_matrix))

    # print_matrix(tr_parity_matrix)

    right = make_parity_matrix_right(parity_matrix)
    left = make_parity_matrix_left(parity_matrix)
    below = make_parity_matrix_below(tr_parity_matrix)
    above = make_parity_matrix_above(tr_parity_matrix)

    # finally, creating the parity sensitivity matrix
    for row in range(0, M):
        for col in range(0, N):
            while 1:
                if right[row][col] == 'even':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of right")
                    break
                elif right[row][col] == 'odd':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of right")
                    break

                elif left[row][col] == 'even':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of left")
                    break
                elif left[row][col] == 'odd':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of left")
                    break

                elif above[col][row] == 'even':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of above")
                    break
                elif above[col][row] == 'odd':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of above")
                    break

                elif below[col][row] == 'even':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of below")
                    break
                elif below[col][row] == 'odd':
                    result_matrix[row][col] = 'x'
                    # print("breaking out of below")
                    break

                else:
                    # print("breaking out of nope")
                    break

    # removing the quotes from the characters
    for i in range(len(result_matrix)):
        separator = " "
        result_matrix[i] = separator.join(result_matrix[i])

    # printing the final answer
    # print_matrix(result_matrix)

    output = ''
    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[0])):
            output += result_matrix[i][j]
            if j < len(result_matrix[0]) - 1:
                output += ' '
        if i < len(result_matrix) - 1:
            output += '\n'
    print(output)



if __name__ == '__main__':
    # matrix for testing
    # inp = [[8, 8],
    #        [2, 3, 4, 8, 7, 9, 7, 1],
    #        [3, 1, 5, 6, 2, 4, 1, 9],
    #        [1, 9, 1, 1, 6, 2, 2, 1],
    #        [2, 3, 7, 6, 5, 3, 8, 2],
    #        [8, 8, 5, 7, 6, 1, 3, 7],
    #        [8, 9, 2, 8, 5, 5, 3, 7],
    #        [4, 4, 6, 1, 9, 7, 9, 7],
    #        [3, 8, 9, 4, 6, 4, 4, 6]]
    #
    # no_of_rows = inp[0][0]
    # no_of_columns = inp[0][1]

    # input_matrix = inp[1:no_of_rows + 1][0:no_of_columns]

    user_input = input()

    no_of_rows, no_of_columns = user_input.split()

    no_of_rows = int(no_of_rows)
    no_of_columns = int(no_of_columns)

    input_matrix = [['.'] * no_of_columns for i in range(no_of_rows)]

    for i in range(0, no_of_rows):
        input_matrix[i] = input().split()

    for i in range(0, no_of_rows):
        for j in range(0, no_of_columns):
            input_matrix[i][j] = int(input_matrix[i][j])

    create_parity_matrix(no_of_rows, no_of_columns, input_matrix)
