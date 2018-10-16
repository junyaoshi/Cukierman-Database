import csv
import itertools as it


def read_file(file_name):
    try:
        l = []
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                l.append(row)
        return l
    except IOError as e:
        print(e)


def deduplicate(file_name):

    # read file
    data = read_file(file_name)

    for i in range(1, len(data)):
        new_row = []

        person = data[i][0]
        company = data[i][6]
        position = data[i][8]
        phone = data[i][10]
        email = data[i][13]

        new_row.extend([person, company, position, phone, email])

        for j in it.chain(range(1, i), range(i+1, len(data))):

            db_row = []

            db_person = data[j][0]
            db_company = data[j][6]
            db_position = data[j][8]
            db_phone = data[j][10]
            db_email = data[j][13]

            db_row.extend([db_person, db_company, db_position, db_phone, db_email])

            # find intersection
            intersection = list(set(new_row) & set(db_row))
            if len(intersection) == 0:
                continue
            elif len(intersection) == 1 and (intersection[0] == company or intersection[0] == position or intersection[0] == '') :
                continue
            elif len(intersection) == 5:
                data[i][1] = 5
            elif len(intersection) == 4:
                data[i][1] = 4
            elif len(intersection) == 3:
                data[i][1] = 3
            elif len(intersection) == 2:
                data[i][1] = 2
            else:
                data[i][1] = 1
            print(str(person) + ': ' + str(intersection))
            data[i][2] = str(intersection)
            break

    try:
        with open(file_name + '_Deduped' + '.csv', 'w+', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
    except IOError as e:
        print(e)


