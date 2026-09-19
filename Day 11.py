# def add_two_numbers(num1,num2):
#     sum = num1 + num2
#     return sum
# a = add_two_numbers(int(input('number 1:')),int(input('number 2:')))
# print(a)

# def area_of_circle(r):
#     pie = 3.14
#     area = pie*r*r
#     return area
# b = area_of_circle(int(input('Radius:')))
# print(f'{b:.2f}')

# def add_all_nums(*nums):
#    sum=0
#    for num in nums:
#     if isinstance(num,str):
#       return 'Error string detected'
#     else:
#        sum += num
#    return sum
# c = add_all_nums(2,2,2,2)
# print(c)

# def convert_celsius_to_fahrenheit(C):
#     F = (C * 9/5) + 32
#     return F
# d = convert_celsius_to_fahrenheit(int(input('Celsius:')))
# print(d)

# def check_season(month):
#     if month in ('September', 'October', 'November') :
#         return "Autumn"
#     elif month in ('December','January', 'February') :
#         return "Winter"
#     elif month in ('March', 'April', 'May') :
#         return "Spring"
#     elif month in ('June', 'July', 'August') :
#         return "Summer"
#     else:
#         return 'Error'
# print(check_season(str(input('Enter the month:').title())))
     
# def calculate_slope(a,b):
#      x_1 , y_1 = a
#      x_2 , y_2 = b
#      M = (y_2 - y_1)/(x_2 - x_1)
#      return M

# print(calculate_slope([2,3],[5,4]))

# def solve_quadratic_eqn(a,b,c):
#     x_1 = (-b+(b**2-4*a*c)**0.5)/2*a
#     x_2 = (-b-(b**2-4*a*c)**0.5)/2*a
#     return x_1,x_2
# print(solve_quadratic_eqn(1,6,9))
    
# def print_list(a):
#     for i in a:
#         print(i)

# print_list()

# def reverse_list(a):
#     b=[]
#     for i in a[-1::-1]:
#         b.append(i)
#     return b
# print(reverse_list([1, 2, 3, 4, 5]))
# print(reverse_list(["A", "B", "C"])) 

# def capitalize_list_items(a):
#     b = []
#     for i in a:
#         b.append(i.capitalize())
#     return b
# print(capitalize_list_items(['potato', 'tomato', 'mango', 'milk']))

# def add_item(a,b):
#     a.append(b)
#     return a
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_stuff, 'Meat'))

# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))  

# def  remove_item(a,b):
#     a.remove(b)
#     return a
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# print(remove_item(food_stuff, 'Meat'))

# numbers = [2, 3, 7, 9, 5]
# print(remove_item(numbers, 5))

# def sum_of_numbers(a):
#     sum = 0
#     for i in range(1,a+1):
#         sum += i
#     return sum
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050

# def sum_of_odds(a):
#     sum_odd = 0
#     for i in range(1,a+1):
#         if i%2 == 1:
#             sum_odd += i
#     return sum_odd
# print(sum_of_odds(5))  
# print(sum_of_odds(10)) 
# print(sum_of_odds(100)) 

# def sum_of_even(a):
#     sum_even = 0
#     for i in range(1,a+1):
#         if i%2 == 0:
#             sum_even += i
#     return sum_even
# print(sum_of_even(5))  
# print(sum_of_even(10)) 
# print(sum_of_even(100)) 

# def evens_and_odds(a):
#     odds = 0
#     evens = 0
#     for i in range (1,a + 1):
#         if i % 2 == 1:
#             odds += 1
#         if i % 2 == 0:
#             evens += 1
#     return f'The number of odds are {odds}.\nThe number of evens are {evens}.'
# print(evens_and_odds(100))
    
# def factorial(a):
#     b = 1
#     if a == 0:
#         return 1
#     for i in range(1,a+1):
#         b *= i
#     return b
# print(factorial(4))

# def is_empty(a):
#     if a == [] or a == () or a == {}:
#         return 'It is empty'
#     else:
#         return 'Not empty'
# b = [1,2,3]
# print(is_empty(b))

# def calculate_mean(a):
#     sum = 0
#     N = 0
#     for i in a:
#         sum += i
#         N += 1
#     mean = sum / N
#     print(mean)
# calculate_mean([2, 3, 7, 9])
    
# def calculate_median(a):
#     b = sorted(a)
#     if len(b)%2 == 0:
#         M1 = b[len(b)//2]
#         M2 = b[(len(b)//2)-1]
#         M = (M1+M2)/2
#     else:
#         M = b[len(b)//2]
#     print(M)
# calculate_median([2, 3, 7, 9])

import statistics

# def calculate_mode(a):
#     Mode = statistics.multimode(a)
#     return Mode
# print(calculate_mode([1,1,1,2,2,2,3,4,5,6,6,7,7,8,8]))

# def calculate_range(a):
#     b = sorted(a)
#     c = min(b)
#     d = max(b)
#     Range = d - c 
#     print(Range)
# calculate_range([5,4,7,6,9,8,10])

# def calculate_variance(a):
#     b = statistics.variance(a)
#     print(f'variance: {b}')
#     c = statistics.pvariance(a)
#     print(f'pvariance: {c}')
# calculate_variance([5,4,7,6,9,8,10])

# def calculate_std(a):
#     b = statistics.stdev(a)
#     print(b)
#     c = statistics.pstdev(a)
#     print(c)
# calculate_std([5,4,7,6,9,8,10])

# def greet(Name='Guest'):
#     print(f"Hello, {Name}")
# greet('Nico')

# def show_args(**a):
#     for name, value in a.items():
#         print(f'{name}: {value}', end=',')

# # show_args(name="Alice", age=30, city="New York")
   
# show_args(name="Bob", pet="Fluffy, the bunny")

# def is_prime(a):
#     if a%2 == 1 and a%3 == 1:
#         return 'prime'
#     else:
#         return 'Not prime'
    
# print(is_prime(6))

# def unique(a):
#     if len(a) == len(set(a)):
#         print('unique')
#     else:
#         print('Not unique')

# unique([1,2,4,4,5])

# def check_same_type(lst):
#     # An empty list or a list with one item is technically homogeneous
#     if not lst:
#         return True
        
#     first_type = type(lst[0])
#     return all(type(item) is first_type for item in lst)

# print(check_same_type([]))

import keyword

def is_valid_variable_name(name: str) -> bool:
    """Checks if a string can be used as a valid Python variable name."""
    # Ensure the input is a string
    if not isinstance(name, str):
        return False
        
    # Check if it's a valid identifier and not a reserved keyword
    return name.isidentifier() and not keyword.iskeyword(name)

print(is_valid_variable_name())