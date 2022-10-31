def add(n1,n2):
  return n1+n2
def subtract(n1,n2):
  return n1-n2
def multiplication(n1,n2):
  return n1*n2
def division(n1,n2):
  return(n1/n2)
dict={
"+":add,
"-":subtract,
"*":multiplication,
"/":division,
}
num1=int(input("Enter number first number: "))
num2=int(input("Enter number second number: "))
for operators in dict:
  print(operators)
operation_symbol=input("pick any one of the operation from above")
calucation_function=dict[operation_symbol]
answer = calucation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
