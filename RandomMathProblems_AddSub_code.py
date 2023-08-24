# creating new math worksheets for Margaux
# practicing addition and subtraction

import random

problems = int(input('How many questions? '))

def main():
  num1 = random.randint(0,11)
  num2 = random.randint(0,num1)
    
  print(num1, " - ", num2, " =    ")
  
def secondmain():
  num1 = random.randint(0,11)
  num2 = random.randint(0,11)
  print(num1, " + ", num2, " =    ")
  
for total in range(problems):
  if (total % 2) == 0:
    secondmain()
  else:
    main()