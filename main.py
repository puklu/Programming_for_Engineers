from numpy import sort


def check_if_valid_date(possible_date):
    possible_month = int(possible_date[1])
    possible_day = int(possible_date[0])

    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]

    if 0 < possible_month < 13:
        if possible_month in months_31:
            if 0 < possible_day < 32:
                return True
        if possible_month in months_30:
            if 0 < possible_day < 31:
                return True
        if possible_month == 2:
            if 0 < possible_day < 29:
                return True
        else:
            return False
    else:
        return False

def extract_DM_date(line):
    date = []
    for word in line:
        if word.endswith("."):
            possible_date = word.split(".")
            # print(possible_date)
            if len(possible_date) == 3:
                # print(check_if_valid_date(possible_date))
                if check_if_valid_date(possible_date):
                    date.append(word)
    print(date)

def find_closest_valid_number(line, month):

    months_31 = ["January", "March", "May", "July", "August", "October", "December"]
    months_30 = ["April", "June", "September", "November"]

    numbers_in_line = [0] * len(line)

    aux = [0] * len(line)
    for i in range(len(line)):
        if line[i] == month:
            aux[i] = 1

    # print(line)
    for j in range(len(line)):
        if line[j].endswith(","):
            line[j] = line[j].split(",")[0]
        if line[j].endswith("."):
            line[j] = line[j].split(".")[0]
        if line[j].isnumeric():
            if month in months_31:
                if 0 < int(line[j]) < 32:
                    numbers_in_line[j] = line[j]
            if month in months_30:
                if 0 < int(line[j]) < 31:
                    numbers_in_line[j] = line[j]
            if month == 2:
                if 0 < int(line[j]) < 29:
                    numbers_in_line[j] = line[j]

    # print(numbers_in_line)
    # print(aux.index(1))

    distance_from_month = [10000000] * len(line)
    for k in range(len(numbers_in_line)):
        if numbers_in_line[k] != 0:
            distance_from_month[k] = abs(k - aux.index(1))

    # print(distance_from_month)
    closest_distance = min(distance_from_month)
    index_of_closest_number = distance_from_month.index(closest_distance)

    closest_valid_date = numbers_in_line[index_of_closest_number]
    # print(closest_valid_date)

    return closest_valid_date

def extract_month(line):
    names_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = []
    # print(line)
    flag = 0
    for words in line:
        if words in names_of_months:
            flag += 1
            month.append(words)
    if flag == 1:
        # print(month[0], flag)
        valid_day = find_closest_valid_number(line, month[0])
        return month[0], valid_day

def solution(text_lines):
    for line in text_lines:
        # extract_DM_date(line)
        print(extract_month(line))
        # print(line)




if __name__ == '__main__':

    no_of_lines = input()

    no_of_lines = int(no_of_lines)

    text_lines = [[] for i in range(no_of_lines)]

    # print(text_lines)



    for i in range(0, no_of_lines):
        text_lines[i] = input().split()

    solution(text_lines)

