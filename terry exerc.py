#output question and ask for input
number = input("Type in a 3 digit number\n")
#convert input to integers
num1 = int(number[0])
num2 = int(number[1])
num3 = int(number[-1])
#calculate values
answer = (num1 + num3) * num2
#print out answer
print(answer)