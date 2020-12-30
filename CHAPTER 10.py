#!/usr/bin/env python
# coding: utf-8

# CHAPTER 10 : FILES AND EXCEPTIONS

# In[1]:


#read a file

with open("pi.txt") as file_object:
    contents=file_object.read()
    print(contents)


# In[2]:


# read file line by line
with open ("pi.txt") as file_object:
    for  line in file_object:
        print(line)


# In[3]:


# make a list of lines from a file
with open("pi.txt") as file_object:
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())


# In[4]:


#working with a file's content
with open("pi.txt") as file_object:
    lines=file_object.readlines()
pi_string=' '
for line in lines:
    pi_string+=line.rstrip()
print(pi_string)
print(len(pi_string))


# In[5]:


birthday=input("Enter your bday in ddmmyy: ")
if birthday in pi_string:
    print("your bday appears")
else:
    print("nope, you're unlucky !")


# In[6]:


# 10.1
with open("learning_python.txt") as file_object:
    lines=file_object.read()
    print(lines)


# In[7]:


with open("learning_python.txt") as file_object:
    lines=file_object.readlines()
    for line in lines:
        print(line)


# In[8]:


#10.2
with open("learning_python.txt") as file_object:
    lines=file_object.read()
    print(lines.replace("python","C"))


# In[9]:


#writing into a new text file created by python
with open("programmimg.txt","w") as file_object:
    file_object.write("i love programming !")


# In[10]:


#writing multiplelines
with open("programmimg.txt","w") as file_object:
    file_object.write("i love programming !\n")
    file_object.write("i love creating new games !")


# In[11]:


#using append
with open("programmimg.txt","a") as file_object:
    file_object.write("\nusing ammend does not delete all previous data unlike write mode  !")


# In[12]:


# 10.3
user_name=input("Enter your name: ")
with open("guest.txt","w") as file_object:
    file_object.write(user_name.title())


# In[13]:


# 10.4
while True:
    name = input("enter your name, \nprint 'quit' to end.")
    if name=="quit":
        break
    else:
        with open("guest_book.txt","a") as file_object:
            file_object.write(name + " aya tha idhar! ")
        print(name+" , welcome you soab!")
    


# In[14]:


# 10.5
reason=' '
while reason !='quit':
    reason=input("why the hell do you like programming: ")
    with open("reasonswhypeoplelikeprogrammimg.txt","a") as f:
        f.write(reason)
    print("response recorded !")
#do this like 10.4


# In[16]:


# handling errors
# using try-except blocks
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero !")


# In[18]:


print("give 2 numbers and i'll divide them")
print("Enter 'q' to exit")

while True:
    n1=input("\nFirst Number")
    if n1=="q":
        break
    n2=input("\nSecond number: ")
    if n2=="q":
        break
    answer=int(n1)/int(n2)
    print(answer)


# In[22]:


print("give 2 numbers and i'll divide them")
print("Enter 'q' to exit")

while True:
    n1=input("\nFirst Number")
    if n1=="q":
        break
    n2=input("\nSecond number: ")
    if n2=='q':
        break
    try:
        answer=int(n1)/int(n2)
    except ZeroDivisionError:
        print("You can't divide by 0 idiot!")
    else:
        print(answer)


# In[2]:


# handling file not  found error
try:
    with open("alice.txt") as f:
        contents=f.read()
except FileNotFoundError:
    print("nhi mili")


# In[7]:


# 10.6
print("enter 2 numbers to add")
f1=input("enter 1st number: ")
f2=input("enter 2nd number: ")

try:
    f1=int(f1)
    f2=int(f2)
except ValueError:
    print("enter a 'number'")
else:
    print(f1+f2)


# In[2]:


# 10.7
print("press 'q' to quit.")
while True:
    try:
        x=input("enter 1st number")
        if x=="q":
            break
        y=input("enter 2nd number")
        if y=="q":
            break
    except ValueError:
        print("enter a number")
    else:
        print(int(x)+int(y))


# In[10]:


# 10.8
file_name="cats.txt"
try:
    with open(file_name) as f1:
        contents=f1.read()
        print(contents)
