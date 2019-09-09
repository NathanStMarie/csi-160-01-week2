import random
"""
Filename: greeter.py
Author: Nathan St. Marie
Date: 9/8/2019

Purpose:
    Write a program that has a conversation with the user. The program must ask for strings, integers and floats as
    input. The program must ask for at least 4 different inputs from the user. The program must reuse atleast 4 of these
    inputs in what it displays on the screen. The program must perform at least 2 arithmetic operations on the numbers
    the user inputs.  Please turn in your .py file.

    Please include comments in your code to explain how it works

"""


# The greet_user() function defines a list of greetings, and an accompanying random integer that
# represents a random element to print from it.
def greet_user():
    # Define list of greetings,
    greeting_list = ["Hello there! I am Greeter.",
                     "Greetings, from Greeter! Greeter being me, of course.",
                     "Welcome to my cyberspace, I am Greeter.",
                     "49 20 6c 6f 76 65 20 79 6f 75! Oh sorry, you're not like me."]
    # Grab random integer to represent random element in list of greetings
    random_element_index = random.randint(0, len(greeting_list) - 1)
    # Output to screen the selected greeting
    print(greeting_list[random_element_index])


def get_input_and_reply():
    # The following list contains lists, which contain outputs for the user (as Strings), and an
    # accompanying String to represent which data type to expect back from the user.
    question_list = [["What's your favorite color?", "str"],
                     ["What is your age?", "int"],
                     ["I'm hungry for numbers, please give me a decimal!", "float"],
                     ["What is your name?", "str"]]

    random_element_index = random.randint(0, len(question_list) - 1)

    # this if / elif structure accounts for the expected differing inputs possible from question_list
    if question_list[random_element_index][1] == "str":
        user_input = str(input(question_list[random_element_index][0]))
    elif question_list[random_element_index][1] == "int":
        user_input = int(input(question_list[random_element_index][0]))
    elif question_list[random_element_index][1] == "float":
        user_input = float(input(question_list[random_element_index][0]))

    # this if / elif structure defines the reply for the user depending on the random index that was generated (random_element_index)
    if random_element_index == 0:
        reply = str("Your favorite color is " + str(user_input) + "? I'd tell you mine, but I can't see.")
    elif random_element_index == 1:
        reply = str("You are " + str(user_input) + " years old? That's roughly " + str(user_input * 365) + " days.")
    elif random_element_index == 2:
        reply = str("Nom nom nom.. that " + str(user_input) + " was tasty.. when divided in half, it is " + str(user_input / 2) + ", and when cubed it is " + str(user_input ** 2))
    elif random_element_index == 3:
        reply = str(str(user_input) + " is your name. Mine is Greeter!")
        
    print(reply)


# Greet the user, then run through the get_input_and_reply() method 4 times
greet_user()
for x in range(0,4):
    get_input_and_reply()



            
