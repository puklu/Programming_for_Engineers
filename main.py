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


def calculate_duration_between_two_dates(n, dates):
    days_in_each_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # print(dates)
    answer = {}

    if len(dates) == 1:
        answer[int(dates[0].split(".")[1])] = [n+1, 1, dates[0], dates[0]]
        return answer
        # return [n+1, 1, dates[0]]
    else:
        months = {}
        for i in range(len(dates)):
            # print(dates[i])
            if dates[i].split(".")[1] in months.keys():
                months[dates[i].split(".")[1]].append(dates[i].split(".")[0])
            else:
                months[dates[i].split(".")[1]] = [dates[i].split(".")[0]]

        # sort values of each key of months
        for month in months.keys():
            months.get(month).sort()

        # sort the dictionary by keys
        # print(months)
        first_month = min(map(int, list((months.keys()))))
        last_month = max(map(int, list((months.keys()))))

        if first_month == last_month:
            first_day = min(int(months[str(first_month)][0]), int(months[str(last_month)][len(months[str(last_month)])-1]))
            last_day = max(int(months[str(first_month)][0]), int(months[str(last_month)][len(months[str(last_month)]) - 1]))
        else:
            first_day = months[str(first_month)][0]
            last_day = months[str(last_month)][len(months[str(last_month)])-1]

        # print("first day= " + months[str(first_month)][0])
        # print("last day= " + months[str(last_month)][len(months[str(last_month)]) - 1])

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
        start_date = str(first_day)+"."+str(first_month)+"."
        end_date = str(last_day)+"."+str(last_month)+"."

        answer[int(start_date.split(".")[1])] = [n + 1, duration, start_date, end_date]
        # print("answer")
        # print(answer)
        return answer
        # return [n+1, duration, start_date, end_date]


