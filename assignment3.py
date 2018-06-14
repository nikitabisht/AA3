#question1

list=[]
name1= input("enter the number for the list")
list.append(name1)
name2= input("enter the number for the list")
list.append(name2)
print("the list is", list)

#question2

a=[]
b=["google","apple","facebook","microsoft","tesla"]
a.append(b)
print(a)

#question3

a=["java","python","java","php","java"]
print(a.count("java"))

#question4

a=[8,3,1,9,2]
a.sort()
print(a)

#question5

A=[1,2,3,4]
B=[5,6,7,8]
C=A+B
print(C)

#question6

a=[1,2,3,4,5]
a.pop()
print(a)

#question7

number = (1,2,3,4,5,6,7)
print("total even:", len ([i for i in number if (i%2==0)]))
print ("total odd:", len ([i for i in number if (i%2!=0)]))