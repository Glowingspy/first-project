#it imports the module time
import time

#i used function because it is easy to restart the program incase of any accidental presses
#i know that the indentation may not be perfect, but if it works it works
def maincode():
    print('Do you want to start the timer?')
    print('Type "yes" or "no" ')
    yes_no = input()
    if yes_no == 'no':
        print('Get out of here!!!')
    elif yes_no == 'yes':
     print('From what second do you want to start?')
     print('Choose an integer from 1 to 60')
     print('Press ENTER to start')
     secask = int(input())    
     if secask > 60 or secask <= 0:
      print('That is an invalid statment. The program will restart in 10 seconds')
      time.sleep(10)
      maincode()
     elif secask > 0 and secask <= 60:
         while secask > 0 :
             print(secask - 1)
             time.sleep(1)
             secask = secask - 1  
                
             
                         
    else:
     print('The input you have typed is invalid. The program will restart in 10 seconds')
     while True:
      time.sleep(10)
      maincode()
      


maincode()      