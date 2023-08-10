import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

# # how to get x,y coordinates of a click on the screen
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer = turtle.Turtle()

correct_guesses = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

#print(all_states)

answer_state = ""
while answer_state != "Exit":
    cgc = len(correct_guesses)
    answer_state = screen.textinput(title=f"{cgc}/50", prompt="What's another state's name?").title()
    if answer_state in all_states:
        
        all_states.remove(answer_state)
        correct_guesses.append(answer_state)

        #print(data[data.state == answer_state].x)
        #print(data[data.state == answer_state].y)   
        x = int(data[data.state == answer_state].x)
        y = int(data[data.state == answer_state].y)
        answer.penup()
        answer.goto(x, y)
        answer.write(answer_state)
    if cgc == 50:
        answer.goto(0, 0)
        answer.write("You got them all!")
        break

