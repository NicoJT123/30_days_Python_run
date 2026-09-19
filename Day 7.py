# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_companies.update({'Youtube','NVIDIA','Tiktok'})
print(it_companies)

it_companies.remove('Google')
print(it_companies)
it_companies.discard('Instagram')
print(it_companies)

C = A.union(B)
print(C)

print(A & B)
print(A.intersection(B))

print(A.issubset(B))

print(A.isdisjoint(B))

D = A.union(B)
E = B.union(A)
print(D)
print(E)

print(A.symmetric_difference(B))
print(A ^ B)

del A
del B
del C
del D

age_set = set(age)
print(age_set)
print(len(age))
print(len(age_set))
print(len(age) > len(age_set))
print(len(age) < len(age_set))
print(len(age) == len(age_set))

string = ''
list = []
tuple = ()
set_1 = {}

sentence = 'I am a teacher and I love to inspire and teach people'
list = sentence.split()
print(list)
sets = set(list)
print(sets)
print(len(sets))