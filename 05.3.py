Age = int(input('Enter desired age: '))

if Age > -1 and Age <= 12:
    print ('Kid')
elif Age >= 13 and Age <= 17:
    print ('Teen')
elif Age == 18:
    print ('Debut')
else:
    print ('Adult')
