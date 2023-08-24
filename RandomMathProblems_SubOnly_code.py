# creating new math worksheets for Margaux
# practicing subtraction

import random

problems = int(input('How many questions? '))

def main():
  num1 = random.randint(0,11)
  num2 = random.randint(0,num1)
    
  print(num1, " - ", num2, " =    ")
  

for total in range(problems):
  main()