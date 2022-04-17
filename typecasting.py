#conversion of variable in different data type
while True:
  try:
    inpt=input("Enter a number:-")
    tp=[int,str,float,complex]
    count=len(tp)
    for i in range(0,count,1):
      cv=tp[i](inpt)
      print(cv,"==>",type(cv),"\n") 
            
  except ValueError:
    if(inpt.isalpha()):
      print(inpt,"is a string","\n") 
      print("Try again","\n")
    else:
      print(inpt,"is not a number","\n")
      print("Try again","\n")