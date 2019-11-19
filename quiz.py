
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
QUIZ= ["What is the literal definition of Equinox? \n a) Equal Dark  \n b) Year Night  \n c) Day Night  \n d) Day Dark  \n e) Equal Night\n",

"""Before NASA was formed, the National Advisory Committee for Aeronautics (NACA) was started
to supervise and direct the scientific study of the problems of flight.
The NACA also directed and conducted research and experiments in aeronautics.
Which President found NACA?
\n a) Franklin D. Roosevelt  \n b) Woodrow Wilson  \n c) Ronald Reagan  \n d) Theodore Roosevelt  \n e) John F. Kennedy\n""",

"NASA became operational how many years after the Soviets launched Sputnik 1, the world's first artificial satellite?",

"How many Earth's would fit insode Jupiter?",

"""Apollo 10's command module was called "Charlie Brown" and the lunar module was called "Snoopy."  """,

''' Bessie Coleman, known as "Queen Bess, Daredevil Aviator," was the first African-American woman aviator.
She received her pilot's certificate in 1921 in America and learned stunt-flying there. '''

]

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`



#Colors for use later
class colors:
    purple = '\033[35m'
    grey = '\033[37m'
    red='\033[31m'
    green='\033[32m'

correct_questions = []
incorrect_questions = []


# FUNCTIONS
def multiple_choice_question(question, answer):
    print(colors.grey, question)
    user_answer = input("Input a choice (a-e): \n").lower()
    if user_answer == answer:
        print(colors.green, "You are correct!")
        correct_questions.append(user_answer)    
        return 1
    else:
        print(colors.red, "Incorrect, The answer is: ", answer)
        incorrect_questions.append(user_answer)    
        return 0

def numerical_question(question, answer):
    print(colors.grey, question)
    user_answer = input("Input a number: \n")
    if user_answer == answer and user_answer.isdigit():
        print(colors.green, "You are correct!")
        correct_questions.append(user_answer)
        return 1
    else:
        print(colors.red, "Incorrect, The answer is: ", answer)
        incorrect_questions.append(user_answer)
        return 0

def true_false_question(question, answer, fact):
    print(colors.grey, question)
    user_answer = input("Enter True(t) or False(f): \n").lower()
    if user_answer == answer:
        print(colors.green, "You are correct!")
        correct_questions.append(user_answer)
        return 1
    else:
        print(colors.red, "Incorrect, The answer is: ", answer, '\n', fact)
        incorrect_questions.append(user_answer)
        return 0



# TESTS
# multiple_choice_question(Q1, 'e')
# multiple_choice_question(Q2, 'b')

# numerical_question(Q3, '1')
# numerical_question(Q4, '1000')

# true_false_question(Q5, 't', 'Snoopy, the Peanuts Comic Strip character is the astronauts personal safety mascot')
# true_false_question(Q6, 'f', 'She got her license in France\n')

# print("\nCorrect: ", len(correct_questions))
# print("Incorrect: ", len(incorrect_questions))


# questions = {
#     'Q1':Q1,
#     'Q2':Q2,
#     'Q3':Q3,
#     'Q4':Q4,
#     'Q5':Q5,
#     'Q6':Q6,
# }

# for i in questions:
#     print(i, '\n')
# print(questions['Q2'])

# print(QUIZ[0])

for count, ele in enumerate(QUIZ,1):
    print(count, ele, '\n')