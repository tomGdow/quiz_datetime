import data_quiz as d

def problem_one():
    """ print an undefined identifier"""
    problem="""
   
    {: >4s} {}?
   
    """.format("", d.explanation['j'][1])
    answer=('j', d.explanation['j'][1])
    answer_explanation = "{} // {}".format(d.example['j'][0], d.example['j'][1])
    return(problem, answer, answer_explanation)

def problem_maker(key):
    """ print an undefined identifier"""
    def inner():
        problem=""" 
       
        {: >4s} {}?
       
        """.format("",d.explanation[key][1])
        answer=(key, d.explanation[key][1])
        answer_explanation = "{} // {}".format(d.example[key][1], d.example[key][2])
        return(problem, answer, answer_explanation)
    return inner
