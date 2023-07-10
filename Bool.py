from random import randint
r= 0
number = randint(1,10)
while r<3:
    print("Угадай число от 1 до 10")
    p = int(input())
    r+=1
    if p < number:
        if(number-p)<=2:
         print ("тепло,число больше твоего, ты почти угадал")
        else:
            print("Холодно, число больше,попробуй еще раз")

    elif p > number:
        if (p-number) <= 2:
         print("тепло, число меньше твоего, ты почти угадал")
        else:
            print("холодно, число меньше,попробуй еще раз")
    elif p == number:
        break
if p == number:
    print("Превосходно")
elif p != number:
    print("У тебя не осталось попыток.")

