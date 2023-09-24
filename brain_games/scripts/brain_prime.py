#!/usr/bin/env python3
# from brain_games.cli import welcome_user
from random import randint, choice
import prompt, math


def greet():
    prime()


def main():
    greet()


def prime():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count_rounds = 3
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < count_rounds:
        number = randint(1, 10)
        print(f"Question: {number}")
        answer = prompt.string('Your answer: ')
        result = 0
        for j in range(2, number // 2 + 1):
            if number % j == 0:
                result += 1
        if (result == 0 and answer == 'yes') or (result > 0 and answer == 'no'):
            print('Correct!')
            i += 1
        else:
            if result == 0:
                print(f"'{answer}' is wrong answer;(.Correct answer was 'yes'.")
                print("Let's try again, " + name + "!")
                break
            else:
                print(f"'{answer}' is wrong answer;(.Correct answer was 'no'.")
                print("Let's try again, " + name + "!")
                break
    if i == count_rounds:
        print(f'Congratulations, {name}!')
