# Practice #1
###
# 1. Створи програму, що запитує твоє ім’я, прізвище та по-батькові.
# Виведи на екран своє повне ПІБ.
def task1():
    first_name = input('Enter your first name: ')
    middle_name = input('Enter your middle name: ')
    last_name = input('Enter your last name: ')

    print(f"It's a pleasure to meet you, {first_name} {middle_name} {last_name}!")

###
# 2. Напиши програму, яка б визначала, чи не довше 20 символів рядок, який ввів користувач. 
# Якщо рядок більше 20 символів, програма має виводити помилку.
def task2():
    string = input('Type your string: ')
    
    if len(string) > 20:
        raise Exception("Sorry, string is too long! Try not more than 20 symbols")
    else:
        print('Your string is not more than 20 symbols')

###
# 3. Напиши програму, яка б визначила існування трикутника, по введеним користувачем трьом сторонам 
# та виводила на екран «трикутник існує» та «трикутника не існує», в залежності від результату.
def task3():
    try: 
        a = int(input('Enter the length of the 1st side of a triangle: '))
        b = int(input('Enter the length of the 2nd side of a triangle: '))
        c = int(input('Enter the length of the 3d side of a triangle: '))
        
        if ((a + b > c) and
            (a + c > b) and
            (b + c > a)):
            # the only case when triangle exists - all conditions are True
            print('Great, Triangle with entered sides exists!')
        else:
            print("Sorry, Triangle with entered sides doesn't exist.")
            
    except ValueError:
        print('Error... You should write only numbers.')

###
# 4. Напиши програму, яка б обраховувала площу кола по введеному користувачем радіусу.
import math

def task4():
    try:
        radius = int(input('Enter radius of a circle: '))
        circle_area = math.pi * radius ** 2
        print('%.2f' % circle_area)
        
    except ValueError:
        print('Error... You should write only numbers')
        
###
# 5. Напиши програму, яка б клала у словник значення ціни і назви товару, які користувач вводить з клавіатури.
def task5():
    item = input('Enter your item: ')
    price = input('Enter the price for your item: ')
    
    product = dict(item_name = item, item_cost = price)
    print(f"We have {product['item_name']} with the price equals {product['item_cost']}")
    
# Write the task number    
def main():
    task5()
    
main()