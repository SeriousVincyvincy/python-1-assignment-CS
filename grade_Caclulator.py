#Variable Assignment
LabPP = int(input("Enter the number of labs completed: "))
if LabPP > 6:
    LabPP = 6
LabPPW = ((LabPP/6)*20)
Quizzes = int(input("Enter the number of quizzes completed: "))
if Quizzes > 6:
    Quizzes = 6
QuizzesW = ((Quizzes/6)*15)
Ass1 = float(input("Enter grade for Assignment 1: "))
Ass2 = float(input("Enter grade for Assignment 2: "))
Ass3 = float(input("Enter grade for Assignment 3: "))
Ass4 = float(input("Enter grade for Assignment 4: "))
AssAvg = ((Ass1 + Ass2 + Ass3 + Ass4)/4)
AssW = (AssAvg*0.16)
MidT1 = float(input("Enter grade for Midterm 1: "))
MidT2 = float(input("Enter grade for Midterm 2: "))
MidTAvg = ((MidT1 + MidT2)/2)
MidTW = ((MidTAvg)*0.25)
Final = float(input("Enter grade for Final exam: "))
FinalW = (Final*0.18)
MF_Prep = float(input("Enter grade for Midterms and Final Preparation: "))
MF_PrepW = (MF_Prep*0.06)
FINAL_GRADE = round((LabPPW + QuizzesW + AssW + MidTW + FinalW + MF_PrepW), 1)
print("Your Grade is: " + str(FINAL_GRADE))
