from random import randint
import prompt
import math


def gcd():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count_rounds = 3
    print('Find the greatest common divisor of given numbers.')
    i = 0
    while i < count_rounds:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        print(f"Question: {number1} {number2}")
        answer = prompt.string('Your answer: ')
        result = math.gcd(number1, number2)
        if answer == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{result}'.")
            print("Let's try again, " + name + "!")
            break
    if i == count_rounds:
        print(f'Congratulations, {name}!')
