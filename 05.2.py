def FirstSecondThird():
    FirstNumber = int(input("ENTER YOUR FIRST NUMBER: "))
    SecondNumber = int(input("ENTER YOUR SECOND NUMBER: "))
    ThirdNumber = int(input("ENTER YOUR THIRD NUMBER: "))
    return FirstNumber, SecondNumber, ThirdNumber


def UnoDosTres(First, Second, Third):
    if First < Second and First < Third:
        Min = First 

    elif Second < First and Second < Third:
        Min = Second

    elif Third < First and Third < Second:
        Min = Third

    return Min

First, Second, Third = FirstSecondThird()
Min = UnoDosTres(First, Second, Third)
print (f'The lowest number to {First}, {Second}, {Third} is {Min}.')