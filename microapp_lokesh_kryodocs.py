

def prec(c):
  if(c=='*' or c=='/'):
     return 2
  elif(c=='+' or c=='-'):  
     return 1  
  else:
     return -1
def evaluate(expression):
  stack=[] 
  res=""
  stack.append('0')
  for i in expression:
     if(i.isnumeric()):
        res=res+i 
     elif(i=='('):
           stack.append(i)
     elif(i==')'):
            c=stack.pop()
            while(c!='('):
                res=res+c
                c=stack.pop()  
     else: 
          c=stack.pop()
          while((c!='0' and (prec(i)<=prec(c)))):
              res=res+c
              c=stack.pop()  
          stack.append(c)     
          stack.append(i)

  c=stack.pop()                  
  while(c!='0'):
    res=res+c
    c=stack.pop()
  #print(res)

  stack1=[]
  for i in res:
   if i.isnumeric():
     stack1.append(i)
   else:
     val1=int(stack1.pop())
     val2=int(stack1.pop())
     if i=='+':
         stack1.append(val2+val1)
     elif i=='-':
         stack1.append(val2-val1)
     elif i=='*':
         stack1.append(val2*val1)
     elif i=='/':
          stack1.append(val2/val1)
  return stack1.pop()

expression=input("enter an expression:")
print(evaluate(expression))
