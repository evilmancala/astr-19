'''
Write a Python program that declares a class 
describing your favorite animal. 

Do the data members of the class represent the 
following physical parameters of the animal: 
	length of the arms (float), 
	length of the legs (float), 
	number of eyes (int), 
	does it have a tail? (bool), 
	is it furry? (bool). 

#------------------------------------

Write an initialization function that 
sets the values of the data members when 
an instance of the class is created. 

#------------------------------------

Write a member function of the class to print out 
and describe the data members representing the 
physical characteristics of the animal.
'''

#------------------------------------

#Creating a class for an ibex!
#Had to swap arm and leg length because they are usually
#the same for most animals. 

#Now they have been changed to "limb length" and "height".

import random

#^^ for height and limbs

class Ibex:
	#initialize the class
	def __init__(self,name="Ibex",
		eyes=2,tail=True,furry=True):

		self.name = name
		self.limblength = random.randrange(70,100) 
		self.height = random.randrange(120,140)
		self.eyes = eyes
		self.tail = tail
		self.furry = furry



