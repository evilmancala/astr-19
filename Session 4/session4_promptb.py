#Import
from session4_prompt import Ibex

def main():
#new species
	nubian = Ibex(name="Nubian Ibex")

	print(nubian.name)
	print(nubian.limblength)
	print(nubian.height)
	print(nubian.eyes)
	print(nubian.tail)
	print(nubian.furry)

	print()

#run main
if __name__=="__main__":
	main()