# this asks you baaic questiond and tells you your bmi

print("Do you want to start calculating your BMI(body mass index)? ")
print('WRITE "yes" or "no" ')
yes_no = input()


if yes_no == ('no'):
    print('Get out of here!!!')
elif yes_no == 'yes':
    print('What is your weight(in kg)? ')
    weight = float(input())
    print('what is your height(in cm)?')
    height = float(input())
 
    print('This is your BMI(body mass index)  :  ')
    bmi = weight / (height**2)     
    print(bmi)
       


else: 
 print('The statment is invalid, please run the system again')
 
while yes_no == 'yes':
 if bmi > 25 and bmi < 30:
  print('you are overweight')
  break
 elif bmi < 19 :
  print('you are underweight')
  break
 elif bmi > 30 :
  print('You are obese')
  break
 elif bmi > 19 and bmi < 25 :
  print('You have a healthy bmi')
  break