def solution(text_lines):
    # print(text_lines)
    possible_dates_collector = {}

    for i in range(len(text_lines)):
        dates_in_line = extract_DM_date(text_lines[i])
        # print("::::::::::")
        # print(dates_in_line)
        if dates_in_line:
            expedition_dates_with_duration = calculate_duration_between_two_dates(i, dates_in_line)
            # split_day = (expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])[2])[0:2]
            split_day = (expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])[2])
            split_day = split_day.split(".")[0]
            if len(split_day) == 1:
                split_day = str(0)+split_day
            # print((split_day))
            # print("..//..")
            # print((expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])[2])[0:2])
            if list(expedition_dates_with_duration.keys())[0] in list(possible_dates_collector.keys()):

                possible_dates_collector[float(str(list(expedition_dates_with_duration.keys())[0])+ "." + split_day)] = [expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])[0]]
                possible_dates_collector[float(str(list(expedition_dates_with_duration.keys())[0]) + "."+ split_day)].append(expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])[1])
                possible_dates_collector[float(str(list(expedition_dates_with_duration.keys())[0]) + "."+ split_day)].append(expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])[2])
                possible_dates_collector[float(str(list(expedition_dates_with_duration.keys())[0]) + "."+ split_day)].append(expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])[3])

            else:
                # print("....")
                # print(float(str(list(expedition_dates_with_duration.keys())[0]) + "." + split_day))
                possible_dates_collector[float(str(list(expedition_dates_with_duration.keys())[0]) + "." + split_day)] = expedition_dates_with_duration.get(list(expedition_dates_with_duration.keys())[0])
                # possible_dates_collector.update(expedition_dates_with_duration)

    # print(expedition_dates_with_duration)
    # print(possible_dates_collector)
    sorteddict = sorted(possible_dates_collector)
    # print(sorteddict)
    # print("....")

    ### making pairs ###
    # sorting for pairing
    sorted_for_pairing = []
    # print(sorted_for_pairing)
    for i in range(len(sorteddict)):
        sorted_for_pairing.append(possible_dates_collector.get(sorteddict[i]))
    print(sorted_for_pairing)
    # print(len(sorted_for_pairing))

    # convert to dictionary for making it sortable
    pairs_dict = {}
    for j in range(len(sorted_for_pairing)):
        key1 = sorted_for_pairing[j][2].split(".")[1]
        key2 = sorted_for_pairing[j][2].split(".")[0]
        key = key1 + "." + key2
        # print(".....")
        # print(sorted_for_pairing[j])

        pairs_dict[key] = sorted_for_pairing[j]

    print(pairs_dict)

    h = 0
    while h < len(pairs_dict)-1:
        # print(pairs_dict.get(list(pairs_dict.keys())[h]))

        now_date = (pairs_dict.get(list(pairs_dict.keys())[h])[3])
        now_date = now_date.split(".")
        if len(now_date[0]) == 1:
            now_date = float(now_date[1] + "." + str(0) + now_date[0])
        else:
            now_date = float(now_date[1] + "." + now_date[0])

        next_date = (pairs_dict.get(list(pairs_dict.keys())[h+1])[2])
        next_date = next_date.split(".")
        if len(next_date[0]) == 1:
            next_date = float(next_date[1] + "." + str(0) + next_date[0])
        else:
            next_date = float(next_date[1] + "." + next_date[0])

        # print(now_date)
        # print(next_date)
        if next_date < now_date:
            del pairs_dict[list(pairs_dict.keys())[h+1]]
        else:
            h += 1

    print(pairs_dict)


    #pairing
    pairs = [[] for i in range(len(pairs_dict)-1)]
    # pairs = {}

    now_date = (pairs_dict.get(list(pairs_dict.keys())[0])[3])
    now_date = now_date.split(".")
    if len(now_date[0]) == 1:
        now_date = float(now_date[1] + "." + str(0) + now_date[0])
    else:
        now_date = float(now_date[1] + "." + now_date[0])

    next_date = (pairs_dict.get(list(pairs_dict.keys())[1])[2])
    next_date = next_date.split(".")
    if len(next_date[0]) == 1:
        next_date = float(next_date[1] + "." + str(0) + next_date[0])
    else:
        next_date = float(next_date[1] + "." + next_date[0])

    # pairs[0].append(pairs_dict.get(list(pairs_dict.keys())[0]))
    for k in range(len(pairs_dict)-1):
        dates = [pairs_dict.get(list(pairs_dict.keys())[k])[3], pairs_dict.get(list(pairs_dict.keys())[k+1])[2]]
        # print("....")
        # print(dates)
        dur = calculate_duration_between_two_dates(0, dates)
        dur = dur.get(list(dur.keys())[0])[1]
        # print(dur)

        # now_date = (pairs_dict.get(list(pairs_dict.keys())[k])[3])
        # now_date = now_date.split(".")
        # now_date = float(now_date[1] + "." + now_date[0])
        # next_date = (pairs_dict.get(list(pairs_dict.keys())[k+1])[2])
        # next_date = next_date.split(".")
        # next_date = float(next_date[1] + "." + next_date[0])

        # print(now_date)
        # print(next_date)
        # print("......")



        if dur > 7: #and next_date>now_date:
            # print("testing...")
            # print(pairs)
            pairs[k].append(pairs_dict.get(list(pairs_dict.keys())[k]))
            pairs[k].append(pairs_dict.get(list(pairs_dict.keys())[k+1]))

        #     now_date = int(pairs[k][0][3].split(".")[1])
        #     print("//////////")
        #     print(now_date)
        #     now_date = (pairs_dict.get(list(pairs_dict.keys())[k])[3])
        #     now_date = now_date.split(".")
        #     now_date = float(now_date[1] + "." + now_date[0])
        # next_date = (pairs_dict.get(list(pairs_dict.keys())[k+1])[2])
        # next_date = next_date.split(".")
        # next_date = float(next_date[1] + "." + next_date[0])
        print(pairs)




    for m in range(len(pairs)):
        if [] in pairs:
            pairs.remove([])

    # print(pairs)

    expedition_duration = pairs[0][0][1]+pairs[0][1][1]
    print(expedition_duration)
    for l in range(len(pairs)):
        print(pairs[l][0][0], end=" ")
        print(pairs[l][0][2], end=" ")
        print(pairs[l][0][3], end=" ")
        print(pairs[l][1][0], end=" ")
        print(pairs[l][1][2], end=" ")
        print(pairs[l][1][3])


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
