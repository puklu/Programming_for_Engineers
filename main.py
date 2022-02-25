# hw01

# Vivek Punia

import sys


# calculates parity of a number
def calculate_parity(x):
    if x % 2 == 0:
        return 0
    else:
        return 1


# to check the parity values of all the elements of a row to the right of some index
def store_parity_row_right(array, index):
    if index < len(array) - 2:
        # print("index=" + str(index))
        # print(len(array) - 2)
        if array[len(array) - 1] == 1:
            store = 'odd'
        else:
            store = 'even'

        for i in range(len(array) - 1, index, -1):
            # print("i= " + str(i))
            # print("store= " + store)
            # print("array= " + str(array[i]))
            if store == 'odd':
                if array[i] == 1:
                    store = 'odd'
                else:
                    store = 'mixed'

            elif store == 'even':
                if array[i] == 1:
                    store = 'mixed'
                else:
                    store = 'even'

            elif store == 'mixed':
                store = 'mixed'


    else:
        store = 'nope'

    # print(store)
    return store


# to check the parity values of all the elements of a row to the left of some index
def store_parity_row_left(array, index):
    if index > 1:
        # print(len(array))
        if array[0] == 1:
            store = 'odd'
        else:
            store = 'even'

        for i in range(0, index):
            # print("i= " + str(i))
            # print("store= " + store)
            # print("array= " + str(array[i]))
            if store == 'odd':
                if array[i] == 1:
                    store = 'odd'
                else:
                    store = 'mixed'

            elif store == 'even':
                if array[i] == 1:
                    store = 'mixed'
                else:
                    store = 'even'

            elif store == 'mixed':
                store = 'mixed'

    else:
        store = 'nope'

    return store


# to check the parity values of all the elements of a column above some index
def store_parity_col_above(array, index):
    if index > 1:
        # print(len(array))
        if array[0] == 1:
            store = 'odd'
        else:
            store = 'even'

        for i in range(0, index):
            # print("i= " + str(i))
            # print("store= " + store)
            # print("array= " + str(array[i]))
            if store == 'odd':
                if array[i] == 1:
                    store = 'odd'
                else:
                    store = 'mixed'

            elif store == 'even':
                if array[i] == 1:
                    store = 'mixed'
                else:
                    store = 'even'

            elif store == 'mixed':
                store = 'mixed'

    else:
        store = 'nope'

    return store


# to check the parity values of all the elements of a column below some index
def store_parity_col_below(array, index):
    if index < len(array) - 2:
        # print(len(array))
        if array[len(array) - 1] == 1:
            store = 'odd'
        else:
            store = 'even'

        for i in range(len(array) - 1, index, -1):
            # print("i= " + str(i))
            # print("store= " + store)
            # print("array= " + str(array[i]))
            if store == 'odd':
                if array[i] == 1:
                    store = 'odd'
                else:
                    store = 'mixed'

            elif store == 'even':
                if array[i] == 1:
                    store = 'mixed'
                else:
                    store = 'even'

            elif store == 'mixed':
                store = 'mixed'

    else:
        store = 'nope'

    return store


# to print a matrix in readable format
def print_matrix(array):
    # print(array)
    for row in range(len(array)):
        print(array[row])
    print()


# to create the parity sensitive matrix
def create_parity_matrix(M, N, input1):
    # no of rows
    # M = input1[0][0]
    # # no of columns
    # N = input1[0][1]

    # M, N = list(map(int, input().split()))

    # input1 = [list(input().split()) for i in range(M)]

    # the final matrix that will contain the parity sensitivity of elements
    result_matrix = [['.'] * N for i in range(M)]
    # a matrix that contains the parity value of each element
    parity_matrix = [['.'] * N for i in range(M)]
    # print(parity_matrix)

    # creating the parity matrix
    for i in range(0, M):
        for j in range(0, N):
            parity_matrix[i][j] = calculate_parity(input1[i][j])
    # print_matrix(parity_matrix)

    # transposing the parity matrix, makes
    # it easy to check parity of elements above and below an index
    tr_parity_matrix = list(zip(*parity_matrix))

    # print(tr_parity_matrix)
    # print(tr_parity_matrix[0])
    # print(store_parity_col_above(tr_parity_matrix[3], 4))

    # finally creating the parity sensitivity matrix
    for row in range(0, M):
        for col in range(0, N):
            while 1:
                # check parity to its right
                # print(store_parity_row_right(parity_matrix[row], col))
                if store_parity_row_right(parity_matrix[row], col) == 'even':
                    # print(str(row) + ",  "+ str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking-store_parity_row_right")
                    break
                # print(store_parity_row_right(parity_matrix[row], col))
                elif store_parity_row_right(parity_matrix[row], col) == 'odd':
                    # print(str(row) + ",  " + str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking-store_parity_row_right")
                    break

                # check parity to its left
                elif store_parity_row_left(parity_matrix[row], col) == 'even':
                    # print(str(row) + ",  " + str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking-store_parity_row_left")
                    break
                elif store_parity_row_left(parity_matrix[row], col) == 'odd':
                    # print(str(row) + ",  " + str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking4-store_parity_row_left")
                    break

                # check parity below it
                elif store_parity_col_below(tr_parity_matrix[col], row) == 'even':
                    # print(str(row) + ",  " + str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking-store_parity_col_below")
                    break
                elif store_parity_col_below(tr_parity_matrix[col], row) == 'odd':
                    # print(str(row) + ",  " + str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking-store_parity_col_below")
                    break

                # check parity above it
                elif store_parity_col_above(tr_parity_matrix[col], row) == 'even':
                    # print(str(row) + ",  " + str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking-store_parity_col_above")
                    break
                elif store_parity_col_above(tr_parity_matrix[col], row) == 'odd':
                    # print(str(row) + ",  " + str(col))
                    result_matrix[row][col] = 'x'
                    # print("breaking-store_parity_col_above")
                    break

                else:
                    # print("breaking-nope")
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
        if  i < len(result_matrix) - 1:
            output += '\n'
    print(output)
    # print(len(output))


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
