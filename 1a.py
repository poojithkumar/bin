
def remove_duplicates(numbers):
    n= []
    for number in numbers:
       if number not in n:
           n.append(number)
    return n
c=remove_duplicates([1,2,3,4,5,5,5,6,3,2])
print "newlist:",c

