my_name = 'Alina'
my_age = 18
print('my name is ', my_name, ", i'm ", my_age)

mnx5 = my_name * 5
mn = my_name + my_name + my_name + my_name + my_name
print(mn, mnx5)

user_name, user_age = input("what is ur name? how old are u?").split()
flag = True
while flag:
    try:
        user_age = int(user_age)
        flag = False
    except ValueError:
        print('error, try again')
        user_age = input()

flag = True
while flag:
    if user_age > 150 or user_age < 0:
        user_age = int(input('silly little liar, enter ur actual age'))
    else:
        break

if user_age < 18:
    print('kid, go learn ur lessons')
elif user_age > 30:
    print('don\'t u think about ur last will')
else:
    print('so what am i supposed to joke about')

print(user_name[1:-1])
print(user_name[::-1])
print(user_name[-3], user_name[-2], user_name[-1])
print(user_name[0:5])

u_a = map(int, list(str(user_age)))
mult = 1
for i in u_a:
    mult *= i
u_a = map(int, list(str(user_age)))
print(len(user_name), sum(u_a), mult)

un = user_name
un = un.replace(un[0], un[0].upper(), 1)
print(un, user_name.upper(), user_name.lower())
for i in un:
    if i.isupper():
        un = un.replace(i, i.lower(), 1)
    else:
        un = un.replace(i, i.upper(), 1)
print(un)

flag = True
while flag:
    answer = int(input("2 + 2 * 2 = "))
    if answer == 6:
        print('correct')
        break
    else:
        print('no, try again')
