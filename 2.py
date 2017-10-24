 
#1. Introduction to Python: Files, List and Dictionary - Write a python program to read contents of a file (filename as 
#argument) and store number of occurrences of each word in a dictionary. Display the top 10 words with most number of 
#occurrences in descending order. Store the length of each of these words in a list and display the list. Write a one-line 
#reduce function to get the average length and one-line list comprehension to display squares of all odd numbers and 
#display both. 
 
import sys 
import os 
import functools 
 
if(len(sys.argv) != 2): 
    print ("Invalid Arguments\n") 
    sys.exit() 
 
if(not(os.path.exists(sys.argv[0]))): 
    print ("Invalid File Path\n") 
    sys.exit() 
 
if(sys.argv[1].split('.')[-1] != "txt"): 
    print ("Invalid File Format. Only TXT files allowed\n") 
    sys.exit() 
 
escape = open(sys.argv[1]) 
worddic = { } 
for line in escape:   
        myline = line.split() 
         
        for word in myline: 
                w = worddic.get(word,0) 
                #print ("key word %s exists in doctionary with %d value" %(word, w)) 
                worddic[word] = w + 1  
print (worddic ,"\n ") 
 
sortedlist = [ ] 
sortedlist = sorted(worddic.items(),reverse=True) #NOTE - sorted returns a list not dictionary 
print("\n\n") 
print ("Sorting in Descending order of Key Value - here words (Z words first...)", sortedlist) 
 
def key_value(x): 
    return x[1] 
     
sortedlist = sorted(worddic.items(), key = key_value, reverse = True) 
print("\n\n") 
print ("After LAMBDA --- Sorting in Dscending order of Value Occurance - frequency of word occurance ", sortedlist) 
    
topten = [] 
for i in range(10):   
    try: 
        wordTuple = sortedlist[i] 
        topten.append(len(wordTuple[0])) 
        print("\n\n") 
        print (wordTuple[0], " Frequency: " , wordTuple[1] , " Length " , len(wordTuple[0])) 
    except IndexError: 
        print ("\n\n File has less than 10 words") 
        break 
 
print ("\n\n\n Lengths of 10 most frequently occuring words:") 
print (topten) 
 
mysum = functools.reduce(lambda x, y: x + y, topten)   #one-line reduce fuction to get average length of top 10 words 
print ("\n\n Average length of Top Ten words: " , mysum/len(topten)) 
 
squares = [x**2 for x in topten if x%2 != 0]     #one-line list comprehension to display squares of all odd numbers 
print ("\n\n Squres of odd word lengths: ") 
print (squares) 

