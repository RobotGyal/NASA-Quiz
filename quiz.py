
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
QUIZ= ["\nWhat is the literal definition of Equinox? \n a) Equal Dark  \n b) Year Night  \n c) Day Night  \n d) Day Dark  \n e) Equal Night\n",

"""\nBefore NASA was formed, the National Advisory Committee for Aeronautics (NACA) was started
to supervise and direct the scientific study of the problems of flight.
The NACA also directed and conducted research and experiments in aeronautics.
Which President found NACA?
\n a) Franklin D. Roosevelt  \n b) Woodrow Wilson  \n c) Ronald Reagan  \n d) Theodore Roosevelt  \n e) John F. Kennedy\n""",

"\nNASA became operational how many years after the Soviets launched Sputnik 1, the world's first artificial satellite?",

"\nHow many Earth's would fit insode Jupiter?",

"""\nApollo 10's command module was called "Charlie Brown" and the lunar module was called "Snoopy."  """,

'''\nBessie Coleman, known as "Queen Bess, Daredevil Aviator," was the first African-American woman aviator.
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

# print(QUIZ[0])

running = True
while running:

    # for count, ele in enumerate(QUIZ,1):
    #     print(count, ele, '\n')
    print(colors.purple, "\n\nWelcome to the NASA QUIZ!!!! Prepare to put your knowledge to the test!!\n")

    print(colors.purple, "\nThe first 2 questions will be multiple choice. Please enter a letter(a-e)\n")
    multiple_choice_question(QUIZ[0], 'e')
    multiple_choice_question(QUIZ[1], 'b')

    print(colors.purple, "\nThe next 2 questions will be numerical. Please enter a whole number\n")
    numerical_question(QUIZ[2], '1')
    numerical_question(QUIZ[3], '1000')

    print(colors.purple, "\nThe last 2 questions will be true/false. Please enter True(t) or False(f) \n")
    true_false_question(QUIZ[4], 't', 'Snoopy, the Peanuts Comic Strip character is the astronauts personal safety mascot')
    true_false_question(QUIZ[5], 'f', 'She got her license in France\n')
    
    print(colors.grey, "\nCorrect: ", len(correct_questions))
    print("Incorrect: ", len(incorrect_questions))

    play_again = input("Would you like to play again? Press Yes(y) or No(n)\n").lower()
    if play_again == 'y':
        continue
    else:
        running = False