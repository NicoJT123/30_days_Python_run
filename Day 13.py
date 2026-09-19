# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# Positive_numbers = [i for i in numbers if i > 0]
# print(Positive_numbers)

# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_list = [i for j in list_of_lists for i in j]
# print(flat_list)

# list_of_tuples = [(x , x**0 , x**1 , x**2 , x**3 , x**4 , x**5) for x in range(11)]
# print(list_of_tuples)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# c={
#     'FINLAND':'FIN',
#     'SWEDEN': 'SWE',
#     'NORWAY':'NOR'
# }
# d = [[a.upper(),a.upper()[:3],b.upper()] for i in countries for a,b in i]
# print(d)

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# a = [{'country':b.upper(),'city':c.upper()} for i in countries for b,c in i]
# print(a)

# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# a = [[b + ' ' + c] for i in names for b,c in i]
# print(a)

slope = lambda x_1,y_1,x_2,y_2 : (y_2-y_1)/(x_2-x_1)
print(slope(2,2,6,10))