
# Multiple Choice
Q1 = "What is the literal definition of Equinox? \n a) Equal Dark  \n b) Year Night  \n c) Day Night  \n d) Day Dark  \n e) Equal Night\n"
# equal night

Q2 = """Before NASA was formed, the National Advisory Committee for Aeronautics (NACA) was started
to supervise and direct the scientific study of the problems of flight.
The NACA also directed and conducted research and experiments in aeronautics.
Which President found NACA?
\n a) Franklin D. Roosevelt  \n b) Woodrow Wilson  \n c) Ronald Reagan  \n d) Theodore Roosevelt  \n e) John F. Kennedy\n"""
# Woodrow Wilson

# Numerical Response
Q3 = "NASA became operational how many years after the Soviets launched Sputnik 1, the world's first artificial satellite?"
# 1

Q4 = "How many Earth's would fit insode Jupiter?"
# 1000


# True/False
Q5 = """Apollo 10's command module was called "Charlie Brown" and the lunar module was called "Snoopy."  """
# True
# if answer = False, respond -> 

Q6 = ''' Bessie Coleman, known as "Queen Bess, Daredevil Aviator," was the first African-American woman aviator.
She received her pilot's certificate in 1921 in America and learned stunt-flying there. '''
# False, she got her license in France

#Colors for use later
class colors:
    purple = '\033[35m'
    grey = '\033[37m'
    red='\033[31m'



# FUNCTIONS
def multiple_choice_question(question, answer):
    print(colors.grey, question)
    user_answer = input("Input a choice (a-e): \n").lower()
    if user_answer == answer:
        print("You are correct!")
        return 1
    else:
        print(colors.red, "Incorrect, The answer is: ", answer)
        return 0

def numerical_question(question, answer):
    print(colors.grey, question)
    user_answer = input("Input a number: \n")
    if user_answer == answer and user_answer.isdigit():
        print("You are correct!")
        return 1
    # elif user_answer == answer and user_answer.isdigit == False:
    #     print("Inproper format")
    else:
        print(colors.red, "Incorrect, The answer is: ", answer)
        return 0

def true_false_question(question, answer, fact):
    print(colors.grey, question)
    user_answer = input("Enter True(t) or False(f): \n").lower()
    if user_answer == answer:
        print("You are correct!")
        return 1
    else:
        print(colors.red, "Incorrect, The answer is: ", answer, '\n', fact)
        return 0



# TESTS
multiple_choice_question(Q1, 'e\n')
multiple_choice_question(Q2, 'b\n')

numerical_question(Q3, '1\n')
numerical_question(Q4, '1000\n')

true_false_question(Q5, 't', 'Snoopy, the Peanuts Comic Strip character is the astronauts personal safety mascot')
true_false_question(Q6, 'f', 'She got her license in France\n')