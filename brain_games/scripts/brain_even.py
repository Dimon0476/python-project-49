#!/usr/bin/env python3
# from brain_games.cli import welcome_user
from random import randint
import prompt


def greet():
    is_even()


def main():
    greet()


def is_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count_rounds = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < count_rounds:
        question = randint(1, 10)
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if (question % 2 == 0 and answer == 'yes') or (question % 2 == 1 and answer == 'no'):
            print('Correct!')
            i += 1
        else:
            if question % 2 == 0:
                print(f"'{answer}' is wrong answer;(.Correct answer was 'yes'.")
                print("Let's try again, " + name + "!")
                break
            if question % 2 == 1:
                print(f"'{answer}' is wrong answer;(.Correct answer was 'no'.")
                print("Let's try again, " + name + "!")
                break
    if i == count_rounds:
        print(f'Congratulations, {name}!')
