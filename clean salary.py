import csv

with open("Clean_Salary_Data_with_Numbers.csv","r") as csvIn, open("clean salary.csv","w+",newline="") as csvOut:
    ls = []
    reader = csv.reader(csvIn)
    header = ["timestamp","company","title","totalyearlycompensation","location","yearsofexperience",
              "yearsatcompany","basesalary","stockgrantvalue","bonus","cityid","dmaid","rowNumber","Masters_Degree",
              "Bachelors_Degree","Doctorate_Degree","Highschool","Some_College","Race_Asian","Race_White","Race_Two_Or_More",
              "Race_Black","Race_Hispanic"]
    ls2 = []
    first = True
    for row in reader:
        if first:
            # append headers to cleaned csv file
            ls.append(header)
            first = False
            continue
        else:
            timestamp = row[0]
            company = row[1]
            title = row[3]
            totalyearlycompensation = row[4]
            location = row[5]
            yearsofexperience = row[6]
            yearsatcompany = row[7]
            basesalary = row[9]
            stockgrantvalue = row[10]
            bonus = row[11]
            cityid = row[14]
            dmaid = row[15]
            rowNumber = row[16]
            Masters_Degree = row[17]
            Bachelors_Degree = row[18]
            Doctorate_Degree = row[19]
            Highschool = row[20]
            Some_College = row[21]
            Race_Asian = row[22]
            Race_White = row[23]
            Race_Two_Or_More = row[24]
            Race_Black = row[25]
            Race_Hispanic = row[26]

            
            if timestamp == "NA":
                timestamp = 0
            if company == "NA":
                company = 0
            if title == "NA":
                title = 0
            if totalyearlycompensation == "NA":
                totalyearlycompensation = 0
            if location == "NA":
                location = 0
            if yearsofexperience == "NA":
                yearsofexperience = 0
            if basesalary == "NA":
                basesalary = 0
            if stockgrantvalue == "NA":
                stockgrantvalue = 0
            if bonus == "NA":
                bonus = 0
            if cityid == "NA":
                cityid = 0
            if dmaid == "NA":
                dmaid = 0
            if rowNumber == "NA":
                rowNumber = 0
            if Masters_Degree == "NA":
                Masters_Degree = 0
            if Bachelors_Degree == "NA":
                Bachelors_Degree = 0
            if Doctorate_Degree == "NA":
                Doctorate_Degree = 0
            if Highschool == "NA":
                Highschool = 0
            if Some_College == "NA":
                Some_College = 0
            if Race_Asian == "NA":
                Race_Asian = 0
            if Race_White == "NA":
                Race_White = 0
            if Race_Two_Or_More == "NA":
                Race_Two_Or_More = 0
            if Race_Black == "NA":
                Race_Black = 0
            if Race_Hispanic == "NA":
                Race_Hispanic = 0

            if float(basesalary) > 140000:
                basesalary = 1
            else:
                basesalary = 0

            ls2 =[timestamp,company,title,totalyearlycompensation,location,yearsofexperience,yearsatcompany,basesalary,
                  stockgrantvalue,bonus,cityid,dmaid,rowNumber,Masters_Degree,Bachelors_Degree,Doctorate_Degree,Highschool,
                  Some_College,Race_Asian,Race_White,Race_Two_Or_More,Race_Black,Race_Hispanic]
        
        ls.append(ls2)


    writer = csv.writer(csvOut)
    writer.writerows(ls)

