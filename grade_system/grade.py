# IMPORTING REQUIRED LIBRARIES 
import pandas as pd 
import csv
from os import system
import numpy
# TAKING NUMBER OF EXECUTION TIME 
no_of_ex = int(input("Enter no of data you want to enter: "))
data = {}
count = 0
# CHECKING WHETHER INPUTED NO IS VALID OR NOT 
if count == no_of_ex:
    print("Error! Please enter valid no.")
else:
    while (no_of_ex != count):
        name = input("Enter name: ")
        dep = input("Enter depertment name: ")
        roll = int(input("Enter college roll no: "))
        sex = input("Enter sex: ")
        marks = int(input("Enter marks: "))
        # DECISION OF MAKING GRADE SYSTEM 
        if (marks>=90) and (marks<=100):
            grade = "O"
        elif (marks>=80) and (marks<=89):
            grade = "E"
        elif (marks>=70) and (marks<=79):
            grade = "G"
        elif (marks>=60) and (marks<=69):
            grade = "P"
        elif (marks<60):
            grade = "Fail"
        # MAKING DATA TABLE 
        df = pd.DataFrame(
            {
                "Name": [name],
                "Depertment": [dep],
                "Roll No": [roll],
                "Sex":[sex],
                "Marks":[marks],
                "Grade":[grade]
            }
        )  
        # CONVERTING DATE TABLE TO CSV FILE 
        df.to_csv("score.csv",mode="a")
        count = count+1         
# Reading the csv file
df_new = pd.read_csv('score.csv') 
# saving xlsx file
GFG = pd.ExcelWriter('score.xlsx')
df_new.to_excel(GFG, index=False)
GFG.save()       
