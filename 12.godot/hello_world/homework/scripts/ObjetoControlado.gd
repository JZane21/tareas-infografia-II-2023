extends Node2D

var position_x = 100
var position_y = 100
var speed = 5
var pressed_buttons = [
	false,
	false,
	false,
	false,
	false,
	false
]

func _process(delta):
	position.x = position_x
	position.y = position_y
	if pressed_buttons[0]:
		position_x -= speed
	if pressed_buttons[1]:
		position_x += speed
	if pressed_buttons[2]:
		position_y += speed
	if pressed_buttons[3]:
		position_y -= speed
	if pressed_buttons[4]:
		rotate(-0.1)
	if pressed_buttons[5]:
		rotate(0.1)

func _input(event):
	if (event is InputEventKey and event.is_pressed()):
		if (event.as_text_key_label() == "A"):
			pressed_buttons[0] = true
		if (event.as_text_key_label() == "D"):
			pressed_buttons[1] = true
		if (event.as_text_key_label() == "S"):
			pressed_buttons[2] = true
		if (event.as_text_key_label() == "W"):
			pressed_buttons[3] = true
		if (event.as_text_key_label() == "Q"):
			pressed_buttons[4] = true
		if (event.as_text_key_label() == "E"):
			pressed_buttons[5] = true
	elif (event is InputEventKey and event.is_released()):
		if (event.as_text_key_label() == "A"):
			pressed_buttons[0] = false
		if (event.as_text_key_label() == "D"):
			pressed_buttons[1] = false
		if (event.as_text_key_label() == "S"):
			pressed_buttons[2] = false
		if (event.as_text_key_label() == "W"):
			pressed_buttons[3] = false
		if (event.as_text_key_label() == "Q"):
			pressed_buttons[4] = false
		if (event.as_text_key_label() == "E"):
			pressed_buttons[5] = false

func _on_left_button_button_down():
	pressed_buttons[0] = true
func _on_left_button_button_up():
	pressed_buttons[0] = false

func _on_right_button_button_down():
	pressed_buttons[1] = true
func _on_right_button_button_up():
	pressed_buttons[1] = false

func _on_down_button_button_down():
	pressed_buttons[2] = true
func _on_down_button_button_up():
	pressed_buttons[2] = false

func _on_up_button_button_down():
	pressed_buttons[3] = true
func _on_up_button_button_up():
	pressed_buttons[3] = false


func _on_left_rotation_button_button_down():
	pressed_buttons[4] = true
func _on_left_rotation_button_button_up():
	pressed_buttons[4] = false

func _on_right_rotation_button_button_down():
	pressed_buttons[5] = true
func _on_right_rotation_button_button_up():
	pressed_buttons[5] = false
