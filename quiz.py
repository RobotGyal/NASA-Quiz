
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

Q6 = ''' Bessie Coleman, known as "Queen Bess, Daredevil Aviator," was the first African-American woman aviator.
She received her pilot's certificate in 1921 in America and learned stunt-flying there. '''
# False, she got her license in France



# FUNCTIONS
def multiple_choice(question, answer):
    print(question)
    user_answer = input("Input a answer: \n").lower()
    if user_answer == answer:
        print("You are correct!")
    else:
        print("You are incorrect")




# TESTS
multiple_choice(Q1, 'e')
multiple_choice(Q2, 'b')