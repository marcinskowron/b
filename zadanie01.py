with open('rows.txt', 'r') as f:
    check_sum = 0
    for row in f:
        temp_list = []
        for value in row.split():
            temp_list.append(int(value))
        check_sum += max(temp_list) - min(temp_list)
    print(check_sum)
