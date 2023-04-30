import pygame

class Ball:

	"""
	creates a ball object with default color red
	and default radius 50 pixels

	"""

	def __init__(self, start_time, radius = 50, color = (255,   0,   0), center=(0,0)):
		# create private variables 
		self.__radius = radius
		self.__color = color

		# create public variables
		self.x, self.y = center
		self.vel = 0
		self.t = start_time

	def draw_ball(self, screen):
		# draws circle at specified location
		pygame.draw.circle(screen, self.__color, (self.x, self.y), self.__radius)

	def velocity(self, t):
		# returns next velocity given time and initial velocity
		return self.vel + 9.81 * (t - self.t)
		
	@property
	def radius(self):
		# radius getter
		return self.__radius

	@radius.setter
	def radius(self, radius):
		# radius setter
		self.__radius = radius
