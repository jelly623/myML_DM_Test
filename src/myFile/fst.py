# __*__ coding: utf-8 __*__

letter = "chenweiting"
for i in letter:
    print (i)

a = "chenweiting"
if "d" in a:
    print (True)
else:
    print (False)

def mianji(x,y):
    z = x * y
    print (z)
mianji(3,6)


############################     4.6 推导式     ####################################
################################   列表推导式   ####################################
data = [ i for i in range(1,100) ]
print (data)
data2 = [ t for t in range(1,100) if t % 2 == 0 and t % 3 != 0 ]
print (data2)
data3 = { t for t in range(1,10)}
print (data3)
number_list = [number + 1 for number in range(1,6)]
print (number_list)

rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols]
for cell in cells:
    print (cells)
for row,col in cells:
    print (row,col)
################################   字典推导式   ###################################
word = "charestics"
letter_counts = {letter: word.count(letter) for letter in word }
print (letter_counts)
letter_counts = {letter:word.count(letter) for letter in set(word)}
print (letter_counts)
################################   集合推导式   ###################################
a_set = {number for number in range(1,6) if number % 3 == 1}
print (a_set)
number_thing = (number for number in range(1, 6))
for t in number_thing:
    print (t)
############################     4.4 循环     ####################################
count = 1
while count <= 5:
    print(count)
    count += 1
############################     break 跳出循环   ################################
'''
while True:
    stuff = input("string to capitalize [q to quit]:" )
    if stuff == "q":
        break
    print(stuff.capitalize())
'''
############################     continue 跳到循环开始   ################################
'''
while True:
    value = input("integer, please [q to quit]" )
    if value == "q":
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print (number, "squared is",number * number)
'''

numbers = [8,2,6]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0 :
        print("found even number",number)
        break
    position += 1
else:
    print("no even number found")


j = 1
a = 1
while j < 3:
    for i in range(3):
        print (i)
        a = a + 1
        continue
    j = j + 1
print(i,j,a)

##########################################################################
import math
def cosin(param):
    print(math.cos(param))
cosin(5)

def apple(color = ""):
    if color == "red":
        print ("it's a ",color ,"apple")
    if color == "blue":
        print("it's a ",color ,"apple")
    else:
        print("it's a green apple")
apple("a")
apple()

'''
def num(*p):
    a = len(p)
    return a
p = [1,2,3,4,5]
'''

class person():
    def speak(self,word):
        print (word)
    def walk(self,step):
        print (step)
a = person()
a.speak("hi")

def min(a,b,c):
    if a < b:
        temp = a
    else:
        temp = b
    if temp < c:
        print(temp)
        return temp
    else:
        print(c)
        return c
mini = min(6,8,0)
