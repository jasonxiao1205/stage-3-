# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
import pandas as pd
import sklearn
from math import sqrt
from sklearn import metrics
from sklearn import linear_model
from sklearn.model_selection import train_test_split

with open("Levels_Fyi_Salary_Clean_Data.csv", "r", encoding='utf-8') as csvIn:
    company_dictionary = {}
    title_dictionary = {}
    location_dictionary = {}
    year_dictionary = {}
    
    reader = csv.reader(csvIn)
    first = True
    for row in reader:
        if first:
            first = False
            continue

        company = row[1]
        title = row[3]
        location = row[5]
        year = row[7]
        # change date to year only
        row[0] = row[0].split(" ")[0].split("/")[2]
        # changing company,title,location to unique numeric identifiers.
        if company not in company_dictionary:
            company_dictionary[company] = len(company_dictionary) + 1
        -re
        if title not in title_dictionary:
            title_dictionary[title] = len(title_dictionary) + 1
        
        if location not in location_dictionary:
            location_dictionary[location] = len(location_dictionary) + 1

        row[1] = company_dictionary[company]
        row[3] = title_dictionary[title]
        row[5] = location_dictionary[location]
        #row[7] = year_dictionary[year]
        
# the dictionaries have key being company/title/location and value being a number. Changing the order to get number as key
    company_dictionary = {value:key for key, value in company_dictionary.items()}
    title_dictionary = {value:key for key, value in title_dictionary.items()}
    location_dictionary = {value:key for key, value in location_dictionary.items()}
    year_dictionary = {value:key for key, value in year_dictionary.items()}


df = pd.read_csv("Clean_Salary_Data_with_Numbers.csv")
x = df[['yearsofexperience', 'yearsatcompany']] # slice dataFrame for input variables
y = df['basesalary']        # slice dataFrame for target variable
x_train, x_test, y_train, y_test = train_test_split(x.values, y.values, test_size=0.2, random_state=10)
regr = linear_model.LinearRegression().fit(x_train, y_train)

# Let's create one sample
#
sample = [7, 2] 
sample_pred = regr.predict([sample])
print('----- Sample case -----')
print("Years of experience:", sample[0])
print("Year at company:", sample[1])
print('Predicted base salary:', int(sample_pred))
print('-----------------------')

# Use the model to predict X_test
y_pred = regr.predict(x_test)
# Root mean squared error
mse = metrics.mean_squared_error(y_test, y_pred)
print('Root mean squared error (RMSE):', sqrt(mse))
# R-squared score: 1 is perfect prediction
print('R-squared score:', metrics.r2_score(y_test, y_pred))