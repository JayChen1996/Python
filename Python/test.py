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
