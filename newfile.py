#1
print(3+4)    #addition(+)
print(3-4)      #substraction(-)
print(3*4)      #multiplication(*)
print(3**4)     #exponetial(**)
print(3/4)       #division(/)
print(3//4)       #floor division operator(//)
print(3%4)        #modulus(%)
print()
print()

#2
print("Daniel")
print("Amao")
print("Nigeria")
print("I am enjoying 30days of python challenge")
print()
print()

#3
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Amao', 'Python', 'Nigeria']))
print(type('Dan'))
print(type("'Amao'"))
print(type("Nigeria"))
#4
print()
first_name, last_name, country, age, is_married = 'Amao', 'Daniel', 'Nigeria', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
#5
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
#6
# Printing out types
print(type('Amao'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2,3,4]))     # list
print(type({'name':'Amao','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))      
#
print()
# int to float

num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int

gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int
num_str = 10.6
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Asabeneh'
print(first_name)
print(first_name)                    # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
#
print()
#7
first_name="Daniel"
print(len(first_name))
print()
#8
first_name="Daniel"
last_name="Amao"
print(len(first_name))
print(len(last_name))
print()
#9
num_1=5
num_2=4
variable_total=num_1+num_2
print(variable_total)
print()
variable_diff=num_1-num_2
print(variable_diff)
print()
variable_product=num_1*num_2
print(variable_product)
print()
variable_division=num_1/num_2
print(variable_division)
print()
variable_remainder=num_1%num_2
print(variable_remainder)
print()
variable_exp=num_1**num_2
print(variable_exp)
print()
variable_floor_division=num_1//num_2
print(variable_floor_division)

r=30
area_of_circle=  3.14*r**2
print(area_of_circle)
print()
#10
first_name, last_name, full_name, country, city, age, year, is_married, is_light_on= 'Amao', 'Daniel', 'Amao Daniel', 'Nigeria', 'Lagos', 10, 2022, False, 'Yes'
print(first_name, last_name, country, age, is_married, sep=" ; ")
print('First name:', first_name)
print('Last name: ', last_name)
print("Full name:", full_name)
print('Country: ', country)
print('City:', city)
print('Age: ', age)
print('Year:', year)
print('Married: ', is_married)
print('Light: ', is_light_on)
#11
print("Tell me anything...")
anything = input()
print("Hmm...", anything, "... Really?")

#12
anything = int(input("Enter a number: "))
something = anything ** 2.0
print(anything, "to the power of 2 is", something)