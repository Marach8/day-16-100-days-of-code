print('''Fill in the blank lyrics! (Type in the blank lyrics and see if you are as cool as me.)''')
print()
print('\033[31mYou have only 5 trials for this \033[0m')
print()
x = 5
y = 1
while x != 0:
  print()
  ask = input('I love ___ to the moon. > ')
  print()
  if ask == 'you':
    print(f'\033[32m!Weldone, You got the correct word with {y} trial(s). 🎉\033[0m')
    break
  else:
    print('Nope, you did not get the right word, try again!')
    x -= 1
    y += 1
    print()
    print(f'\033[31mYou have only {x} trials left\033[0m')  