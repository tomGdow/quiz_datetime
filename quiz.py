import random

import problems_quiz as p
import functions_quiz as f
import data_quiz as d

if __name__ == '__main__':

    problem_list = [p.problem_maker(x) for x in d.codes.keys()]
    random_problem_list = random.sample(problem_list, k=len(problem_list)) # k = probem_number
    question_counter = f.counter(len(problem_list))
    f.display_problem(random_problem_list[0],question_counter, len(problem_list))
    i = 1
    quit = False
    while not quit and i < len(problem_list):  # i < problem_number
        choice =f.next_question(random_problem_list[i], f.continue_choice, question_counter, len(problem_list))
        i += 1
        quit = not choice

