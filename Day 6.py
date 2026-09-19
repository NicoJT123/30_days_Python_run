empty_tuple = ()
brother = ('keyne',)
sister = ('Nancy',)
Siblings = brother + sister
print(Siblings)

print(f"How many siblings do you have? {len(Siblings)}")

mother = ('Mardiyana',)
father = ('Sudiman',)
family_members = Siblings + mother + father
print(family_members)

Siblings = family_members[0:2]
Parents = family_members[2:]
print(Siblings)
print(Parents)

Fruits =('Apple','Banana','Orange')
Vegetables =('Cucumber','Carrot','Cabbage')
Animal_Products = ('Milk','Chicken','Egg')
food_stuff_tp = Fruits + Vegetables + Animal_Products
print(food_stuff_tp)

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt) 

print(food_stuff_lt[int(len(food_stuff_lt)/2)])

first_three_items = food_stuff_lt[0:3]
print(first_three_items)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
a = input('is it a nordic country :')
b = a in nordic_countries
if b is True:
    print('yes')
else:
    print('no')