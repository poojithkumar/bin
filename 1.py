#1. Introduction to Python: Functions and I/O - Write a temperature converter python program, which is menu driven.
#Each such conversion logic should be defined in separate functions. The program should call the respective function
#based on the users requirement. The program should run as long as the user wishes so. Provide an option to view the last
#5 conversions stored as list of tuples with attributes - from unit, value, to unit, value, date and time of conversion, sorted
#by the users choice (from-value, to-value or date/time).
 
import datetime
import time
from datetime import datetime
from operator import itemgetter
 
record = tuple()
details = tuple()
records = tuple()
l= []
pos = 0
posi=0
 
records = list(records)
 
def c_to_k(records):
    print("Enter your temperature in celsius")
    temp = float(input(">>> "))
    converted = temp + 273.15
    dt = date_time()
    print("Converted value in kelvin= ",converted) 
    details = ('Celsius',temp,'Kelvin',converted,str(dt))
    tuple_insert(records,details)
 
def c_to_f():
    print("Enter your temperature in celsius")
    temp = float(input(">>> "))
    dt = date_time()
    converted = (1.8 * temp) + 32
    print("Converted value in fahrenheit = ",converted) 
    details = ('Celsius',temp,'Fahrenheit',converted,str(dt))
    tuple_insert(records,details)      
 
def f_to_c():
    print("Enter your temperature in fahrenheit")
    temp = float(input(">>> "))
    dt = date_time()
    converted = (temp-32)/1.8
    print("Converted value in celsius = ",converted)    
    details = ('Fahrenheit',temp,'Celsius',converted,str(dt))
    tuple_insert(records,details)
 
def k_to_c():
    print("Enter your temperature in kelvin")
    temp = float(input(">>> "))
    dt = date_time()
    converted = temp - 273.15
    print("Converted value in celsius = ",converted)     
    details = ('Kelvin',temp,'Celsius',converted,str(dt))
    tuple_insert(records,details)
 
def tuple_insert(records,details):
    records.append(details)
    tuple(records)
    return records
 
def date_time():
    value = datetime.now()
    return value
 
def view_conversions():
    print("\nHow do you want to sort your conversions??\n--------\n1.from-value\n2.to-value\n3.date-time\n")
    print("Enter your choice")
    sort_choice = input(">>> ")
    print("------THE CONVERSIONS YOU PERFORMED ARE-------")
    
    if(sort_choice == '1'):
        record=sorted(records, key=itemgetter(1))
        print(record)
    elif(sort_choice == '2'):
        record=sorted(records, key=itemgetter(3))
        print(record)
    elif(sort_choice == '3'):
        record=sorted(records, key=itemgetter(4))
        print(record)
        
        
while(True):
    print("\nMenu\n-------\n1.Celsius to Kelvin\n2.Celsius to Fahrenheit\n3.Fahrenheit to celsius\n4.Kelvin to Celsius\n5.View last 5 conversions\n")
    print("Enter your choice")
    choice=input(">>> ")
    print("choice=",choice)
    
    if(choice == '1'):
        c_to_k(records)
    elif(choice == '2'):
        c_to_f()
    elif(choice == '3'):
        f_to_c()
    elif(choice == '4'):
        k_to_c()
    elif(choice == '5'):
        view_conversions() 
    else:
        print("invalid choice")
        
    print("Do you want to continue? Y/N")
    s = input(">>> ")
    select = s.lower()
    if(select == 'n'):
        print("You exited")
        break


