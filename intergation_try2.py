# Chelsea Novo
# This program is a quiz game for programming.
# some of the things that helped me where the POGIL worksheets and prof, Vanselows class website.
# Ctrl + Alt + L
"""Welcome coder, do you dare begin this quiz?"""
def main():
    """
The following questions will be true or false
    """
    if __name__ == "__main__":
        main()
# Gave true or false a value, so if the answer is incorrect then the value will not match up


word_true = 'true'
word_false = 'false'
# Gave questions variable names so when used in if and else the program will know which question it is talking about.
# I utilized if and else so when the user inputs the answer it will only mark the right answer as right and anything
# else is wrong
t_f_1 = input('1.If you were to code: print (hello) * 20 ; hello would print 20 times: ')
if t_f_1 == word_false:
    print('correct')
elif t_f_1 == word_true:
    print('incorrect')
else:
    print("Please try again and use true or false")

t_f_2 = input('2. Would this line of code cause an error: 1apple= "1 apple", print(1apple)?')
if t_f_2 == word_false:
    print('correct')
elif t_f_2 == word_true:
    print('incorrect')
else:
    print("Please try again and use true or false")

# I now am introducing math formulas
print('The following contain math coding questions answer with integers ONLY \n')

# I am not just utilizing the answer, but allowing the computer to do the math to eliminate human error.
while True:
    try:
        m_1 = int(input('3. What is the output for this line of code: print(3**4) :'))
        if m_1 == 3**4:
            print('nice')
            break
        else:
            print("incorrect")
            break
    except ValueError:
        print('need whole number')
        continue
# utilizing while true in order to make sure user follows instructions
# try and except along with breaks to make sure the question continues even integers occur
# along with stopping with with value error making the project robust
while True:
    try:
        m_2 = int(input('4. What is the output for print(16//3): '))
        if m_2 == 16 // 3:
            print('nice')
            break
        else:
            print('incorrect')
            break
    except ValueError:
        print('need whole number')

while True:
    try:
        m_3 = int(input('5. What is the output for print(20%3): '))
        if m_3 == 20 % 3:
            print('nice')
            break
        else:
            print('Incorrect')
            break
    except ValueError:
        print("need whole number")

while True:
    try:
        m_4 = int(input('6. What is the output for print(12//4-2**4: '))
        if m_4 == 12 // 4 - 2 ** 4:
            print('Wow your brain is amazing')
            break
        else:
            print('not right silly \n')
            break
    except ValueError:
        print("need whole number")
print('The following will be true or false')
# utilizing while true in order to use str, this is to make sure the user is not entering numbers
while True:
    try:
        m_5 = str(input('7. Utilize -if- as a stand alone command, would it cause an error? '))
        if m_5 == word_false:
            print("Correcto!!")
            break
        else:
            print("not correct at all please remember these are true or false")
            break
    except ValueError:
        print("give me true or false")

while True:
    try:
        m_6 = str(input('8.The sign for equal is this ='))
        if m_6 == word_false:
            print("yay!!")
            break
        else:
            print("incorrect")
            break
    except ValueError:
        print("true or false")

while True:
    try:
        m_7 = str(input("9. 20 and 30 are not equal, would you use =! to code that?"))
        if m_7 != word_false:
            print("great job braniac! \n")
            break
        else:
            print('its okay in 5 more questions I will show you something cool, hold tight')
    except ValueError:
        print("true or false")
# allowing the user to know these are math questions
print("The following will be math questions again, integers only")
while True:
    try:
        m_8 = int(input("10. What number is <10 and >8"))
        if m_8 == m_8 < 10 and m_8 > 8:
            print("correct")
            break
        else:
            print('not so good')
            break
    except ValueError:
        pritn('Make sure it is an a whole integer')
while True:
    try:
        m_9 = int(input('11. type 10'))
# utilizing while and not to simplify code and make it a little smoother
        if m_9 != 10:
            print("yikes")
        else:
            print("you cannot read I guess")
    except ValueError:
        print("number please")

while True:
    try:
        m_10 = int(input("12. what is a number more than 10 OR less than 5"))
        if m_10 == m_10 > 10 or m_10 < 5:
            print("you got some math in yah")
        else:
            print("better luck next time")
    except ValueError:
        print("whole number please")
while True:
    try:
        m_11 = int(input("13. what number plus another number does not equals the first number"))
        total = 0
        for x in range(2):
            number = int(input("Enter a number: "))
            total += number
        if m_11 == total:
            print("nice")
            break
        else:
            print("not so nice")
            break
    except ValueError:
        print("whole number please")
while True:
    try:
        m_12 = int(input("14.if i gave you x= range (3,6) how many lines would the output have"))
        x = range(1, 2)
        for n in x:
            if m_12 == 3:
                print('mice are nice')
                break
            elif m_12 != 3:
                print("mice not nice")
                break
    except ValueError:
        print("number please")
print("you finished this quiz")

# utilizing def to define a function

def endofquiz():
    """
This ends the quiz saying bye
    """
    bye_coder = "Bye dear coder, wow I really had to try for this quiz so please appreciate"
    print(bye_coder)

# function is returning parameter
endofquiz()