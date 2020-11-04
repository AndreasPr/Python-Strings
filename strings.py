# It is an ordered, immutable collection data type and it is used for text representation

my_string = "hello"
print(my_string)

#-------Triple quotes (Used for multi-line strings)------------
my_string2 = """Hello
World"""
print(my_string2)

 #------------------------------------Access Elements---------------------------------
my_string3 = "Hello Andreas"
char = my_string3[1]
char2 = my_string3[-1]
print(char) #e
print(char2) #s

#---------------------------------------Substring------------------------------------
my_string4 = "Hello Andreas"
substring1 = my_string4[1:5]
substring2 = my_string4[:5]
substring3 = my_string4[:]
print(substring1) #ello
print(substring2) #Hello
print(substring3) #Hello Andreas

#----------------------------------------Stepping------------------------------
my_string5 = "Hello Andreas"
substring_step1 = my_string5[::1]
substring_step2 = my_string5[::2]
substring_step3 = my_string5[::-1] #trick to reverse the string
print(substring_step1) #Hello Andreas
print(substring_step2) #HloAdes
print(substring_step3) # saerdnA olleH

#------------------------------------------Concatenation---------------
greeting = "Hello"
name = "Andreas"
sentence = greeting + " " + name
print(sentence) #Hello Andreas

# -----------------------------------------Iteration--------------------
greeting = "Hello"
for i in greeting:
    print(i)

#------------------------------------------If Statement-------------------------------
greeting2 = "Hello"
if 'o' in greeting2:
    print("Yes")
else:
    print("No")
#------------------------------------------Remove Whitespaces----------------
my_string6 = "               Hello Andreas             "
my_string6 = my_string6.strip()
print(my_string6) #Hello Andreas

#------------------------------------------String with Capital, lower Letters, startswith, endswith, find, count, replace--------
my_string7 = "Hello Andreas"
print(my_string7.upper()) #HELLO ANDREAS
print(my_string7.lower()) #hello andreas
print(my_string7.startswith('Hello')) #True
print(my_string7.endswith('Andreas')) #True
print(my_string7.find('o')) # 4. Returns the index of the first o
print(my_string7.find('lo')) # 3. Returns the index of the first letter from the substring
print(my_string7.find('tr')) #-1. It didn't find the string
print(my_string7.count('l')) #2 How many o exist
print(my_string7.replace('Andreas', 'World')) #Hello World (returns a new string, it does not change the original)

#-----------------------------------------Convert a String to List---------------
my_string9 = "How are you"
my_list = my_string9.split(" ") #Space is the default
print(my_list) #['How', 'are', 'you']

my_string10 = "How,are,you"
my_list1 = my_string10.split(",")
print(my_list1) #['How', 'are', 'you']

#-----------------------------------------Convert a List to String----------------
my_string11 = "How,are,you"
my_list2 = my_string11.split(",")
print(my_list2) #['How', 'are', 'you']
new_string = " ".join(my_list2)
print(new_string) #How are you



#-----------------------------------------Time Comparison of the Performance in conversion of a List to String------

from timeit import default_timer as timer
my_list3 = ['a'] * 1000000


#BAD PRACTICE FOR CONVERSION FROM LIST TO STRING
start = timer()
my_string13 = ""
for i in my_list3:
    my_string13 += i
stop = timer()
print(stop - start) #0.3544739
#print(my_string13) #aaaaaaa


# GOOD PRACTICE FOR CONVERSION FROM LIST TO STRING
start = timer()
my_string12 = "".join(my_list3)
stop = timer()
print(stop - start) #0.008831499999999992
#print(my_string12) #aaaaaaa

#----------------------------------------------------------Format a String---------------------------------
#--------- 1st way:
varString = "Andreas"
varNumber = 2
varFloatNumber = 2.1954657

my_string14 = "The variable is %s" %varString
my_string15 = "The variable is %d" %varNumber
my_string16 = "The variable is %.2f" %varFloatNumber 
print(my_string14)
print(my_string15)
print(my_string16)

#--------- 2nd way:
varNumber2 = 5
varFloatNumber2 = 2.942534
my_string17 = "The variable is {}".format(varNumber2)
my_string18 = "The variable is {:.2f}".format(varFloatNumber2)
my_string19 = "The variable is {:.2f} and {}".format(varNumber2, varFloatNumber2)
print(my_string17)
print(my_string18)
print(my_string19)

#---------- 3rd way (FASTEST):
varNumber3 = 5
varFloatNumber3 = 2.942534
my_string20 = f"The variable is {varNumber3} and {varFloatNumber3}"
my_string21 = f"The variable is {varNumber3*2} and {varFloatNumber3}"
print(my_string20)
print(my_string21)







