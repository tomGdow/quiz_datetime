import os
import random

import data_quiz as d
import problems_quiz as p

def opening_msg():
    os.system('cls')
    print("What is the strftime format for the following?")

def options_msg():
    list_of_keys = list(d.codes.keys())
    len_codes = len(list_of_keys)//2
    bit1=(list_of_keys)[:len_codes+1]
    bit2=(list_of_keys)[len_codes:]
    zipped_list= list(zip(bit1,bit2))
    for item1, item2 in zipped_list: 
        print("{: >4s}{: >4s}{: >8s}{: >12s}{: >8s}".format("",item1, d.codes[item1], item2, d.codes[item2]))

def get_user_choice(): 
    bad_input = True
    while (bad_input):
        try:
            choice = input('Your Choice ? ')
            if choice != '':
                choice = choice[0]
            if choice not in d.codes.keys() or choice == '':
                raise ValueError('Invalid Choice')
            bad_input=False
        except ValueError as e:
            print(e)

    return choice[0]


def analyze_choice(fn,choice): 
    answer =fn()[1][0]
    while(choice != answer):
        print(f"No, the answer is not {d.codes[choice]}") 
        print('Have another go')
        choice=get_user_choice()
    print()
    print("YOU ARE RIGHT!")
    # print("{: >4s}{}".format("",'You are right!'))
    print()
    print("{: >4s}{}".format("",fn()[1]))
    print()
    print("{: >4s}{}".format("",fn()[2]))
    print()
    # print("{: >4s}{}".format("",fn()[3]))

def choose_problem():
    sample = random.sample(problem_list,1)
    return sample

def display_problem(problem, question_counter, total_questions): 
    opening_msg()
    print(f"Question {next(question_counter)} of {total_questions}")
    print(problem()[0]) 
    options_msg()
    print()
    choice=get_user_choice()
    analyze_choice(problem,choice)

# continue_choice=True        

def continue_choice():
    continue_choice=True        
    user_choice = input("CONTINUE or [Q/q]? > ")
    if (user_choice == '' or user_choice[0].upper() == "Y") and continue_choice:
        return continue_choice
        print('Bye')
        return continue_choice

def next_question(problem, choice_fn, question_counter,total_questions):
    user_continue_choice = choice_fn()
    if user_continue_choice:
        display_problem(problem, question_counter, total_questions)
    return user_continue_choice 
    
def counter(n):
    i = 1
    while i <=n:
        yield i
        i += 1

