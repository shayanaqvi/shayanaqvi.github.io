+++
title = 'Quick-and-dirty random encounter mechanic in Godot'
date = 2025-04-01T14:32:04+05:00
Categories = ["Video Games", "Programming"]
draft = false
+++

I'm surprised that I managed to get this done in about 20 minutes last night given that I've come back to Godot after nearly 3 years!

Anyways, we'll be writing a barebones random encounter mechanic here. From my experience with some 90s to mid 2000s JRPGs, I _think_ random encounters generally work as such:

1. Start a timer of a random duration that counts down to a random encounter
2. Pause this timer if the player stops moving / is idle
3. Resume the same timer when the player starts moving again

This is what we shall implement.

# Project setup

We'll have a total of 3 scenes: one for the player, one for the "main" scene, and one that contains the code for the random encounters.

## Player scene

I went a bit overkill with the player scene, since I set up animations [with this spritesheet](https://otterisk.itch.io/hana-caraka-base-character) and added a sprinting mechanic. You don't need to do this, but you can if you want.

This is how I have my player scene set up:

{{<image
  frame="true"
  width=16em
  src="img/random-encounters-godot/1.png"
  caption="\"player\" is a CharacterBody2D"
>}}

Writing player movement isn't the focus of this article, so I'll just put the code that handles player movement below.

{{< highlight gdscript "linenos=inline, style=arduino" >}}
extends CharacterBody2D

enum directions {UP, DOWN, LEFT, RIGHT}
var current_direction = directions.DOWN
var screen_size
var is_sprinting
@export var speed = 250
@onready var animated_sprite = get_node("AnimatedSprite2D")

func _ready() -> void:
	screen_size = get_viewport_rect().size

func _process(delta: float) -> void:
	handle_player_movement(delta)

func handle_player_movement(delta):
	if Input.is_action_just_pressed("sprint"):
		speed *= 1.5
		is_sprinting = true
	if Input.is_action_just_released("sprint"):
		speed /= 1.5
		is_sprinting = false

	# determine direction of movement
	velocity = Vector2.ZERO
	if Input.is_action_pressed("move_right"):
		velocity.x += 1
		current_direction = directions.RIGHT
	if Input.is_action_pressed("move_left"):
		velocity.x -= 1
		current_direction = directions.LEFT
	if Input.is_action_pressed("move_up"):
		velocity.y -= 1
		current_direction = directions.UP
	if Input.is_action_pressed("move_down"):
		velocity.y += 1
		current_direction = directions.DOWN
	
	# normalise movement vector
	if velocity.length() > 0:
		velocity = velocity.normalized() * speed
	
	# update player position
	position += velocity * delta
	position = position.clamp(Vector2.ZERO, screen_size)

	# handle animations
	if velocity.length() == 0:
		match current_direction:
			directions.RIGHT:
				animated_sprite.flip_h = false
				animated_sprite.play("idle_left_right")
			directions.LEFT:
				animated_sprite.flip_h = true
				animated_sprite.play("idle_left_right")
			directions.UP:
				animated_sprite.play("idle_up")
			directions.DOWN:
				animated_sprite.play("idle_down")
	else:
		if velocity.x > 0 and velocity.y == 0:
			animated_sprite.flip_h = false
			if is_sprinting:
				animated_sprite.play("sprint_left_right")
			else:
				animated_sprite.play("walk_left_right")
		if velocity.x < 0 and velocity.y == 0:
			animated_sprite.flip_h = true
			if is_sprinting:
				animated_sprite.play("sprint_left_right")
			else:
				animated_sprite.play("walk_left_right")
		if velocity.y > 0 and velocity.x == 0:
			animated_sprite.play("walk_down")
		if velocity.y < 0 and velocity.x == 0:
			animated_sprite.play("walk_up")
{{< /highlight >}}

If you want this code to work via copy/pasting, then you'll have to set up the animations for the sprite and the input map yourself.

Also, this code is probably pretty convoluted; I just needed something quick.

### Adding signals

We'll emit a signal whenever the player moves or stops moving. These signals we shall connect in our random encounter script, which we'll write in just a bit.

First, define two signals.

{{< highlight gdscript "linenos=inline, style=arduino" >}}
signal player_moving
signal player_stopped
{{< /highlight >}}

Then, at line 49, add `player_stopped.emit()` and at line 61, `player_moving.emit()`. That's it!

# Random encounter scene 

There are only two things here: a regular ol' Node and a timer (which I've named to "random_encounter_timer"). You'll want to attach a script to the node.

