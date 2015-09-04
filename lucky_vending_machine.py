""" 
--------------------------------------------------------LUCKY VENDING MACHINE-----------------------------------------------------------------------------------
"""
import sys
import random 
name = None


class player(object):
	def __init__(self,playerName,prizes = '', worth = 0, spent = 0):
		self.playerName = playerName
		self.prizes = prizes
		self.spent = spent
		self.worth = worth

	def playerStat(self):
		print self.playerName,self.prizes,self.worth,self.spent

	def gamble(self,prizes,worth,spent):
		self.prizes += prizes
		self.worth += worth
		self.spent += spent

	def won(self):
		print "You've won So far : ",self.prizes,"is worth of $",self.worth

	
def game_help():
		print """

		-----------------GAME HELP-----------------
		Option 1:
		- Please first create a user 
				choose option 1 to set up a new user
				enter your name make sure your input is not empty
				you'll see option menu again

		Option 2:
		- Make any guess between 1-5 and you can win prizes if you're lucky
			you can win Pen Book DVD Keyboard etc worth 10 times what spent

		Option 3:
			To see What you've won so far
		"""


def luckyVendingMachine():
	global name
	print """
		Welcome to the Lucky Vending Machine
		choose an option and enter an integer value
		==============================
		(1) Set Up New Player
		(2) Guess A Prize
		(3) What Have I Won So Far?
		(4) Display Game Help
		(5) Exit Game"""
	print '\n'	

	prize_dic = {1:('pen ',10,1), 2:('Book ',20,2), 3:('DVD ',30,3), 4:('Mouse ',40,4), 5:('Keyboard ',50,5)}
	emp = ''
	zero = 0

	choice = raw_input()
	
	#Set up a New Player
	if choice == '1':
		name = raw_input('please enter player name\t')
		
		# empty sequences are false in python
		if name and name.strip():

			name = player(name)
			# name.playerStat()
			luckyVendingMachine()
			
		else:
			print '\n ****You must enter Name**** '
			luckyVendingMachine()


			

	elif choice == '2':
	#Guess a prize
		if name is None:
			print 'user does not exist Please Set up New user'
			# print "\nPlayer does not exist \nyou must set up a new Identity: %s"%name
			luckyVendingMachine()

		else:
			print 'Welcome ',name.playerName
			rand_int = random.randint(1, 5)
			# print rand_int
			player_guess = int(raw_input("\nplease guess a number between 1-5 "))
			

			# Checking if user guess is appropriate or not
			if player_guess >=1 and player_guess <=5:
				
				if player_guess == rand_int:
					name.gamble(prize_dic[player_guess][0], prize_dic[player_guess][1], prize_dic[player_guess][2])
					print "Congratulation You've won",prize_dic[player_guess][0],"  worth $",prize_dic[player_guess][1]
					print "you've spent only $",prize_dic[player_guess][2]
					# name.playerStat()
					luckyVendingMachine()

				else:
					print '\n  Sorry you loose It cost you $', prize_dic[player_guess][2],'\n\tBetter luck Next Time'

					name.gamble(emp, zero,prize_dic[player_guess][2])
					# name.playerStat()
					luckyVendingMachine()	
			else:
				print 'Choose between integer 1 to 5'
				luckyVendingMachine()


		pass

	#What i have Won So Far
	elif choice == '3':
		if name is None:
			print "you're new user please setup your account first"
			luckyVendingMachine()
		else:
			name.won()
			luckyVendingMachine()
	
		pass
	#Display Game Help
	elif choice == '4':
		game_help()
		luckyVendingMachine()
		pass

	elif choice == '5':
	#Exit
		sys.exit(1)

	else:
		print "inappropriate choice"
		luckyVendingMachine()

if __name__ == '__main__':
	luckyVendingMachine()
	