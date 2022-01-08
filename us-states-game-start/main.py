import turtle
import pandas
from turtle import Turtle

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

write_map = Turtle()
write_map.penup()
write_map.hideturtle()
states_correct = 0

# print(type(answer_title_case))
df = pandas.read_csv("50_states.csv")
game = True
# df_dict = df.to_dict()
correct_answers_sum = []
while game:
     #list to check all new answers with previous ones
    answer_state = screen.textinput(title=f"{states_correct}/50 States Correct", prompt="What's another state's name?")
    answer_title_case = answer_state.title()
    if answer_title_case in df["state"].values and answer_title_case not in correct_answers_sum:
        correct_answers_sum.append(answer_title_case)
        correct_state_row = df[df.state == answer_title_case] # monday = data[data.day == "Monday"]
        x = int(correct_state_row["x"])
        y = int(correct_state_row["y"])
        # value1 = correct_state_row['state']
        # print(x, y, value1)
        write_map.goto(x, y)
        write_map.write(answer_title_case)
        states_correct += 1

turtle.mainloop()

screen.exitonclick()