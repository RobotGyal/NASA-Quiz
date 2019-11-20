
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
    blue = '\33[94m'
    blink = '\33[5m'
    end = '\33[0m'

correct_questions = []
incorrect_questions = []
acceptable_letters = ['a', 'b', 'c', 'd', 'e']
true_false = ['t', 'f']
question_num = 1

# FUNCTIONS
def multiple_choice_question(question, answer):
    print(colors.grey, question)
    user_answer = input("Input a choice (a-e): \n").lower()
    if user_answer == answer:
        print(colors.green, "You are correct!")
        correct_questions.append(user_answer)    
        return 1
    elif user_answer not in acceptable_letters:
        print("\nInput out of bounds. Try again")
        multiple_choice_question(question, answer)
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
    elif user_answer.isdigit() == False:
        print("\nInput not a number. Try again")
        numerical_question(question, answer)
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
    elif user_answer not in true_false:
        print("\nInput out of bounds. Try again")
        true_false_question(question, answer, fact)
    else:
        print(colors.red, "Incorrect, The answer is: ", answer, '\n', fact)
        incorrect_questions.append(user_answer)
        return 0




running = True
while running:
    # for count, ele in enumerate(QUIZ,1):
    #     print(count, ele, '\n')
    print(colors.blue, "\n\nWelcome to the NASA QUIZ!!!! Prepare to put your knowledge to the test!!\n")

    print(colors.blue, "\nThe first 2 questions will be multiple choice. Please enter a letter(a-e)\n")
    multiple_choice_question(QUIZ[0], 'e')
    multiple_choice_question(QUIZ[1], 'b')

    print(colors.blue, "\nThe next 2 questions will be numerical. Please enter a whole number\n")
    numerical_question(QUIZ[2], '1')
    numerical_question(QUIZ[3], '1000')

    print(colors.blue, "\nThe last 2 questions will be true/false. Please enter True(t) or False(f) \n")
    true_false_question(QUIZ[4], 't', 'Snoopy, the Peanuts Comic Strip character is the astronauts personal safety mascot')
    true_false_question(QUIZ[5], 'f', 'She got her license in France\n')
    
    print(colors.blink, "\nCorrect: ", len(correct_questions))
    print("Incorrect: ", len(incorrect_questions))

    if len(correct_questions) < 2:
        print(colors.blue, "\nYou put in good effort but try for higher next time!")
    elif len(correct_questions) >= 2 and len(correct_questions) < 5:
        print(colors.blue, "\nNot too shabby!")
    else:
        print(colors.blue, "\nYou are a master at NASA. Good Job Space Cadet!")


    print(colors.end, colors.blue, "\nWould you like to play again?")
    play_again = input("Press Yes(y) or No(n)\n").lower()
    if play_again == 'y':
        continue
    else:
        running = False