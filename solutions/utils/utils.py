def load_data_for_day(day):
    file_name = '../data/day' + str(day) + '.txt'

    data = list([])

    with open(file_name, 'r') as data_file:
        for line in data_file:
            data.append(line.strip())

    return data