>## Connecting the signals we defined
>
>Firstly, create a "main" scene and add your player and this new random encounter scene in it. Then, select your player and find the signals we defined on the right-hand side.
>
>{{<image
  frame="true"
  width=16em
  src="img/random-encounters-godot/2.png"
>}}
>
>Double click on each signal, and connect it to the script we created in the random encounter scene.
>
>{{<image
  frame="true"
  width=16em
  src="img/random-encounters-godot/3.png"
>}}

We'll add one more signal to our random encounter script, which is the timer's timeout signal. You can connect that in a similar fashion to the other signals. There should be 3 functions now in that script.

Now comes the actual meat of this article.

Remember what we read about random encounters above:

>1. Start a timer of a random duration that counts down to a random encounter
>2. Pause this timer if the player stops moving / is idle
>3. Resume the same timer when the player starts moving again

Let's start with the timer. Remember, we don't want the timer to run if the player is idle, so it makes sense to start it when we get the signal of player movement.

{{< highlight gdscript "linenos=inline, style=arduino" >}}
func _on_player_player_movement():
    timer_duration = randf.range(0.5, 1.0) * 2
    random_encounter_timer.start(timer_duration)
{{< /highlight >}}

>There's no particular reason as to why I'm doing the timer duration that way; I thought it was easier for testing purposes.

We also know that we want to trigger a random encounter when the timer times out.

{{< highlight gdscript "linenos=inline, style=arduino" >}}
func on_random_encounter_timer_timeout():
    print("Random encounter!")
{{< /highlight >}}

And, we also want to pause this timer when the player stops moving.

{{< highlight gdscript "linenos=inline, style=arduino" >}}
func _on_player_player_stopped():
    random_encounter_timer.set_paused(true)
{{< /highlight >}}

The main issue now is that we'll be starting a new timer every time the player moves. We want to allow any timer we set to complete first, before we start a new one. So, we'll check if we currently have a timer going in the background. 

{{< highlight gdscript "linenos=inline, style=arduino" >}}
func _on_player_player_movement():
    # if no timer is running, start a new one.
    if random_encounter_timer.is_stopped():         
        timer_duration = randf.range(0.5, 1.0) * 2
        random_encounter_timer.start(timer_duration)

    # if we have a paused timer, resume it.
    if random_encounter_timer.is_paushed():
        random_encounter_timer.set_paused(false)
{{< /highlight >}}

That's it!

Here's all the code:

{{< highlight gdscript "linenos=inline, style=arduino" >}}
extends Node

@onready var random_encounter_timer = get_node("random_encounter_timer")

var timer_duration = 0

func _on_random_encounter_timer_timeout() -> void:
	print("Random encounter!")

func _on_player_player_moving() -> void:
	if random_encounter_timer.is_stopped():
		timer_duration = randf_range(0.5, 1.0) * 2
		random_encounter_timer.start(timer_duration)
	if random_encounter_timer.is_paused():
		random_encounter_timer.set_paused(false)

func _on_player_player_stopped() -> void:
	random_encounter_timer.set_paused(true)
{{< /highlight >}}

I'll put a clip of this below; you should be able to see it working in the console.
{{< youtube CnSdl4r5sv0>}}

I don't write guides very often, so let me know if I can explain anything here better!