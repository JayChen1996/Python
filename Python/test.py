'''
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday,in the form mmddyy:")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("YOur birthday does not appear in the first million digits of pi"
'''

'''
filename = "pidigits.txt"
with open(filename) as file_object:
    filecontent = file_object.read()

print(filecontent)
file_rows = []
with open(filename) as file_object:
    for c in file_object:
        file_rows.append(c)

for file_row in file_rows:
    print(file_row)

'''
'''
写入文件
filename = "programming.txt"

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets")
    file_object.write("I love creating apps that can run in a browser.")
'''

'''
guest_name = input("please input your name")

filename = "guest.txt"

with open(filename,'w') as file_object:
    file_object.write(guest_name)
'''

'''
写入文件
filename = 'guest_book.txt'

file_content = ""

while True:
    guest_name = input("please input your name")
    if guest_name != 'stop':
        file_content += guest_name+'\n'
    else:
        break

with open(filename,'w') as file_object:
    file_object.write(file_content)
'''

'''
异常处理
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
'''

'''
异常处理
print("Give me two numbers,and I will divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break

    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)

'''

'''
文件未找到异常
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sory, the file "+filename+" does not exit."

print(msg)
'''

'''
分析书中有多少个单词
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sory, the file "+filename+" does not exit."
    print(msg)
else:
    #计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file "+filename+" has about "+str(num_words)+" words.")
'''

'''
def count_words(filename):
    """计算文件大致包含多少单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sory, the file "+filename+" does not exit."
        print(msg)
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")


count_words('alice.txt')
'''

'''
print("helloworld")
'''
'''
try:
    while True:
        num1 = input("please input number1:\n")
        num2 = input("please input number2:\n")
        print("the value is "+str(int(num1)+int(num2)))
except TypeError:
        print("input number please")
except ValueError:
        print("ValueError")
'''
'''
filename = 'flowers.txt'

try:
    with open(filename) as cat_file:
        cat_log = cat_file.readlines()
    for c in cat_log:
        print(c)
except FileNotFoundError:
    pass
'''

'''
统计文件中the的数量
def count_the(filename):
    with open(filename) as file_object:
        file = file_object.read()
    words = file.split()
    count = 0
    for word in words:
        if word.lower() == 'the':
            count += 1
    return count

print(count_the('life_and_adventures.txt'))
'''
'''
import json

numbers = [2,3,5,7,11,13]

filename = 'numbers.json'

with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)


with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)

username = input("What is your name")
filename = 'username.json'
with open(filename,'w') as f_obj:
    json.dump(username,f_obj)
    print("We'll remember you when you come back,"+username+"!")

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcom back,"+username+"!")
'''

'''
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
 

while True:
   for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
'''    

'''

#绘制折线图
import matplotlib.pyplot as plt


input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.plot(input_values,squares,linewidth=5)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.tick_params(axis='both',labelsize=14)
plt.show()

'''


'''
import matplotlib.pyplot as plt
#绘制散点图

x_values = list(range(1,1001))
y_values = [value*value for value in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=40)
#plt.axis([0,1100,0,1100000])
plt.tick_params(axis='both',which='major')
plt.savefig('squares_plot.png',bbox_inches='tight')

'''

'''
#绘制立方散点图,颜色映射，c是一个列表而且大小需要和点的个数相同

import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [value**3 for value in x_values]
c_test = list(range(1,5000))

plt.scatter(x_values,y_values,c=c_test,cmap=plt.cm.gist_rainbow)
plt.show()
'''


'''
#随机漫步
import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
    def __init__(self,num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([1,-1])
        distance = choice([-1,-3,4,8])
        return direction*distance
 

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.figure(figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values,rw.y_values,lineWidth=1)

    plt.scatter(0,0,c='green',edgecolor='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',s=100)
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.show()
'''

'''
#pygal 的使用
from random import randint
import pygal

class Dice():
    def __init__(self,num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        #randint(a,b)  return  n, a <= n <= b
        return randint(1,self.num_sides)


dice_1 = Dice()
dice_2 = Dice(10)

results = []
for roll_num in range(1000):
    results.append(dice_1.roll()+dice_2.roll())

frequencies = []
max_result = dice_1.num_sides + dice_2.num_sides

for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = [str(value) for value in range(2,17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')

'''
'''
import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,highs = [],[]

    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        dates.append(current_date)

        high =int(row[1])
        highs.append(high)

fig = plt.figure(dpi=128)
plt.plot(dates,highs,c='red')

plt.title("Daily high temperatures,July 2014",fontsize=1)
plt.xlabel("fontsize=16")
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
 
plt.show()
'''

'''
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:",r.status_code)
response_dict = r.json()
print("Total reposities:",response_dict['total_count'])

repo_dicts = response_dict['items']

names,stars = [],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

my_style = LS("#333366",base_style=LCS)
#show_legend=False 隐藏图例
chart = pygal.Bar(style=my_style,x_label_rotation=45,show_legend=True)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels=names
#第一个参数是图例名列表
chart.add(",",stars)
chart.render_to_file('python_repos.svg')

'''
'''
import requests
from bs4 import BeautifulSoup

url = 'http://music.163.com/#/song?id=64312'

response = requests.get(url)

html_doc = response.text
soup = BeautifulSoup(html_doc)

print(soup.find_all('em','f-ff2'))

'''

'''
import json
import os
import os.path
import requests
from bs4 import BeautifulSoup

dirPath = '/media/jaychen/WIN10/Users/JayChen/AppData/Local/Netease/CloudMusic/webdata/lyric'
lyrics_path = dirPath+'/lyrics'
if os.path.exists(lyrics_path) == False:
    os.mkdir(lyrics_path)

def format_lyricfile(filepath,dirpath):
    with open(filepath) as file_obj:
        json_data = json.load(file_obj)

    #从网页中获取文件名
    filename = filepath.split('/')[-1]
    url = 'http://music.163.com/#/song?id='+filename

    response = requests.get(url)

    print(response.text)

    soup = BeautifulSoup(response.content,'html.parser')
    song_name = soup.find('div',class_='tit')

    with open(lyrics_path+'/song_name','w') as lyric:
        for lyric_row in song_lyric.split('\n'):
            lyric.write(lyric_row+"\n")




#parent 父目录 dirnames 所有文件夹名(不含路径) filenames 所有文件名
for parent,dirnames,filenames in os.walk(dirPath):
    for filename in filenames:
        format_lyricfile(dirPath+'/'+filename,dirPath)
'''
'''
#GUI Python
import tkinter

top = tkinter.Tk()
top.minsize(200,250)
text = tkinter.Entry()
text.pack()

top.mainloop()

'''

from tkinter import *
#创建一个root控件,根窗口，需要在其他控件之前创建
#一个窗口只能有一个root控件
root = Tk()
w1 = Label(root)
explanation = """At present, only GIF and PPM/PGM 
formats are supported, but an interface  
exists to allow additional image file 
formats to be added easily."""

w2 = Label(root,justify=LEFT,padx=10,text=explanation).pack(side='left')

root.mainloop()










