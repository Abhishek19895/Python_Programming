__author__ = 'abhisheksingh29895'

''' I have used the below url's to help answer this question
1.  "http://www.cyberciti.biz/faq/python-raw_input-examples/"
2.  "http://www.regular-expressions.info/numericranges.html"
3.  "http://stackoverflow.com/questions/10373660/converting-a-pandas-groupby-object-to-dataframe"
'''

#using the module for regular expressions
import  re
import  pandas  as  pd


#Problem 1 : Billing form validation and parsing

#------------------------   Name parsing
def validate_name(name,  name_type):
    I_name  =  name.split()
    len_name  =  len(I_name)
    #If the name consists of 3 words it contains a middle name
    if (len_name  == 3  and  name_type  ==  1):
        first_name  =  I_name[0];  middle_name  =  I_name[1];  last_name  =  I_name[2]
        fn  =  re.match(r'^[A-Za-z-]+',  first_name)  ;  mn  =  re.match(r'^[A-Za-z-]+',  middle_name)
        ln  =  re.match(r'^[A-Za-z-]+',  last_name)
        if (fn  and  mn  and  ln):
            print "Valid Name"
            print "The first name is :", first_name
        else:
            print "Invalid Name"
    elif (len_name  == 2  and  name_type  ==  1):
        first_name  =  I_name[0];  last_name  =  I_name[1]
        fn  =  re.match(r'^[A-Za-z-]+',  first_name)  ;  ln  =  re.match(r'^[A-Za-z-]+',  last_name)
        if (fn  and  ln):
            print "Valid Name"
            print "The first name is :", first_name
        else:
            print "Invalid Name"
    elif (len_name  == 3  and  name_type  ==  2):
        first_name  =  I_name[1]  ;  middle_name  =  I_name[2]  ;  last_name  =  I_name[0]
        fn  =  re.match(r'^[A-Za-z-]+',  first_name)  ;  mn  =  re.match(r'^[A-Za-z-]+',  middle_name)
        ln  =  re.match(r'^[A-Za-z-,]+',  last_name)
        if (fn  and  mn  and  ln):
            print "Valid Name"
            print "The first name is :", first_name
        else:
            print "Invalid Name"
    elif (len_name  == 2  and  name_type  ==  2):
        first_name  =  I_name[1];  last_name  =  I_name[0]
        fn  =  re.match(r'^[A-Za-z-]+',  first_name)  ;  ln  =  re.match(r'^[A-Za-z-,]+',  last_name)
        if (fn  and  ln):
            print "Valid Name"
            print "The first name is :", first_name
        else:
            print "Invalid Name"
    else:
        print "Invalid Name"


#------------------------   Address input
def validate_address(address):
    #Checking for filters
    St  =  re.search("(St)",  address)
    ave  =  re.search("(ave)",  address)
    street  =  re.search("(street)",  address)
    Street  =  re.search("(Street)",  address)
    rm  =  re.search("(rm)",  address)
    Rm  =  re.search("(Rm)",  address)
    apt  =  re.search("(apt)",  address)
    index  =  ""
    #Validating the input string based on filters
    if  Street:
        print "Valid Address"
        index  =  "Street"
    elif  ave:
        print "Valid Address"
        index  =  "ave"
    elif  street:
        print "Valid Address"
        index  =  "street"
    elif  St:
        print "Valid Address"
        index  =  "St"
    elif  rm:
        print "Valid Address"
    elif  Rm:
        print "Valid Address"
    elif  apt:
        print "Valid Address"
    else:
        print "Invalid Address"

#Catching the street name
    if index:
        Add_split  =  address.split()
        position  =  Add_split.index(index)
        Street_name  =  Add_split[position  -  1]
        print "Name of the street is :",  Street_name


#----------------------------- Phone input
def validate_phone(phone):
    phone_match1  =  re.match(r'\d{3}-\d{3}-\d{4}',  phone)
    phone_match2  =  re.match(r'\(\d{3}\)\d{3}-\d{4}',  phone)
    phone_match3  =  re.match(r'\d{3}-\d{4}',  phone)
    #Validating the input string based on filters
    if  phone_match1:
        print "Valid Phone Number"
    elif  phone_match2:
        print "Valid Phone Number"
    elif  phone_match3:
        print "Valid Phone Number"
    else:
        print "Invalid Phone Number"



#-----------------------------   email
def validate_email(email):
    #Checking for filters
    edu_match  =  re.match(r'.+.edu',  email)
    com_match  =  re.match(r'.+.com',  email)
    org_match  =  re.match(r'.+.org',  email)
    #Validating the input string based on domain filters
    if  edu_match:
        print "Valid Domain"
        print "The Domain is: edu"
    elif  com_match:
        print "Valid Domain"
        print "The Domain is: com"
    elif  org_match:
        print "Valid Domain"
        print "The Domain is: org"
    else:
        print "Invalid Domain"


#----------------------------    credit card
def validate_credit_card(credit_card):
    #Checking for filters
    credit16_match  =  re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$',  credit_card)
    credit15_match  =  re.match(r'^\d{4}-\d{6}-\d{5}$',  credit_card)
    #Validating the input string based on domain filters
    if  credit16_match:
        print "Valid Credit Card"
    elif  credit15_match:
        print "Valid Credit Card"
    else:
        print "Invalid Credit Card"


#Calling all the functions
def main():
#I am building an option for the user to select his naming style and then enter his name
    name_type  =  raw_input('(Naming style) Enter 1 or 2, where  1. (First_Name Last_Name) or 2. (Last_Name, First_Name) :')
    name_type  =  int(name_type)
    name  =  raw_input("Enter your Full Name")
    validate_name(name,  name_type)
    address  =  raw_input('Enter your address : ')
    validate_address(address)
    email  =  raw_input('Enter your email : ')
    validate_email(email)
    phone  =  raw_input('Enter your phone number: ')
    validate_phone(phone)
    credit_card  =  raw_input('Enter your credit card number : ')
    validate_credit_card(credit_card)

#Calling the main functions
main()
