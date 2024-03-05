from turtle import Turtle, Screen
import pandas

# Creates the turtle object that will display the blank US states map
t = Turtle()
screen = Screen()
screen.addshape("blank_states_img.gif")
t.shape("blank_states_img.gif")
screen.setup(700, 500)

# # Code to find mouse click coordinates
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_mouse_click_coor)

# Creates a dataframe from the CSV file containing information on US states names and respective coordinates on map
file = pandas.read_csv("50_states.csv")

# Creates lists of the US states and their respective X and Y coordinates on the map
states_list = file.state.tolist()
x_coord = file.x.to_list()
y_coord = file.y.to_list()

guessed_states = []
states_abb = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
              "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
              "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Sets base conditions for the game
game_over = False
not_exist = False
duplicate_state = False

while not game_over:
    # Prompts user for an input
    if duplicate_state:
        guess = screen.textinput("Guess", "You have already guessed this state.Try again.")
        duplicate_state = False
    elif not_exist:
        guess = screen.textinput("Guess", "This state does not exist. Try again.")
        not_exist = False
    else:
        guess = screen.textinput("Guess", "Enter the name of a state")

    # Ensures the first letter of each word is capitalized to match the format in the states list for comparison
    split_name = guess.split()
    new_value = split_name[0].capitalize()
    if len(split_name) > 1:
        new_value += " " + split_name[1].capitalize()

    if new_value in states_list and new_value not in guessed_states:
        # Creates a new turtle object to display the guessed state name on the map
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        state_index = states_list.index(new_value)
        x = x_coord[state_index]
        y = y_coord[state_index]
        new_turtle.goto(x, y)
        new_turtle.write(states_abb[state_index], move=False, align="center", font=("Arial", 8, "normal"))
        guessed_states.append(new_value)

    # Detects a duplicate guess
    elif guess in guessed_states:
        duplicate_state = True

    # Detects an invalid guess
    else:
        not_exist = True

    # Detects if the user completes or quits the game
    if len(guessed_states) == 50 or guess == "quit":
        game_over = True

# Informs the user of their success
if len(guessed_states) == 0:
    message_turtle = Turtle()
    message_turtle.write(f"Success!", move=False, align="center", font=('Courier', 40, 'normal'))
    message_turtle.hideturtle()

# Adds all 'unguessed' states to the states_to_learn.csv for the user to review
states_to_learn = pandas.DataFrame(states_list)
states_to_learn.to_csv("States_to_learn.csv")
screen.mainloop()
