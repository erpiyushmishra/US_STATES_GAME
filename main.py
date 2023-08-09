

import turtle
import pandas
screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_state=data.state.to_list()





answered_state_list=[]
while len(answered_state_list)<50:
    answer_state = screen.textinput(title=f"{len(answered_state_list)}/50 are correct", prompt="What's another state's name").title()
    if answer_state=="Exit":
        missing_states=[]
        missing_states=[state for state in all_state if state not in answered_state_list]
        # for state in all_state:
        #     if state not in answered_state_list:
        #         missing_states.append(state)
        missing_data=pandas.DataFrame(missing_states)
        missing_data.to_csv("I did it again")
        break


    if answer_state in all_state:
        answered_state_list.append(answer_state)

        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
missing_states_in_panda=pandas.DataFrame(missing_states)
missing_states_in_panda.to_csv("what I missed")






