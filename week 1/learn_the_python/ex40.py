class accHolder(object):
	
	def __init__(self,name,balance = 0.0):
		self.name = name
		self.balance = balance
	def deposit(self,amount):
		self.balance += amount
		print "%s your current balance is %f"%(self.name,self.balance)
	def withdraw(self,amount):
		if self.balance-amount < 0 :
			print "withdrawn of amount",amount,"not possible "
		else :
			self.balance -=amount
			print "%s your balance is %f"%(self.name,self.balance)

chanish = accHolder('chanish')
deposit = int(input("enter the amout you'd like to deposite"))
chanish.deposit(deposit)
withdraw = int(input("how much money you'd like to withdraw"))
chanish.withdraw(withdraw)


		
