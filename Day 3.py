age = 18
height = 1.83
print(type(1 + 2j))

B = float(input('Enter base :'))
H = float(input('Enter height :'))
area = 0.5*B*H
print(area)

a=float(input('Enter a :'))
b=float(input('Enter b :'))
c=float(input('Enter c :'))
perimeter = a+b+c
print(perimeter)

r=float(7)
area_circle=3.14*r**2
c=2*3.14*r
print(area_circle)
print(c)

m_1=2.0
print(m_1)

(x_1,y_1)=(2,2)
(x_2,y_2)=(6,10)
m_2=(y_2-y_1)/(x_2-x_1)
print(m_2)

print(m_1==m_2)

a=1
b=6
c=9
x=(-b+(b**2-4*a*c)**0.5)/2*a
y=x**2+6*x+9
print('x=',x)
print('y=',y)

print('Python=',len('python'))
print('Dragon=',len('dragon'))
print('on in python=','on' in 'python')
print('on in dragon=','on' in 'dragon')

print('jargon is in I hope this course is not full of jargon=','jargon' in 'I hope this course is not full of jargon')

print('There is no on in both dragon and python=', 'on' not in 'dragon and python')

print(str(float(len('python'))))

n=int(input('Number='))
if n%2 == 0 :
   print('Even')
else :
   print('Odd')

print(7//3 == int(2.7))

print(type('10') == type(10))

print(int(9.8) == 10)

h=int(input('Enter hours:'))
r=int(input('Enter rate per hour:'))
e=h*r
print('Your weekly earning is ', e)

y=int(input('Enter number of years you have lived:'))
s=y*365*24*60*60
print (f'You have lived for {s} seconds.')

for x in range(1,6) :
   print(x , x**0 , x**1 , x**2 , x**3 , x**4)