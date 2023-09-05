import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

city = turtle.Turtle()
city.penup()
city.hideturtle()

game_is_on = True
compteur = 0

while compteur < 50:
    answer_state = screen.textinput(title=f"{compteur}/50 States correct", prompt="What's another state's name?").title() 
    
    if answer_state == "Exit":
        state_to_learn = [state for state in all_states if state not in guessed_states]
        df = pd.DataFrame(state_to_learn)
        df.to_csv("learn.csv")
        break
        
    if answer_state in all_states:
        state_data = data[data["state"] == answer_state]
        city.goto(int(state_data.x),int(state_data.y))
        city.write(f"{answer_state}")
        guessed_states.append(answer_state)
        compteur += 1
    
      

