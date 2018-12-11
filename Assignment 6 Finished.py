#1. 
#An IDE usually has the ability to write code, compile, and debug (more specialized) while a notebook is more broad and usually just involves writing the code.
#Colab is a notebook and Spyder is an IDE.  I prefer Colab because I find it more easy to navigate since it's cleaner/less cluttered than Spyder.

#2.
print(2*3) #multiply 2 and 3
print(2**3) #raise 2 to the 3rd power/exponent
print(2/3) #2 divided by 3
print(2//3) #2 divided by 3, then round down to nearest whole number

#3
name=input('Enter name: ')
print('Hello ' + name)

#4
from math import pi
r=int(input('Enter radius of circle: '))
area=pi*r**2
print('The area is: ', area)

#5
from graphicslib import *
def main():
    win=GraphWin('questionFive', 500, 500)
    center=Point(250,250)
    c=Circle(center, 50)
    c.draw(win)
    win.getMouse()
    win.close()
main()

#6
#A string is a series of characters/words
#A list is a series of characters/words/numbers/strings, listed out to show each input
#A file is a text document that contains words/phrases/numbers that have been typed in Python
str1=('hello')
str2=('goodbye')
list=[str1, str2]
print(list)

#7
def openFile():
    file=open('S:\\file.txt','w+')
    file.writelines('hello\n')
    file.close()
    file2=open('S:\\file.txt','a')
    file2.writelines('goodbye')
    file2.close()
openFile()


#8
a=input('Enter a sentence: ')
words=a.split()
if len(words) < 5:
    print('This is a short sentence.')
else:
    print('This is a long sentence.')


#9
def main():
    sum = 0.0
    count = 0
    x = int(input("Enter a number (negative to quit) >> "))
    while x >= 0:
        sum = sum + x
        count = count + 1
        x = float(input("Enter a number (negative to quit) >> "))
    print("\nThe average of the numbers is", sum / count)
main()


#10 Boolean expressions are used to narrow results
b=int(input('Enter a number: '))
if (b <= 10) and (b >= 5):
    print('True')
else:
    print('False')
    
#11 Indentation signifies whether a line of code is part of a specific function or not, as well as part of a while loop/if statement
#12 Each .py file is a Python file you've saved
#13 The console window is good for debugging and testing and can be typed in without changing the overall code
#14 The variable explorer shows what variables you've defined in your code; file explorer shows what .py files you have saved; help tab allows you to get help on functions/variables by pressing CTRL+I over a piece of code
#15 A comment is any piece of code with a '#' in front of it (for single lines) or three single quotes in front of and after it (for multiple lines of code) and is used to keep lines from impacting your code or to clarify certain pieces of code

#16 A function can be called to perform certain actions in a code. You can call a specific function without variables by leaving the brackets empty (you still need the brackets)
# first code snippet
outFile=open('s:\\output1.txt')
outFile.writelines('a new line')
outFile.close
# second code snippet
outFile2=open('s:\\output2.txt')
outFile2.writelines('a new line')
outFile2.close()
#The first one won't work because it doesn't have brackets after 'close'; should be outFile.close()

#17 name=dog won't work; should be name='dog' to properly define the variable
#18 Selecting 'run cell' on a single line will just run that line and is useful because it lets you work on a single line at a time and helps with debugging

#19 
import mymodule
mymodule.myFunction()

