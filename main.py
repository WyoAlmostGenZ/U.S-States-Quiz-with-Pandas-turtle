import turtle
import pandas


my_screen = turtle.Screen()
my_screen.title("U.S States Game")
img = "blank_states_img.gif"
my_screen.addshape(img)
turtle.shape(img)


data = pandas.read_csv("50_states.csv")

# print(state_input)
# print(x_cor_input)
# print(y_cor_input)

states_guessed = []
var = 0

all_states = data["state"].tolist()

for entry in range(0, 49):
	user_answer = my_screen.textinput(title=f"GuessState {var} of 50", prompt="What's another state's name").title()

	if user_answer in all_states:
		state_input = data[data["state"] == user_answer]
		x_cor_input = int(state_input["x"])
		y_cor_input = int(state_input["y"])
		var += 1
		t = turtle.Turtle()
		t.penup()
		t.goto(x_cor_input, y_cor_input)
		t.write(user_answer)
		t.hideturtle()
		states_guessed.append(user_answer)
	elif user_answer == "done":
		quit()
	elif user_answer not in all_states:
		print("Sorry that's not a state")

















