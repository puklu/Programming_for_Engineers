# Author: Vivek Punia

# Programming for engineers homework 3 this program extracts dates from text.
# The date is extracted from the sentence
# as follows: In case 1. above, the date is the DM-date. In case 2. above, the integer which is the closest one to
# the month name is interpreted as the day. I case there are two integers in the same minimum distance from the month
# name the first one of them is interpreted as the day.
# The examples of DM-dates are: 1.1.  31.1.


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


# function to extract date from DM_date format. DM_date format = 12.1.
def extract_DM_date(line):
    # print(line)
    date = []
    flag = 0
    names_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December"]
    for word in line:
        # getting rid of a comma it is present after a word
        if word.endswith(","):
            word = word.split(",")[0]

        # if the word ends with a period, it is a candidate of DM_date format
        if word.endswith("."):
            possible_date = word.split(".")
            # print(possible_date)
            if len(possible_date) == 3:
                # print(check_if_valid_date(possible_date))
                if check_if_valid_date(possible_date):
                    date.append(word)
                    flag += 1
    if flag == 1:    # flag to maintain that such date appears only once in the line, otherwise line not considered
        date = date[0].split(".")
        month = names_of_months[int(date[1]) - 1]
        day = int(date[0])
        return month, day


# function to find the closest number to the month name that can be considered as date
def find_closest_valid_number(line, month):
    months_31 = ["January", "March", "May", "July", "August", "October", "December"]
    months_30 = ["April", "June", "September", "November"]

    numbers_in_line = [0] * len(line)    # variable to hold the numbers present in the line

    aux = [0] * len(line)                # variable to maintain the index of the month in the line
    for i in range(len(line)):
        # getting rid of a comma or period at the end of a word if it is there
        if line[i].endswith(","):
            line[i] = line[i].split(",")[0]
        if line[i].endswith("."):
            line[i] = line[i].split(".")[0]

        # updating aux to 1 corresponding the position of month name in the line
        if line[i] == month:
            aux[i] = 1

    # checking the number in the line is valid for the month
    for j in range(len(line)):
        # getting rid of a comma or period at the end of a word if it is there
        if line[j].endswith(","):
            line[j] = line[j].split(",")[0]
        if line[j].endswith("."):
            line[j] = line[j].split(".")[0]

        if line[j].isnumeric():                      # only if the word is numeric
            if month in months_31:                   # if the month is one of 31-days month
                if 0 < int(line[j]) < 32:            # then the number should be between 0 and 32
                    numbers_in_line[j] = line[j]
            if month in months_30:                   # if the month is one of 30-days month
                if 0 < int(line[j]) < 31:            # then the number should be between 0 and 32
                    numbers_in_line[j] = line[j]
            if month == 'February':                  # if the month is february
                if 0 < int(line[j]) < 29:            # then the days should be between 0 and 29
                    numbers_in_line[j] = line[j]

    # print(numbers_in_line)
    # print(aux.index(1))

    # array to hold the distance of the numbers from the month name in the line
    # 10000000 given as a default, a very large distance
    distance_from_month = [10000000] * len(line)
    for k in range(len(numbers_in_line)):
        if numbers_in_line[k] != 0:
            distance_from_month[k] = abs(k - aux.index(1))   # calculating the absolute distance between indices of the numbers and month name

    # print(distance_from_month)
    closest_distance = min(distance_from_month)              # finding the minimum distance
    index_of_closest_number = distance_from_month.index(closest_distance)   # index of the minimum distance

    closest_valid_date = numbers_in_line[index_of_closest_number]   # finally getting the number which can be considered as a valid date
    # print(closest_valid_date)

    return closest_valid_date


# function to extract the date if the month is written in word, like "June"
def extract_month(line):
    names_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                       "November", "December"]

    # to hold the names of months mentioned in the text line
    month = []
    # flag to count if more than one month has appeared in the text line
    flag = 0
    # checking all the words in the line
    for words in line:
        # if the word has a comma or period at its end, remove it
        if words.endswith(","):
            words = words.split(",")[0]
        if words.endswith("."):
            words = words.split(".")[0]

        # if the word resembles the name of a month
        if words in names_of_months:
            flag += 1            # counting the names of months
            month.append(words)  # adding the month names to month variable
    if flag == 1:                # we return only if only one month name has appeared in the line
        # finding the number closest to the month name in the line
        valid_day = find_closest_valid_number(line, month[0])
        # print(valid_day)
        if int(valid_day) > 0:
            return month[0], valid_day


def solution(text_lines):
    for i in range(len(text_lines)):
        # if the line has both DM_date and month format dates, then line is ignored
        if extract_DM_date(text_lines[i]) and extract_month(text_lines[i]):
            # print("here from both")
            continue

        # extract date if it is format DM_date
        if extract_DM_date(text_lines[i]):
            # print("just date")
            month = extract_DM_date(text_lines[i])[0]
            date = extract_DM_date(text_lines[i])[1]
            print(str(i + 1) + ".", month, date)

        # extract date if the month is written in word, like "June"
        if extract_month(text_lines[i]):
            # print("just month")
            month = extract_month(text_lines[i])[0]
            date = extract_month(text_lines[i])[1]
            print(str(i + 1) + ".", month, date)


if __name__ == '__main__':

    # gets the number of lines in the text
    no_of_lines = input()

    # converting to int
    no_of_lines = int(no_of_lines)

    # a list of lists to hold the text lines
    texts = [[] for i in range(no_of_lines)]

    # splitting the line into words
    for i in range(0, no_of_lines):
        texts[i] = input().split()

    # calling the solution method
    solution(texts)
