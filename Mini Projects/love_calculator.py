print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
both_name = (name1+name2).lower()
t = both_name.count('t')
r = both_name.count('r')
u = both_name.count('u')
e = both_name.count('e')

l = both_name.count('l')
o = both_name.count('o')
v = both_name.count('v')
e = both_name.count('e')

first_digit = t+r+u+e
second_digit = l+o+v+e

score = str(first_digit)+str(second_digit)
score = int(score)

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score in range(40, 51):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")



