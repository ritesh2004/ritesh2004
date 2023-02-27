'''
This is a Cashier Machine that makes a instant Bill
@Author : Ritesh Pramanik
'''
#from fileinput import filename
from os import system, write
import pandas as pd 
import csv
import time
def ProductList():
    f = pd.read_excel("ProductList.xlsx")
    print(f)

class Details:
    def UserDetails(self):
        system("cls")
        print("\n\t\tPlease pass customer details carefully.")
        print("\n\t\tGetting the customer's details...")
        name = input("\nCustomer name:")
        CusId = input("\nCustomer ID:")
        CusAdd = input("\nCustomer address:")
        mobileNo = input("\nCustomer Mobile No:")
        emailId = input("\nCustomer Email Id:")
        curr_date_time = time.strftime("%Y-%m-%d-%H-%M-%S")
        filename = name + mobileNo + curr_date_time + ".csv"
        return filename,name,CusId,CusAdd,mobileNo

def BuyingData(filename,name,CusId,CusAdd,mobileNo):
    system("cls")
    print("\n\tPlease Select the option carefully.")
    dict1 = []
    total = 0
    buying = True
    while buying:
        AskProductList = input("See Product List [y/n]: ")
        if AskProductList == "y":
            print("\n\t\tHere is the product list given below...")
            ProductList()
        elif AskProductList == "n":
            pass
        else:
            print("\nPlease enter the correct keyword.")
            break
        print("Please give attention to the spelling of the products while entering the products' names...")
        product = input("\n\t\tEnter the products name you want to buy:")
        quantity = int(input("\n\t\tEnter the quantity:"))   
        price = 0     
        file = open("ProductList.csv","r",newline="\n")
        r = csv.reader(file)        
        for rec in r:
            if rec[0]==product:
                price = rec[3]
                price = int(price)
                print("Price",price)
        subTotal = price*quantity
        if product in ("Apples","Oranges",
"Bananas",
"Lettuce",
"Tomatoes",
"Cheese",
"Cottage cheese",
"Poultry",
"Ham"):
            quantity = str(quantity)
            quantity = quantity + "K.G."
        elif product == [
"Milk", 
"Juice",
"Water"
]:
            quantity = str(quantity)
            quantity = quantity + "L"
        elif product in ["Coffee","Tea"]:
            quantity = str(quantity)
            quantity = quantity + "Cup"
        elif product in [
"Noodles",
"Rice",
"Bread",
"Potato chips",
"Pretzels",
"Ice cream",
"Cookies",
"Paper plates","Napkins","Canned","Dry Mix"
]:
            quantity = str(quantity)
            quantity = quantity + "Pkt"
        elif product in "Egg":
            quantity = str(quantity)
            quantity = quantity + "Piece"
        '''file1 = open("Grocery Bill.csv","r",newline="\n")
        reader = csv.reader(file1)
        found = 0
        BuyingData = []
        for rec in reader:
            if rec[1] == product:
                rec[3] = quantity
                rec[4] = price
                found = 1
            BuyingData.append(rec)
        if found == 1:
            file1 = open("Grocery Bill.csv","w",newline="\n")
            writer = csv.writer(file1)
            writer.writerows(BuyingData)
            file1.close()'''
        buyMore = input("Buy more[y/n]:")
        if buyMore == "y":
            buying = True
        elif buyMore == "n":
            buying = False
        else:
            print("\nPlease enter the valid keyword.")
            break
        total = int(total)
        subTotal = int(subTotal)
        total += subTotal
        field = ["Item","Quantity","Price/unit","Subtotal"]
        date = time.strftime("%d-%m-%Y")
        curr_time = time.strftime("%H:%M:%S")
        mobileNo = str(mobileNo)
        price = str(price)
        Price = price + "/-"
        subTotal = str(subTotal)
        subtotal = subTotal + "/-"
        row = [product,quantity,Price,subtotal]
        details = [["WELCOME TO COMPANY"],
                   ["COMPANY ADDRESS","","","","Email Id:","someone@example.com"],
                   ["","","","","Phone No:","(413)-555-1019"],
                   ["Date:",date,"","Time:",curr_time],
                   ["Name", name,"","Address",CusAdd],
                   ["Cus ID",CusId,"","Mobile No",mobileNo]]
        dict1.append(row)  
        print(dict1) 
        with open(filename,"w") as f:
            writer = csv.writer(f)
            writer.writerows(details)
            writer.writerow(field)
            writer.writerows(dict1)
            total = str(total)
            writer.writerow(["TOTAL",total+"/-"])
            total = int(total)
            writer.writerow(["Please give us feedback on someone@example.com about our service"])
            writer.writerow(["THANKS FOR SHOPPING WITH US"])
def MAINMENU():
    userdetails = Details()
    f = userdetails.UserDetails()
    BuyingData(f[0],f[1],f[2],f[3],f[4])
    print("Bill generated")
    print("Please collect your bill recipt")

MAINMENU()        
    
    
