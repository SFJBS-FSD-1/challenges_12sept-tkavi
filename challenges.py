#Challenge 1:  Write a function that takes a natural number as input and outputs the number of digit in it.
# Conversion of number to string is not allowed

def digits_count(user_input):
    no_of_digits = 0
    while (user_input >= 1):
        user_input=user_input//10
        no_of_digits+=1
    return no_of_digits

user_input = int(input("Enter a Natural Number: "))
print("No. of digits in user_input are:",digits_count(user_input))

# Challenge 2:  Write a function that takes a natural number as input and outputs the reverse of that number.
# Conversion of number to string is not allowed

def reverse_of_num(user_input):
    reversed_num = 0
    rem=0
    while (user_input > 0):
        rem = user_input%10
        user_input = user_input//10
        reversed_num = reversed_num*10 + rem
    return reversed_num

user_input = int(input("Enter a Natural Number : "))
print("Reverse of user_input "+str(user_input)+" is ",reverse_of_num(user_input))

# Challenge 3 : Write a function where user will enter a natural number as input and output returns the
# number of zeroes in the end of the factorial of that number. Conversion of number to string is not allowed

def no_of_zeroes(user_input):
    zeroes=0
    i = 1
    fact=1

    while(i<user_input):
        fact = fact*i
        i = i+1
    print("Factorial of "+str(user_input)+" is",fact)

    while (fact != 0):
        rem=fact%10
        fact=fact//10
        if rem==0:
            zeroes+=1
        else:
            break
    return zeroes

user_input = int(input("Enter a Natural Number : "))
print("No. of zeroes in "+str(user_input)+"! is ",no_of_zeroes(user_input))

# Challenge 4 : list1 = ["India" , "England", "Spain"]
#               list2 = ["Delhi","London","Madrid"]
# Write your own function that takes list1 and list2 as inputs and returns a dictionary like
# dict1 = {“India” : “Delhi” , “England”:”London”, “Spain”:”Madrid”}

def country_capital(list1,list2):
    dict_cntry_cptl ={}
    for country in list1:
        for capital in list2:
            if list1.index(country)==list2.index(capital):
                dict_cntry_cptl[country]=capital
    return dict_cntry_cptl

list1 = ["India" , "England", "Spain"]
list2 = ["Delhi","London","Madrid"]
print(country_capital(list1,list2))

# Challenge 5: Given places = {(“19.07'53.2”, “72.54'51.0”): "Mumbai",(“28.33'34.1”, “77.06'16.6”): "Delhi"}
# Write code to create a new dictionary using given dictionary
# city = {"Mumbai": {“Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”},
#         “Delhi”: {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”}}

def places_lon_lat(places):
    new_places={}
    lon_lat={}
    for key in places:
        lon_lat["Latitude"]=key[0]
        lon_lat["Longitude"]=key[1]
        new_places[places[key]]=lon_lat
    return new_places

places = {("19.07'53.2","72.54'51.0"): "Mumbai",("28.33'34.1", "77.06'16.6"): "Delhi"}
print(places_lon_lat(places))

# Challnege 6 : Given mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
# Using for loop find the sum of all even numbers in mylist

def sum_even_nos(mylist):
    sum_even=0
    for i in mylist:
        if i%2 == 0:
            sum_even+=i
    return sum_even

mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
print(sum_even_nos(mylist))