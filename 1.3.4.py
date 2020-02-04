from pip._vendor.distlib.compat import raw_input
import random


def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'


def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not good
    '''

    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food_id()'
        if food_id('other') != 'NOT Starchy, NOT Fruit':
            works = 'other bug in food_id()'
        # Add tests so that all lines of code are visited during test

    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False


def f(x):
    if int(x) != x:
        print("n is not an integer")
    if x % 2 != 0:
        print("n is odd")
    if x % 3 != 0:
        print("n is even")
    else:
        print("n is a multiple of 6")


def guess_once():
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess <= secret:
            print('Too low - my number is ', secret, sep='', end='!\n')
        else:
            print('Too high - my number is ', secret, sep='', end='!\n')
    else:
        print('Right, my number is', guess, end='!\n')

def quiz_decimal(low, high):
    print('Type a number between', low, 'and', high, '.')
    number = int(raw_input('Number: '))
    if number >= high:
        print('')


