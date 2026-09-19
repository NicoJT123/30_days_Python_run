S = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(S)

a='Coding'
b='for'
c='all'
s=f'{a} {b} {c}'
print(s)

company=s
print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())

print(company.swapcase())

print(company.title())

print(company[7:14])
text = "Coding For All"
result = text.split(' ', 1)[1]#(' ', 1 artinya 1 sampai seterusnya gabung  menjadi 1 )[1 artinya yang di ambil 1]
print(result)  # Output: For All

print(company.index('Coding'))
print(company.find('Coding'))
print(company.startswith('Coding'))

print(company.replace('Coding' , 'Python'))

print('Python for Everyone'.replace('Everyone' , 'All'))

print(company.split())

app="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(app.split())
print(app.split(', '))

print(company.index('C'))
print(company[0])

print(company[-1])

print(company[10])

print('Python For Everyone'[0:-1:11])

print('Coding For All'[0:-1:11])

print(company.index('C'))

print(company.index('f'))

print(company.rfind('l'))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

print(sentence.rindex('because'))

print(sentence[31:54])
print(sentence[sentence.index('because'):sentence.rindex('because')+7])

print(company.startswith('Coding'))

print(company.endswith('Coding'))

print('   Coding For All      '.strip(' '))

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

python_libraries= ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' '.join(python_libraries))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\t        Age\tCountry\t   City \nAsabeneh\t250\tFinland\t   Helsinki')
print('Name    \tAge\tCountry\t   City')
print('Asabeneh\t250\tFinland\t   Helsinki')

radius = 11
area = 3.14 * radius ** 2
print('The area of a circle with radius %d is %.0f meters square.'%(radius,area))

a=8
b=6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b:.2f}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')