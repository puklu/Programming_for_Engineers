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
    # print(line)
    date = []

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

    # print(date)
    return date


def calculate_duration_between_two_dates(dates):
    days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # print(dates)
    if len(dates) == 1:
        return 1
    else:
        months = {}
        for i in range(len(dates)):
            if dates[i].split(".")[1] in months.keys():
                months[dates[i].split(".")[1]].append(dates[i].split(".")[0])
            else:
                months[dates[i].split(".")[1]] = [dates[i].split(".")[0]]

        # sort values of each key of months
        for month in months.keys():
            months.get(month).sort()

        # sort the dictionary by keys

        first_month = min(months.keys())
        first_day = months[first_month][0]
        last_month = max(months.keys())
        last_day = months[last_month][len(months[last_month])-1]

        if first_month == last_month:
            duration = int(last_day) - int(first_day) + 1
            # print(duration)
        else:
            days_in_between = 0
            if int(first_month) in [1, 3, 5, 7, 8, 10, 12]:
                days_in_first_month = 31 - int(first_day) + 1
                days_in_last_month = int(last_day)

            else:
                days_in_first_month = 30 - int(first_day) + 1
                days_in_last_month = int(last_day)

            for k in range(int(first_month), int(last_month)-1):
                # print(k)
                days_in_between += days_in_each_month[k]
                # print(days_in_between)

            duration = days_in_first_month + days_in_last_month + days_in_between
        # print(duration)
        return duration


def solution(text_lines):
    print(text_lines)
    for i in range(len(text_lines)):
        dates_in_line = extract_DM_date(text_lines[i])
        duration = calculate_duration_between_two_dates(dates_in_line)
        # print(dates_in_line)


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
