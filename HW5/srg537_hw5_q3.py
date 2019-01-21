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

# def findIndex(lst, elem):
#     counter = 0
#     for i in lst:
#         if i == elem:
#             return counter
#         counter += 1
#     raise("ERROR")

lstVariable = []
lstVariableNumber = []
userInput = input("Please Enter Arithmetic and enter Finished when done: ")
first = None
var = dict()

op = ['*','+','/','-']
values = ArrayStack()
newVariable = False
reAssign = False

while userInput != "Finished":
    if first is None:
        lstVariable = [] #WILL HOLD THE VARIABLE NAME
        lstVariableNumber = [] #HOLDS ASSOCIATED VARIABLE VALUE AT THE CORRESPONDING INDEX
        var = dict()

    if userInput not in var:
        for i in userInput.split():
            # Push the numbers to the values
            if i not in op and i not in var and i != "=":
                values.push(i)

            # opetations with numbers
            if i in op and not values.is_empty():
                second = int(values.pop())
                first = int(values.pop())
                if i == "+":
                    values.push(first + second)
                elif i == "-":
                    values.push(first - second)
                elif i == "*":
                    values.push(first * second)
                elif i == "/":
                    values.push(first / second)
                if i == "=":
                    if not values.is_empty():
                        var = {'x': values.pop()}
                        newVariable = True

    #         if (i in var and len(userInput) == 1) or (i in var and reAssign == True) or (i in var and newVariable == True):
    #             #Cndition: Size 1 = Return Variable #. If reassigning variable with the variable, push to values the value. If assigning new variable with old variables
    #             #push the old variable values onto the values to assign the new variable
    #             indexInVariable = var.get(i)
    #             values.push(var[indexInVariable])
    #         elif i in var and len(userInput) > 1 and "=" in userInput:
    #             reAssign = True
    #             reAssignIndex = var.get(i)
    #         if i in lstVariable and "=" not in userInput:
    #             values.push(lstVariableNumber[findIndex(lstVariable, i)])
    #
    #
    # if userInput in lstVariable:
    #         index = findIndex(lstVariable, userInput)
    #         print(lstVariableNumber[index])
    # elif reAssign == True:
    #     lstVariableNumber[reAssignIndex] = values.pop()
    #     print(lstVariable[reAssignIndex])
    # elif newVariable == False and reAssign == False:
    #     print(values.pop())
    # elif newVariable == True:
    #     temp = values.top()
    #     lstVariableNumber.append(values.pop())
    #     indexVariable = findIndex(lstVariableNumber, temp)
    #     print(lstVariable[indexVariable])


    #Variable RESET:
    reAssign = False
    newVariable = False
    first = False
    userInput = input("Please Enter Arithmetic: ")

# '''
# TEST CODE SUPPORTS:
# 1)
# x = 500
# x = x x +
# y = x x +
#
# --> 4
# 4
# --> 5 1 -
# 4
# --> x = 5 1 -
# x
# --> x
# 4
# --> x x +
# 8
# --> y = 1 x + 3 4 * - 2 /
# y
# --> y
# -3.5
# --> done()
