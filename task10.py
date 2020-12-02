#only a certain set of characters (in this case a-z, A-Z and 0-9).
import re
str=input("enter the sentence:")
x=re.compile("[A-Za-z0-9]+")
print(x)
if x.fullmatch(str):
    print("valid")
else:
    print("not valid")


#containing 'ab'
str=input("enter the string:")
if re.search('ab',str):
    print(" ab is present ")
else:
    print("ab is not present")

#number at the end of a word/sentence
str1=input("enter the sen:")
if re.search(r'\d$',str1):
    print("last word has a number ")
else:
    print("last word does not have a number")

#numbers (0-9) of length between 1 to 3
str2=input("enter the stringgg")
if re.search('\d',str2) and len(str2)<=3:
    print("yes")
else:
    print("no")

#uppercase letters
str3=input("enter the sentence:")
if re.match("^[A-Z]+$",str3):
    print("match")
else:
    print("no match")
