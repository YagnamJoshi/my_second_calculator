from replit import clear
from art import logo
def add(a,b):
  a=float(a)
  b=float(b)
  return a+b
def sub(a,b):
  a=float(a)
  b=float(b)
  return a-b
def mul(a,b):
  a=float(a)
  b=float(b)
  return a*b
def div(a,b):
  a=float(a)
  b=float(b)
  return a/b

def calculator(choice,result1):
  result=0
  if(choice=='n'):
    f_num=input("Enter 1st number: ")
    print("+\n-\n*\n/\n")
    op=input("Choose operator: ")
    s_num=input("Enter 2nd number: ")
    if(op=='+'):
      result=add(f_num,s_num)
      print(f"{f_num}+{s_num}={result}")
    elif(op=='-'):
      result=sub(f_num,s_num)
      print(f"{f_num}-{s_num}={result}")
    elif(op=='*'):
      result=mul(f_num,s_num)
      print(f"{f_num}*{s_num}={result}")
    elif(op=='/'):
      result=div(f_num,s_num)
      print(f"{f_num}/{s_num}={result}")
  else:
    f_num=result1
    print("First number is:",result1)
    print("+\n-\n*\n/\n")
    op=input("Choose operator: ")
    s_num=input("Enter 2nd number: ")
    if(op=='+'):
      result=add(f_num,s_num)
      print(f"{f_num}+{s_num}={result}")
    elif(op=='-'):
      result=sub(f_num,s_num)
      print(f"{f_num}-{s_num}={result}")
    elif(op=='*'):
      result=mul(f_num,s_num)
      print(f"{f_num}*{s_num}={result}")
    elif(op=='/'):
      result=div(f_num,s_num)
      print(f"{f_num}/{s_num}={result}")
  choice=input("Enter 'y' if you want to continue calculating with {result} or 'n' to start a new calculation: ")
  clear()
  if(choice=='y'):
    calculator(choice,result)
  else:
    calculator(choice,result)

print(logo)
calculator('n',0)
