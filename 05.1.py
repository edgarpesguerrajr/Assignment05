def GradeRounded():
    Grade = float(input('Enter your grade percentage: '))
    RoundedGrade = round (Grade)
    return RoundedGrade

Grade = GradeRounded()

if Grade >= 97 and Grade <= 100:
    print ('Description: Excellent')
    print ('Grade/Mark: 1.0')

elif Grade >= 94 and Grade <= 96:
    print ('Description: Excellent')
    print ('Grade/Mark: 1.25')

elif Grade >= 91 and Grade <= 93:
    print ('Description: Very Good')
    print ('Grade/Mark: 1.5')

elif Grade >= 88 and Grade <= 90:
    print ('Description: Very Good')
    print ('Grade/Mark: 1.75')

elif Grade >= 85 and Grade <= 87:
    print ('Description: Good')
    print ('Grade/Mark: 2.0')

elif Grade >= 82 and Grade <= 84:
    print ('Description: Good')
    print ('Grade/Mark: 2.25')

elif Grade >= 79 and Grade <= 81:
    print ('Description: Satisfactory')
    print ('Grade/Mark: 2.5')

elif Grade >= 76 and Grade <= 78:
    print ('Description: Satisfactory')
    print ('Grade/Mark: 2.75')

elif Grade == 75:
    print ('Description: Passing')
    print ('Grade/Mark: 3.0')

else:
    Grade >= 65 and Grade <= 74
    print ('Description: Failure')
    print ('Grade/Mark: 5.0')