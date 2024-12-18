print("There once was a man named George")
print("He was 70 years old.")
print("He really liked the name George,")
print("but didn't like being 70.")
print()

name="Debrato"
age=18
print("There once was a man named "+name)
print("He was",age,"years old.")
name="Deb"
print()
print(f"He really liked the name {name},")
print("but didn't like being {}.".format(age))
print()
print("My name is "+name+" and I am "+str(age)+" years old")
print("\n")
print("test if two lines")
print("Hello\nWorld")
print("Hello \" World")
print()
phrase="Debrato"
print(phrase)
print(len(phrase))
print(phrase[0])
print(phrase[-1])
print(phrase.index("e"))
print(phrase.index("br"))
print(phrase.replace("Deb","Cat"))
print()

print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print()
phrase="debrato"
print(phrase.capitalize())

print()
print(23)
print(23.56)
print(-23)
print(3+4)
print(2*3*(4+5))
print(eval("3+4+5"))
print(10%3)
print()

x="10";m=25
y=int(x)
z=float(x)
n=str(m)
print(x, y, z, m, n)
print(abs(-23))
print()
phrase="Hello, World"
print(phrase.split(","))
words=["Hello","World"]
print(" ".join(words))
fruits=["apple","banana"]
fruits.append("cherry")
print(fruits)
print()

number=[5,3,8,1]
m=number.sort()
print(number)
print(m)
print()

num=[5,3,8,1]
n=sorted(num)
print(num)
print(n)
print()

text = "hello world"
print(text.removeprefix("hello"))
print(text.removesuffix("world"))
print(text.replace("ello ",""))
print()

y=30
import math
print(math.pi)
print(math.sin(math.radians(y)))
print()

x=25.3
print(round(x))
from math import *
print(floor(x))
print(ceil(x))
print(sqrt(x))
print()

name=input("Enter your name:")
print("Hello", name)
print(input())
print()

print(int(23.56))
print()

mixed=[1,"hello",3.14,True]
print(mixed)
print(mixed[0])
print(mixed[-1])
print()

number=[0,1,2,3,4,5]
slice1=number[1:4]
slice2=number[:3]
slice3=number[::2]
slice4=number[2:]
slice5=number[::-1]
print(slice1)
print(slice2)
print(slice3)
print(slice4)
print(slice5)
print()

str1="Hello"
print(list(str1))
print()

num=[1,2,3,4,5]
print(num)
num[4]=87
print(num)
num.append(6)
print(num)
num.insert(1,100)
print(num)
num.extend([33,55])
print(num)
num.remove(33)
print(num)
print(num.pop())
print(num)
num.pop(0)
print(num)
num.remove(2)
print(num)
print(num.count(3))
print(num.index(3))
num.sort()
print(num)
n1=num.copy()
num.clear()
print(num)
print(n1)
print()

num=[12,34,33,7,3,9]
print(sorted(num))
print(list("Debrato"))
print()

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=list1+list2
print(list1)
print(list2)
print(list3)
print()

tuple1=(1,2,3)*2
list1=[1,2,3]*2
print(tuple1)
print(list1)
print(3 in tuple1)
print(3 in list1)
print(5 in tuple1)
print(5 in list1)