except FileNotFoundError:
    print("nhi mili")


# In[12]:


# 10.9 
file_name="cats1.txt"
try:
    with open(file_name) as f1:
        contents=f1.read()
        print(contents)
except FileNotFoundError:
    pass


# In[1]:


import json
numbers=[5,6,8,9,5]
with open("numbers.json","w") as f:
    json.dump(numbers,f)


# In[3]:


import json
with open("numbers.json") as f:
    num=json.load(f)
print(num)


# In[7]:


import json
username=input("Enter your name: ")
with open("username.json","w") as f:
    json.dump(username,f)
    print("we will remameber your name"+username)
    


# In[9]:


import json
with open("username.json") as f:
    user=json.load(f)
print("told ya "+user)


# In[10]:


# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
import json
filename="username.json"
try:
    with open(filename) as f:
        user=json.load(f)
    print("we remember ya "+user)
except FileNotFoundError:
    username=input("Enter your name: ")
    with open(filename,"w") as f:
        json.dump(username,f)
    print("we will remameber your name "+username)
else:
    print("welcome back "+user)


# In[11]:


import json
filename="username1.json"
try:
    with open(filename) as f:
        user=json.load(f)
    print("we remember ya "+user)
except FileNotFoundError:
    username=input("Enter your name: ")
    with open(filename,"w") as f:
        json.dump(username,f)
    print("we will remameber your name "+username)
else:
    print("welcome back "+user)


# In[12]:


import json
def greet_user():
    try:
        with open(filename) as f:
            user=json.load(f)
        print("we remember ya "+user)
    except FileNotFoundError:
        username=input("Enter your name: ")
        with open(filename,"w") as f:
            json.dump(username,f)
        print("we will remameber your name "+username)
    else:
        print("welcome back "+user)
greet_user()


# In[3]:


# 10.11
import json
filename="fav_num.json"
fav_number=input("enter your fav number: ")
with open(filename,"w") as f:
    json.dump(fav_number,f)
        


# In[5]:


import json
filename="fav_num.json"
with open(filename) as f:
    x=json.load(f)
print("I know your favorite number! It’s "+x)


# In[9]:


# 10.12
import json
try:
    filename="fav_num2.json"
    with open(filename) as f:
        x=json.load(f)
except FileNotFoundError:
    filename="fav_num2.json"
    fav_number=input("enter your fav number: ")
    with open(filename,"w") as f:
        json.dump(fav_number,f)
    print("i will remeber that you fav num is"+fav_number)
else:
    print("I know your favorite number! It’s "+x)
    
    


# In[10]:


import json
try:
    filename="fav_num22.json"
    with open(filename) as f:
        x=json.load(f)
except FileNotFoundError:
    filename="fav_num22.json"
    fav_number=input("enter your fav number: ")
    with open(filename,"w") as f:
        json.dump(fav_number,f)
    print("i will remeber that you fav num is"+fav_number)
else:
    print("I know your favorite number! It’s "+x)
    


# In[26]:


#10.13
def get_stored_username():
    filename="user301.json"
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    filename='user301.json'
    username=input("enter your name: ")
    with open(filename,"w") as f:
        json.dump(username,f)
    print("i will remember you "+username)
    
    
def greet_user():
    username=get_stored_username()
    if username:
        test=input("is your name(y/n) "+username)
        if test=="y":
            print("welcome back "+username)
        else:
            username=get_new_username()
            print("we'll remeber you "+username)
    else:
        username=get_new_username()
       
        
    


# In[27]:


greet_user()


# In[28]:


def get_stored_username():
    filename="user302.json"
    try:
        with open(filename) as f:
            username=json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    filename='user302.json'
    username=input("enter your name: ")
    with open(filename,"w") as f:
        json.dump(username,f)
    print("i will remember you "+username)
    
    
def greet_user():
    username=get_stored_username()
    if username:
        test=input("is your name(y/n) "+username)
        if test=="y":
            print("welcome back "+username)
        else:
            username=get_new_username()
            print("we'll remeber you "+username)
    else:
        username=get_new_username()
       
    
greet_user()


# In[ ]:




