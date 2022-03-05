# hw02

# Author: Vivek Punia


# to print the matrix in a readable form
def print_matrix(array):
    # print(array)
    for row in range(len(array)):
        print(array[row])
    print()


# method to clear the canvas given a starting corner and an ending corner
def clear(input_array):
    starting_row = input_array[1]
    starting_col = input_array[2]
    ending_row = input_array[3]
    ending_col = input_array[4]

    for row in range(starting_row, ending_row + 1):
        for col in range(starting_col, ending_col + 1):
            if row <= no_of_rows - 1 and col <= no_of_columns - 1:
                canvas[row][col] = '.'

    # print_matrix(canvas)

# method to draw a rectangle filled with a character, given a starting corner and an ending corner
def rectangle(input_array):
    starting_row = input_array[1]
    starting_col = input_array[2]
    ending_row = input_array[3]
    ending_col = input_array[4]
    character = input_array[5]

    for row in range(starting_row, ending_row + 1):
        for col in range(starting_col, ending_col + 1):
            if row <= no_of_rows - 1 and col <= no_of_columns - 1:
                canvas[row][col] = character

    # print_matrix(canvas)


def substitute(input_array):
    starting_row = input_array[1]
    starting_col = input_array[2]
    ending_row = input_array[3]
    ending_col = input_array[4]
    character1 = input_array[5]
    character2 = input_array[6]

    for row in range(starting_row, ending_row + 1):
        for col in range(starting_col, ending_col + 1):
            if row <= no_of_rows - 1 and col <= no_of_columns - 1:
                if canvas[row][col] == character1:
                    canvas[row][col] = character2

    # print_matrix(canvas)


def pyramid(input_array):
    last_row = input_array[1]
    last_row_starting_col = input_array[2]
    last_row_ending_col = input_array[3]
    character = input_array[4]

    width_of_base = last_row_ending_col - last_row_starting_col + 1

    # calculating height of the pyramid
    height = 0
    number = width_of_base
    while number > 0:
        number -= 2
        height += 1

    # the top row index of the pyramid
    top_row = last_row - height + 1

    # calculating starting column of top row
    if width_of_base % 2 == 1:
        top_row_starting_col = last_row_starting_col + int(width_of_base / 2)
    else:
        top_row_starting_col = last_row_starting_col + int(width_of_base / 2) - 1

    start = top_row_starting_col

    if width_of_base % 2 == 1:
        end = start + 1
    else:
        end = start + 2

    for row in range(top_row, last_row + 1):
        for col in range(start, end):
            if row <= no_of_rows - 1 and col <= no_of_columns - 1 and row >= 0:
                canvas[row][col] = character
        start -= 1
        end += 1
        if start < last_row_starting_col:
            break

    # print_matrix(canvas)


def solution(input_for_canvas):
    for row in range(no_of_commands):
        command = input_for_canvas[row][0]

        if command == 'C' or command == 'c':

            # converting to int
            for k in range(1, len(input_for_canvas[row])):
                input_for_canvas[row][k] = int(input_for_canvas[row][k])

            clear(input_for_canvas[row])

        if command == 'R' or command == 'r':

            # converting to int
            for k in range(1, len(input_for_canvas[row]) - 1):
                input_for_canvas[row][k] = int(input_for_canvas[row][k])

            rectangle(input_for_canvas[row])

        if command == 'S' or command == 's':

            # converting to int
            for k in range(1, len(input_for_canvas[row]) - 2):
                input_for_canvas[row][k] = int(input_for_canvas[row][k])

            substitute(input_for_canvas[row])

        if command == 'P' or command == 'p':

            # converting to int
            for k in range(1, len(input_for_canvas[row]) - 1):
                input_for_canvas[row][k] = int(input_for_canvas[row][k])

            pyramid(input_for_canvas[row])

        # removing the quotes from the characters
    for i in range(len(canvas)):
        separator = " "
        canvas[i] = separator.join(canvas[i])

    output = ''
    for i in range(len(canvas)):
        for j in range(len(canvas[0])):
            output += canvas[i][j]
            if j < len(canvas[0]) - 1:
                output += ' '
        if i < len(canvas) - 1:
            output += '\n'

    print(output)


if __name__ == '__main__':

    no_of_columns, no_of_rows, no_of_commands = input().split()

    no_of_rows = int(no_of_rows)
    no_of_columns = int(no_of_columns)
    no_of_commands = int(no_of_commands)

    canvas = [['.'] * no_of_columns for i in range(no_of_rows)]

    my_list = [[] for i in range(no_of_commands)]
    # print_matrix(canvas)

    for i in range(no_of_commands):
        my_list[i] = input().split()

    solution(my_list)
