lstVariable = []
lstVariableNumber = []

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise ("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise ("Stack is empty")
        return self.data.pop()

def findIndex(lst, elem):
    counter = 0
    for i in lst:
        if i == elem:
            return counter
        counter += 1
    raise("ERROR")


#VARIABLE
userInput = input("-->")
firstTime = None
operations = "-+*/"
stack = ArrayStack()

#CONTROL VARIABLES:
newVariable = False
reAssign = False
while userInput != "done()":
    if firstTime is None:
        lstVariable = [] #WILL HOLD THE VARIABLE NAME
        lstVariableNumber = [] #HOLDS ASSOCIATED VARIABLE VALUE AT THE CORRESPONDING INDEX


    if userInput not in lstVariable:
        for i in userInput.split():
            if i not in operations and i not in lstVariable and i != "=":
                print("num", i)
                stack.push(i)
            #OPERATION CODE
            if i in operations and not stack.is_empty():
                print("op", i)
                second = int(stack.pop())
                first = int(stack.pop())
                if i == "+":
                    stack.push(first + second)
                elif i == "-":
                    stack.push(first - second)
                elif i == "*":
                    stack.push(first * second)
                elif i == "/":
                    stack.push(first / second)
            if i == "=":
                print(i)
                if not stack.is_empty():
                    #stack.pop()
                    lstVariable.append(stack.pop())
                    newVariable = True

            if (i in lstVariable and len(userInput) == 1) or (i in lstVariable and reAssign == True) or (i in lstVariable and newVariable == True):
                print("first: ", i)
                #Cndition: Size 1 = Return Variable #. If reassigning variable with the variable, push to stack the value. If assigning new variable with old variables
                #push the old variable values onto the stack to assign the new variable
                indexInVariable = findIndex(lstVariable, i)
                stack.push(lstVariableNumber[indexInVariable])
            elif i in lstVariable and len(userInput) > 1 and "=" in userInput:
                print("second: ", i)
                reAssign = True
                reAssignIndex = findIndex(lstVariable, i)
            if i in lstVariable and "=" not in userInput:
                print("third: ", i)
                stack.push(lstVariableNumber[findIndex(lstVariable, i)])


    if userInput in lstVariable:
            index = findIndex(lstVariable, userInput)
            print(lstVariableNumber[index])
    elif reAssign == True:
        lstVariableNumber[reAssignIndex] = stack.pop()
        print(lstVariable[reAssignIndex])
    elif newVariable == False and reAssign == False:
        print(stack.pop())
    elif newVariable == True:
        temp = stack.top()
        lstVariableNumber.append(stack.pop())
        indexVariable = findIndex(lstVariableNumber, temp)
        print(lstVariable[indexVariable])

    reAssign = False
    newVariable = False
    firstTime = False
    userInput = input("-->")