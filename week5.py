#normal
'''
a = 1
b = 2
sum = a + b
minus = b - a
mulltiply = a * b
divide = b / a
 '''
#OOP    

def SUM(a, b, c):
    sum = int(a) + int(b) + int(c)
    return sum

def MINUS(a, b, c):
    sum = int(a) - int(b) - int(c)
    return sum

def MULTIPLY(a, b, c):
    sum = int(a) * int(b) * int(c)
    return sum

def DIVIDE(a, b):
    sum = int(a) / int(b)
    return sum

operate = input("1 = Sum, 2 = Minus, 3 = Multiply, 4 = Divide : ")

if(operate == "1"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    inp3 = input("C : ")
    print("SUM = " , SUM(inp1, inp2, inp3))

elif(operate == "2"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    inp3 = input("C : ")
    print("Minus = " , MINUS(inp1, inp2, inp3))
elif(operate == "3"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    inp3 = input("C : ")
    print("Multiply = " , MULTIPLY(inp1, inp2, inp3))
    
elif(operate == "4"):
    inp1 = input("A : ")
    inp2 = input("B : ")
    print("Divide = " , DIVIDE(inp1, inp2))
else:
    print("Not Found")
'''
print("SUM = " , SUM(inp1, inp2, inp3))

print("SUM = ",SUM(10, 20, 30))
print("MINUS = " ,MINUS(50, 10, 15))
print("MULTIPLY" ,MULTIPLY(4, 4, 6))
print("DIVIDE = " ,DIVIDE(8, 2))
'''