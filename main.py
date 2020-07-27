import random

print("--- Welcome To Rock,Paper,Scissors Powered By Python ---\n\n")

options=['Rock','Paper','Scissor']

def initialize():
	init=input("Enter 's' to start \n")
	if(init=="S" or init=='s'):
		start()
	else:
		print("Wrong Choice\n\n")
		initialize()

def predict(choice):
	cpu=random.randrange(1,4)
	print("\nYou - "+options[choice-1]+"\nCPU - "+options[cpu-1])
	if((choice==1 and cpu==1) or (choice==2 and cpu==2) or (choice==3 and cpu==3)):
		print("\nDraw")
		
	elif((choice==1 and cpu==3) or (choice==2 and cpu==1) or (choice==3 and cpu==2)):
		print("\nYou Won")
		
	else:
		print("\nCPU Won")
		
def start():
	print("1 - Rock, 2 - Paper, 3 - Scissor")
	choice=int(input("\nEnter your choice "))
	if(choice<1 or choice >3):
		print("\nInvalid Choice\n")
		start()
		return
		
	predict(choice)
	
initialize()




