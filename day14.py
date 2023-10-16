#_______________Break_and_Continue____________

#BREAK:

for i in range(12):
 if( i == 10):
   break
 print("5 x", i+1, "=", 5*(i+1))

print("Exited from loop")


#Continue:

for i in range(12):
  if( i == 0):
    print("skipping this iteration")
    continue
  print("5 x", i, "=", 5*i)



  """
  Break = The break statement in Python is used to terminate the loop or statement 
  in which it is present. After that, the control will pass to the statements that 
  are present after the break statement, if available. If the break statement is 
  present in the nested loop, then it terminates only those loops which contain the 
  break statement. 
  

  Continue = Continue is also a loop control statement just like the break statement. 
  continue statement is opposite to that of the break statement, instead of terminating 
  the loop, it forces to execute the next iteration of the loop. As the name suggests 
  the continue statement forces the loop to continue or execute the next iteration.
  """