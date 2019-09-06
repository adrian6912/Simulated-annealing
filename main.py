'''
Created on Sep 26, 2018

@author: Adrian Ridder

CS461 Program2
'''

from random import randint
import Suite

if __name__ == '__main__':
    studentMatrix = []  ##The table from scores.txt will go here
    listOfSuites = []
    numberOfStudents = 200
    T = 500
    Itr = 1
    swaps = -1  ##Initialize these two values at -1 so that the 'big' while loop can execute based on these variables
    attempts = -1
    Max = 0
    Min = 0
    avg = 0
    
    with open('scores.txt', 'r') as f:  ##Create a 2 dimensional list s.t. list[student1][student2] gives us the compatibility of two students
        for line in f.readlines():
            studentMatrix.append(line.split(' '))
    
    t = 0
    for x in range(50): ##Assign students to rooms consecutively
        suite = Suite.Suite(t, t + 1, t + 2, t + 3, studentMatrix)
        t += 4
        listOfSuites.append(suite)
    while (swaps != 0 and attempts != 0):
        attempts = 0
        swaps = 0
        while ( (attempts < 20000 and swaps < 2000) ):
            room1 = randint(0, 49)
            room2 = randint(0, 49)
            while (room1 == room2):   ##Make sure they don't equal each other! That'd be dumb.
                room2 = randint(0, 49)
            x = Suite.evalSwap(listOfSuites[room1], listOfSuites[room2], T) ##List of 2 rooms and then a boolean
            if x[2] == True:            ##Count up the successful swaps and the unsuccessful attempts
                listOfSuites[room1] = x[0]  ##Set rooms equal to new rooms
                listOfSuites[room2] = x[1]
                swaps += 1
                attempts += 1
            elif x[2] == False:
                attempts += 1
        scoreList = []
        for room in listOfSuites:
            scoreList.append(room.score)
        for score in scoreList:
            avg += score
        avg /= 50
        Max = max(scoreList)
        Min = min(scoreList)
        printThis = "Itr {:} T = {:} Max = {:} Min = {:} Avg = {:} Att = {:} Swaps = {:}".format(Itr, T, Max, Min, avg, attempts, swaps)
        print(printThis)
        T *= .95
        Itr += 1
        