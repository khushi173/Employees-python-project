'''for i in range(1,10):
    print('hi'*i ,end=' ')

a = int(input('enter the value of a:'))
b = int(input('enter the value of b:'))

if a > b:
    print('hello')
else:
    print('a is not big')
if a > b:
    print('hello')
elif a==b:
    print('both are equal')
elif a<b:
    print('a is small')
while a < b:
    print('hhi')
    break
a = [1,5,2,8,7]
  #b = [1,25,4,64,49]

b = []
for i in a:
    c = i**2
    b.append(c)
print(b)

print([i**2 for i in a])
f=[]
for i in 'python':
    for j in 'learn':
        f.append(i+j)
        print(f)
h = [i+j for i in 'python' for j in 'learn']
g = [ i[-1] for i in h]
print(g)
a = ['tom','python','sam']
b = {}
for i in a:
    b[i] = len(i)
    print(b)

#dictionary comprehension
a = ['tom','python','sam']
m = {i:len(i) for i in a}
print(m)

a= ['tom','sam','john']
b = [85,98,91]
m = {a:b for(a, b)  in zip(a,b)}
print(m)

a= ['tom','sam','john']
b = [85,98,91]
c = []
for i in range(3):
    c.append((a[i],b[i]))
print(c)

a = [('chn',32),('Bang',31),('delhi',33)]
 #{'chn':32,'Bang':31,'delhi':33}
b = {i:j for i,j in a}
print(b)




lst1=[3.14, 66, "Teddy Bear", True, [], {}]
lst2=[]
for i in lst1:
    lst2.append(type(i))
    print(lst2)

a = int(input("Enter the number :"))
if (a%2) == 0:
    print(a,'is even number')
else:
    print(a,'is odd number')

    #functions:
def my_func():
    print('hello')
my_func()
print('-'*50)

for i in range(5):
    my_func()
print('!'*50)
a = my_func()

def my_func2():
    return('hi')

def my_func3():
    print('hello')

a = my_func2()
b = my_func3()

print(a)
print(b)

#arguments
x = int(input("enter the value"))
def my_func4(x):
    return x**2
a= my_func4(x)
print(a)

#Default arguments


def my_func6(x, y=5, z = True):
    while z:
        print(x+y)

c= my_func6(3,y=6)
print(c)

#keyword argumrnt
def my_func7(x=5, y=6, z = 10):
    return x+y+z
v= my_func7(z=100,x=50)
print(v)

#arbitary arguments
def my_fuc(*signal):
signal_strength = my_func(5,9,32,4,6,8)
print(signal_strength)'''

#arbitary keywords
def my_func(**kw):
   # print(type(kw))
    print(kw.values())
    return sum(kw.values())
a= my_func(x =10, y=20, c=50, b=2.5)
print(a)

                #opening a file in python
'''f= open("C:\\Users\\hp\\OneDrive\\Documents\\harman.txt",mode='w', encoding='cp1252')
f.write('\nWelcome to python\n')
f.write('Weather is good')
f.close()

             #writelines() methods
f= open("C:\\Users\\hp\\OneDrive\\Documents\\harman.txt",mode='w', encoding='cp1252')
f.writelines(['Good luck' , 'See you soon'])
f.close()
f= open("C:\\Users\\hp\\OneDrive\\Documents\\harman.txt",mode='r', encoding='cp1252')
print(f.read())

             #readlines() methods
f= open("C:\\Users\\hp\\OneDrive\\Documents\\harman.txt",mode='r', encoding='cp1252')
print(f.readlines())


          #readline() method

f= open("C:\\Users\\hp\\OneDrive\\Documents\\harman.txt",mode='r', encoding='cp1252')
print(f.readline())


a = [1,2,3,4,5]
print('List of numbers:',a)
print('\nSquare of numbers in the list:')
square_a = list(map(lambda x: x**2, a))
print(square_a)
print('\nCube of numbers in the list:')
cube_a = list(map(lambda x: x**3,a))
print(cube_a) '''

































