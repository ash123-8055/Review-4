import re
import pandas as pd


def detail_valid(fname,lname,age,phone_number):
    """
    Description: Validates the firstname, last name, age, phone_number of the user..
    
    parameter: fname: first name of the user
               lname: last name of the user
               age: age of the user
               phone_number: phone number of the user
    
    return: Checks and returns True or False
    """
    
    fname_pattern=r"[a-zA-Z]{3,}"
    lname_pattern=r"[a-zA-Z]{3,}"
    age_pattern=r"^\d{2}$"
    phone_pattern=r"^\d{10}$"
    if bool(re.findall(fname_pattern,fname))==True and bool(re.findall(lname_pattern,lname))==True and bool(re.findall(age_pattern,age))==True and bool(re.findall(phone_pattern,phone_number))==True:
        return True
        
    else:
        return False

fname=input("Enter the first name: ")
lname=input("Enter the last name: ")
age=input("Enter the age: ")
phone_number=input("Enter the Phone Number: ")
if detail_valid(fname,lname,age,phone_number)==True:
    data={
        "first_name":[fname],
        "last_name":[lname],
        "age":[age],
        "phone_number":[phone_number]
    }
    df=pd.DataFrame(data)
    df["phone_number"]=df["phone_number"].str[:3]+"xxxxxxx"
    print(df)

else:
    print("Details are not valid")