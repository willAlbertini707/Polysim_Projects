"""
Simple ball bouncing simulator using pygame
Click anywhere on j-frame to create a new ball
and watch it bounce.
"""

import pygame, sys

# import Ball module
from Ball_Physics import Ball



# pre-define colors for game engine
WHITE =     (255, 255, 255)
BLUE =      (  0,   0, 255)
GREEN =     (  0, 255,   0)
RED =       (255,   0,   0)
BLACK = 	(  0,   0,  0)

# pre define width of j frame
width, height = (800, 800)

def get_time():
	# returns the current time in seconds
	return pygame.time.get_ticks()/1000

# create main function/game loop
def main():

	# initialize pygame
	pygame.init()

	# create clock object for time keeping
	clock = pygame.time.Clock()

	# create screen object to draw to
	screen = pygame.display.set_mode((width, height))

	# set j-frame title
	pygame.display.set_caption("Bouncing Ball")

	# fill background
	screen.fill(WHITE)

	# update screen
	pygame.display.update()

	# create list to store balls
	ball_collection = []

	while True:

		for event in pygame.event.get():

			# monitor events, allow quit action
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

			# monitor for mouse clicks
			if event.type == pygame.MOUSEBUTTONUP:

				# get mouse click position
				pos = pygame.mouse.get_pos()

				# create a new ball object at current time
				temp_ball = Ball(get_time(), center=pos)

				# add ball object to collection
				ball_collection.append(temp_ball)

		# check if list contains any balls
		if ball_collection:

			# look through balls
			for i, ball in enumerate(ball_collection):

				# get current time for velocity calculation
				ball_velocity = ball.velocity(get_time())

				# multiply arbitrary number of pixels by velocity
				ball.y += 1 * ball_velocity


				if ball.y + ball.radius >= height:

					# when ball hits the bottom, reverse the velocity
					ball.y = height - ball.radius
					ball.vel = -ball.velocity(get_time())
					ball.t = get_time()

				# draw ball to screen
				ball.draw_ball(screen)

		# update screen
		pygame.display.update()
		pygame.display.flip()

		# limit frame rate to 20 fps
		clock.tick(20)

		# fill over last object
		screen.fill(WHITE)

# call main function and launch game
if __name__ == "__main__":
	main()