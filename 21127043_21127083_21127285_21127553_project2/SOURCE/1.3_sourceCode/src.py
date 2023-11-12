import sys
import queue
import math

dataMap = dict()
dataType = list()
personMap = dict()
questionList = list()

data_input = 'input.txt'
question_input = 'question.txt'

if len(sys.argv) >= 2:
    data_input = sys.argv[1]
    if len(sys.argv) >= 3:
        question_input = sys.argv[2]
    else: 
        print('input question file: ', end = '')
        question_input = input()
else:
    print('input data file: ', end = '')
    data_input = input()
    print('input question file: ', end = '')
    question_input = input()
    
with open(data_input) as f:
    while currentLine := f.readline():
        currentLine = currentLine[:-1].lower().replace(" ", "")
        if not len(currentLine): continue
        if '%' in currentLine:
            currentLine = currentLine[1:]
            dataType.append(currentLine)
            dataMap.update({currentLine: []})
        else:
            currentLine = currentLine[currentLine.find("(") + 1 : currentLine.find(")")]
            # currentLine = currentLine.split(',')
            dataMap[dataType[-1]].append(currentLine)

with open(question_input) as f:
    while currentLine := f.readline():
        currentLine = currentLine[:-1].lower().replace(" ", "")
        currentLine = currentLine.split('(')
        currentLine = [currentLine[0]] + currentLine[1].split(',')
        currentLine[2] = currentLine[2].split(')')[0]
        questionList.append(currentLine)

class Person:
    def __init__(self, name : str, gender, mate = []):
        self.name = name
        self.gender = gender

        self.father = None
        self.mother = None
        self.mate = None
        self.ex = list()

    def isMale(self):
        return self.gender == 'male'

    def setFather(self, father):
        self.father = father

    def setMother(self, mother):
        self.mother = mother

    def setMate(self, other):
        self.mate = other
    def addEx(self, other):
        self.ex.append(other)

for individual in dataMap['male']:
    personMap.update({individual : Person(individual, 'male')})
    
for individual in dataMap['female']:
    personMap.update({individual : Person(individual, 'female')})

try: 
    for item in dataMap['parent']:
        parent, child = item.split(',')
        if parent in dataMap['male']:
            personMap[child].setFather(personMap[parent])
        else:
            personMap[child].setMother(personMap[parent])
except Exception: pass

try:
    for item in dataMap['married']:
        husband, wife = item.split(',')
        personMap[husband].setMate(personMap[wife])
        personMap[wife].setMate(personMap[husband])
except Exception: pass

try:
    for item in dataMap['divorced']:
        husband, wife = item.split(',')
        personMap[husband].addEx(personMap[wife])
        personMap[wife].addEx(personMap[husband])
except Exception: pass

relationBoard = dict()

for individual_l in personMap:
    for individual_r in personMap:
        relationBoard.update({(individual_l, individual_r) : -1})

def bfs(start):
    global personMap
    global relationBoard
    bfsQueue = queue.Queue()
    bfsQueue.put([personMap[start], 0])

    while not bfsQueue.empty():
        current = bfsQueue.get()
        people = current[0]
        if people == None: continue
        step = current[1]
        relationBoard[(start, people.name)] = step
        
        bfsQueue.put([people.father, step + 1])
        bfsQueue.put([people.mother, step + 1])
        
for individual in personMap:
    bfs(individual)


#CREATE PROBLEM:

# QUESTION ANSWERING:

# DIRECTLY -> self, parent, grandparent (0, 1, 2)
# Throught 2 subnode -> nibling, aunt (0, 1) max = 2
# Throught 1 subnode -> sibling (0) max = 1
# OTHER : STRANGER

def check(person1, person2):
    state = 0
    distance = 250
    middleMan = None

    for individual in personMap:
        if relationBoard[(person1, individual)] < 0 or relationBoard[(person2, individual)] < 0:
            continue
        maxDistance = max(relationBoard[(person1, individual)], relationBoard[(person2, individual)])
        if (maxDistance >= distance): continue
        distance = maxDistance
        state = - (relationBoard[(person1, individual)] - relationBoard[(person2, individual)])
        middleMan = individual

    if middleMan is None:
        if (personMap[person1].mate is not None):
            if (personMap[person1].mate.name == person2): return "Partner"
        if (personMap[person1] in personMap[person2].ex): return "Ex"
        return "Stranger"

    if middleMan == person1 or middleMan == person2:
        if state > 1: return "Grandparent"
        if state < -1: return "Grandchild"
        if state == 1: return "Parent"
        if state == -1: return "Child"

    if distance == 1:
        return "Sibling"

    if state > 1: return "Grandparent"
    if state == 1: return "Aunt/Uncle"
    if state == -1: return "Nibling"
    if state < -1: return "Grandchild"
    return "Cousin"

def relationDefine(person, relation):
    if personMap[person].isMale():
        if relation == 'grandparent': return 'grandfather'
        if relation == 'parent': return 'father'
        if relation == 'sibling': return 'brother'
        if relation == 'nibling': return 'nephew'
        if relation == 'aunt/uncle': return 'uncle'
        if relation == 'child': return 'son'
        if relation == 'grandchild': return 'grandson'
        if relation == 'partner': return 'husband'
    else:        
        if relation == 'grandparent': return 'grandmother'
        if relation == 'parent': return 'mother'
        if relation == 'sibling': return 'sister'
        if relation == 'nibling': return 'niece'
        if relation == 'aunt/uncle': return 'aunt'
        if relation == 'child': return 'daugther'
        if relation == 'grandchild': return 'granddaughter'
        if relation == 'partner': return 'wife'
    return relation

def findX(person, relation, flip = False):
    for individual in personMap:
        if not flip:
            currelation = check(person, individual).lower()
            if relationDefine(individual, currelation) == relation or currelation == relation:
                return individual
        else:
            currelation = check(individual, person).lower()
            if relationDefine(person, currelation) == relation or currelation == relation:
                return individual
    return "Can't find!"

for question in questionList:
    # try:
        person1, person2 = question[1:]
        if person1 == 'x': 
            print(findX(person2, question[0]))
        elif person2 == 'x':
            print(findX(person1, question[0], True))
        else:
            relation = check(person1, person2).lower()
            # print(relation, end=': ')
            print(question[0] == relationDefine(person1, relation) or question[0] == relation)
    # except Exception:
    #     print(False)