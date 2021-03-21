#: Chelsea Novo
#: This program is a quiz game for programming.
#: some of the things that helped me where the POGIL worksheets and prof, Vanselows class website.
print('Welcome coder, do you dare begin this quiz?')

# Gave true or false a value, so if the answer is incorrect then the value will not match up
word_true = 'true'
word_false = 'false'
print('The following questions will be true or false \n')

# Gave questions variable names so when used in if and else the program will know which question it is talking about.
# I utilized if and else so when the user inputs the answer it will only mark the right answer as right and anything
# else is wrong
t_f_1 = input('1.If you were to code: print (hello) * 20 ; hello would print 20 times: ')
if t_f_1 == word_false:
    print('correct')
else:
    print('incorrect')
t_f_2 = input('2. Would this line of code cause an error: 1apple= "1 apple", print(1apple)?')
if t_f_2 == word_true:
    print('correct')
else:
    print('incorrect')

# I now am introducing math formulas
print('The following contain math coding questions answer with integers ONLY \n')
m_1 = int(input('3. What is the output for this line of code: print(3**4) :'))

# I am not just utilizing the answer, but allowing the computer to do the math to eliminate human error.
if m_1 == 3**4:
    print('Nice!')
else:
    print('Not quite, ** is like using exponents ')
m_2 = int(input('4. What is the output for print(16//3): '))
if m_2 == 16//3:
    print('Good job!')
else:
    print('not quite // divides without remainder', end=' do not be sad you will get there \n')

m_3 = int(input('5. What is the output for print(20%3): '))
if m_3 == 20 % 3:
    print('Im running out of ways to say good job')
else:
    print('it be like that', end='not correct \n')

m_4 = int(input('6. What is the output for print(12//4-2**4: '))
if m_4 == 12//4-2**4:
    print('Wow your brain is amazing')
else:
    print('not right silly \n')
print('The following will be true or false')
# utilizing the if elif and else to remind user these are true or false questions
m_5 = input('7. Utilize -if- as a stand alone command, would it cause an error? ')
if m_5 == word_false:
    print("Correcto!!")
elif m_5 == word_true:
    print("Not quite")
else:
    print("not correct at all please remember these are true or false")
m_6 = input('8.The sign for equal is this =')
if m_6 == word_false:
    print("yay!!")
elif m_6 == word_true:
    print("not yay!!")
else:
    print("not correct format pal")
m_7 = input("9. 20 and 30 are not equal, would you use =! to code that?")
if m_7 != word_false:
    print("great job braniac! \n")
else:
    print('its okay in 5 more questions I will show you something cool, hold tight')
print("The following will be math questions again, integers only")
m_8 = int(input("10. What number is <10 and >8"))
if m_8 == m_8 < 10 and m_8 > 8:
    print("correct")
else:
    print('not so good')
m_9 = int(input('11. type 10'))
# utilizing while and not to simplify code and make it a little smoother
while m_9 is not 10:
    print("yikes")
else:
    print("you are a great listener or reader i guess")
m_10 = int(input("12. what is a number more than 10 OR less than 5"))
if m_10 == m_10 > 10 or m_10 < 5:
    print("you got some math in yah")
else:
    print("better luck next time")
m_11 = print("13. what number plus another number does not equals the first number")
total = 0
for x in range(2):
    number = int(input("Enter a number: "))
    total += number
if m_11 == total:
    print("niceeeee")
else:
    print("not so nice")
m_12 = int(input("if i gave you x= range (3,6) how many lines would the output have"))
x = range(1, 2)
for n in x:
    if m_12 == 3:
        print('mice are nice')
    elif m_12 != 3:
        print("mice not nice")

print("\n BRAIN BREAKKKKK IM GOING TO TURN YOUR NEGATIVES INTO POSITIVES!!! ")
def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number
print(absolute_value(int(input("number please"))))
print(absolute_value(int(input("number please"))))
