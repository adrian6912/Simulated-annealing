'''
Created on Sep 26, 2018

@author: Adrian Ridder
'''
from math import sqrt, exp
from random import randint, random
from copy import copy


class Suite(object):
    '''
    Class that represents each room. Attributes include which students are in the room and the room's score
    '''
    def __init__(self, stud1, stud2, stud3, stud4, studentMatrix):
        '''
        Constructor
        '''
        self.studMatrix = studentMatrix
        self.studentList = [stud1, stud2, stud3, stud4]  ##Each student value is the index of that student within the studentMatrix
        self.score = 0
        self.calculateRMS()
        
    def calculateRMS(self):
        '''sets the suite's compatibility score'''
        total = 0
        total += (int(self.studMatrix[self.studentList[0]][self.studentList[1]]) ** 2) 
        total += (int(self.studMatrix[self.studentList[0]][self.studentList[2]]) ** 2)
        total += (int(self.studMatrix[self.studentList[0]][self.studentList[3]]) ** 2)
        total += (int(self.studMatrix[self.studentList[1]][self.studentList[2]]) ** 2)
        total += (int(self.studMatrix[self.studentList[1]][self.studentList[3]]) ** 2)
        total += (int(self.studMatrix[self.studentList[2]][self.studentList[3]]) ** 2)
        self.score = sqrt( total / 6 )      
        return
        
def randSwap(suite1, suite2):
    '''Randomly swaps one student from the first suite with another from the second suite'''
    ind1 = randint(0, 3)
    ind2 = randint(0, 3)
    student1Copy = copy(suite1.studentList[ind1])
    student2Copy = copy(suite2.studentList[ind2])
    suite1.studentList[ind1] = student2Copy
    suite2.studentList[ind2] = student1Copy
    suite1.calculateRMS()   ##Reset each room's score
    suite2.calculateRMS()
    return
    
def evalSwap(suite1, suite2, T):
    '''Essentially, should I actually do the swap or not?'''
    ##Get copies of the original suites
    newSuite1 = Suite(suite1.studentList[0], suite1.studentList[1], suite1.studentList[2], suite1.studentList[3], suite1.studMatrix)
    newSuite2 = Suite(suite2.studentList[0], suite2.studentList[1], suite2.studentList[2], suite2.studentList[3], suite2.studMatrix)
    ##Do random swap of the rooms
    randSwap(newSuite1, newSuite2)
    oldscore = suite1.score + suite2.score
    newscore = newSuite1.score + newSuite2.score
    ##Immediately return the newscore if it's better
    if newscore < oldscore:
        return [newSuite1, newSuite2, True] ##Add third element to the returned list that says if a swap happened or not
    ##The newscore might still be better, so we do some probability! Yay!
    else:
        prob = exp(-(newscore - oldscore) / T)
        if random() < prob:
            return [newSuite1, newSuite2, True]
        else:
            return [suite1, suite2, False]
    
    
    
    
    
    
    
    
    
    
    
    