from random import randint
import prompt


def progression():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count_rounds = 3
    size_progression = 10
    print('What number is missing in the progression?')
    i = 0
    while i < count_rounds:
        start = randint(1, 10)
        rule = randint(1, 10)
        progress = [start]
        for j in range(size_progression):
            progress.append(progress[j] + rule)
        random_index = randint(0, size_progression - 1)
        result = progress[random_index]
        progress[random_index] = '..'
        print(list(map(str, progress)))
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer;(.Correct answer was '{result}'.")
            print("Let's try again, " + name + "!")
            break
    if i == count_rounds:
        print(f'Congratulations, {name}!')
