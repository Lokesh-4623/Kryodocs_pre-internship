# -*- coding: utf-8 -*-
"""week2_assignment.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/161tnNWqeVo2qoUeCTaV84zgGpYeSJD5a
"""

#Given a list of numbers, find the sum of all the elements in the list.
num=[9,8,7,6,3]
sum=0
for i in num:
  sum=sum+i
print(sum)

#Given a list of strings, find the longest string in the list.
fruits=["Apple","Mango","Orange","Watermelon","Banana"]
max=""
for i in fruits:
  if(len(i)>len(max)):    #length of the string can be find by using len()
    max=i
print(max)

#Given a list of numbers, create a new list that contains only the even numbers from the original list.
num=[9,8,4,3,2,1,8,20,79,56]#list allows duplicates
even_num=[]
for i in num:
  if(i%2==0):
    even_num.append(i)
print("The Even numbers are:",even_num)

#Given a list of strings, create a new list that contains only the strings that start with the letter 'a'.
old_str=["good","ask","pillow","allow","aeroplane","lotus"]
new_str=[]
for i in old_str:
  if(i[0]=='a'):
      new_str.append(i)
print(new_str)

#Given a list of nested lists, create a new list that contains the sum of all the values in the nested lists.
l=[[1,2,3],[4,5],[6,7,8,9]]
sum=[]
for i in range(len(l)):
  total=0
  for j in range(len(l[i])):
    total+=l[i][j]
  sum.append(total)  
print("sum of list elements in each list:",sum)
t=0  
for i in range(len(sum)):
   t+=sum[i]
print("sum of all values in the list is:",t)

#Print a nested list
l=[[1,2,3],[4,5],[6,7,8,9]]
for i in l:
  for j in i:
    print(j,end=" ")  
  print("\n")

#Flatten a nested list
old_list=[[1,2,3],[4,5],[6,7,8,9]]
new_list=[j for i in old_list for j in i]
print(new_list)

#Convert a nested list to a string
old_list=[[1,2,3],[4,5],[6,7,8,9]]
new_list=[j for i in old_list for j in i]
new=""
for i in new_list:
  x=str(i)
  new+=x
print(new)
print(type(new))

