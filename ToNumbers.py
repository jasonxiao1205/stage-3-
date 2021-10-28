import csv

with open("Levels_Fyi_Salary_Clean_Data.csv", "r", encoding='utf-8') as csvIn, open("Clean_Salary_Data_with_Numbers.csv", "w", newline="", encoding='utf-8') as csvOut:
    ls = []
    company_dictionary = {}
    title_dictionary = {}
    location_dictionary = {}
    
    reader = csv.reader(csvIn)
    first = True
    for row in reader:
        if first:
            ls.append(row)
            first = False
            continue

        company = row[1]
        title = row[3]
        location = row[5]

        # change date to year only
        row[0] = row[0].split(" ")[0].split("/")[2]

        if company not in company_dictionary:
            company_dictionary[company] = len(company_dictionary) + 1
        
        if title not in title_dictionary:
            title_dictionary[title] = len(title_dictionary) + 1
        
        if location not in location_dictionary:
            location_dictionary[location] = len(location_dictionary) + 1

        row[1] = company_dictionary[company]
        row[3] = title_dictionary[title]
        row[5] = location_dictionary[location]

        ls.append(row)

    writer = csv.writer(csvOut)
    writer.writerows(ls)

    company_dictionary = {value:key for key, value in company_dictionary.items()}
    title_dictionary = {value:key for key, value in title_dictionary.items()}
    location_dictionary = {value:key for key, value in location_dictionary.items()}

    print(company_dictionary)
    print(title_dictionary)
    print(location_dictionary)