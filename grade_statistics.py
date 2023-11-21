# Write your solution here
import math

def userInput():
    inputList = []
    while True:
        printInput = input("Exam points and exercises completed:")
        inputList.append(printInput.split())
        if printInput == "":
            inputList = inputList[:-1]
            #print(inputList)
            return inputList
            break

def examPoints(inputList):
    examPointsList = []
    for value in inputList:
        examPointsList.append(int(value[0]))
    #print(examPointsList)
    return examPointsList

def exercisePoints(inputList):
    pointsList = []
    for value in inputList:
        exercisePoints = int(value[1])
        exercisePoints = math.floor(exercisePoints/10)
        pointsList.append(exercisePoints)
    #print(pointsList)
    return pointsList

def totalPoints(examPoints, exercisePoints):
    totalPointsList = [x + y for x, y in zip(examPoints, exercisePoints)]
    #print(totalPointsList)
    return totalPointsList

def pointsAverage(totalPoints):
    sum = 0
    for i in totalPoints:
        sum += i
    average = sum/(len(totalPoints))
    averageRounded = round(average, 1)
    return averageRounded

def passPercentage(examPoints, totalPoints):
    numberFailed = 0
    i = 0
    while i < len(totalPoints):
        if examPoints[i] < 10 or totalPoints[i] < 15:
            numberFailed += 1
        i += 1
    students = len(totalPoints)
    passPercent = ((students - numberFailed) / students)*100
    passPercent = round(passPercent, 1)
    return passPercent

def gradeDistList(examPoints, totalPoints):
    grade0 = 0
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0

    i = 0
    while i < len(totalPoints):
        if examPoints[i] >= 10:
            if 0 <= totalPoints[i] < 15:
                grade0 += 1
            if 15 <= totalPoints[i] < 18:
                grade1 += 1
            if 18 <= totalPoints[i] < 21:
                grade2 += 1
            if 21 <= totalPoints[i] < 24:
                grade3 += 1
            if 24 <= totalPoints[i] < 28:
                grade4 += 1
            if 28 <= totalPoints[i] <= 30:
                grade5 += 1
        else:
            grade0 += 1
        i += 1
    gradeList = [grade0, grade1, grade2, grade3, grade4, grade5]
    #print(gradeList)
    return gradeList

def gradeDistribution(gradeDistList):
    starList = []
    for value in gradeDistList:
        starList.append(value*"*")
    #print(starList)

    lineList = []
    i = 0
    while i < 6:
        lineList.append(f"  {5-i}: {starList[5-i]}")
        i += 1
    return lineList


def main():
    inputFromUser = userInput()
    examP = examPoints(inputFromUser)
    exerP = exercisePoints(inputFromUser)
    totalP = totalPoints(examP, exerP)
    pointAvg = pointsAverage(totalP)
    passP = passPercentage(examP, totalP)
    gradeList = gradeDistList(examP, totalP)
    gradeDist = gradeDistribution(gradeList)

    print("Statistics:")
    print(f"Points average: {pointAvg}")
    print(f"Pass percentage: {passP}")
    print("Grade distribution:")
    for value in gradeDist:
        print(value)

main()