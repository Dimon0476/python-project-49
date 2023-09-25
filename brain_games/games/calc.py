from random import randint, choice
import prompt


def calc():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count_rounds = 3
    print('What is the result of the expression?')
    i = 0
    while i < count_rounds:
        number1 = randint(1, 10)
        number2 = randint(1, 10)
        operator = choice('+-*')
        print(f"Question: {number1} {operator} {number2}")
        answer = prompt.string('Your answer: ')
        match operator:
            case '+':
                result = number1 + number2
            case '-':
                result = number1 - number2
            case '*':
                result = number1 * number2
        if answer == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{result}'.")
            print("Let's try again, " + name + "!")
            break
    if i == count_rounds:
        print(f'Congratulations, {name}!')
