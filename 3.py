 #3. Introduction to Python : Classes & Objects, Functions 
#a) Write a python class to reverse a sentence (initialized via constructor) word by word. That is: “I am here” should be 
#reversed as “here am I”. Create instances of this class for each of the three strings input by the user and display the 
#reversed string for each, in descending order of number of vowels in the string 
 
strings_dictionary = {} 
sortedstrings = [] 
        
class string_rev: 
    sentence = " " 
        
    def __init__(self,sentence):  
        self.sentence = sentence 
    
    def reverse(self):  
            word_split = self.sentence.split(' ') 
            word_split.reverse() 
            reversed_sentence = ' '.join(word_split) 
            print(reversed_sentence) 
 
            total_vowels =  self.sentence.count('a')+self.sentence.count('e')+self.sentence.count('i')+self.sentence.count('o')+self.sentence.count('u') 
            +self.sentence.count('A')+self.sentence.count('E')+self.sentence.count('I')+self.sentence.count('O')+self.sentence.count('U') 
 
            strings_dictionary[reversed_sentence] = total_vowels 
            strings_dictionary.update({reversed_sentence:total_vowels}) 
             
##or key = lambda Y : Y[1]            
##The method items() returns a list of dict's (key, value) tuple pairs 
##The method get() returns a value for the given key. If key is not available then returns default value None. 
 
s1 = input("\nEnter first sentence:\n") 
string_rev(s1).reverse() 
 
s2 = input("\nEnter second sentence:\n") 
string_rev(s2).reverse() 
 
s3 = input("\nEnter third sentence:\n") 
string_rev(s3).reverse() 
 
print("\n------Descending order of the number of vowels------\n") 
for word in sorted(strings_dictionary , key = strings_dictionary.get , reverse = True): 
    print(word, ':' ,strings_dictionary[word]) 

