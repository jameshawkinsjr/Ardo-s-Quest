def watch():
	print "You glance down at your Ultra Gym Bro Watch Plus XL(TM)"
	print "\t Your Strength is " + str(STRENGTH)
	print "\t Your Stamina is " + str(STAMINA)
	print "\t It is Day " + str(DAYS)

def add_day():
	global DAYS
	DAYS += 1

def add_strength(amount):
	global STRENGTH
	STRENGTH += amount
	print "\t**You gain %d strength. Now you have %d strength**" % (amount, STRENGTH)
	# if all(x in COLLECTIBLES for x in ['Dumbbell', 'Treadmill', 'Barbell']) is True and STRENGTH > 30:

def add_collectible(item):
	COLLECTIBLES.append(item)
	print "\t**YOU UNLOCKED [Gym Equipment] %s**" % (item)

def remove_strength(amount):
	global STRENGTH
	STRENGTH -= amount
	print "\t**You lose %d strength. Now you have %d strength**" % (amount, STRENGTH)



def add_charisma(amount):
	global CHARISMA
	CHARISMA += amount
	print "\t**You gain %d charisma. Now you have %d charisma**" % (amount, CHARISMA)


def remove_charisma(amount):
	global CHARISMA
	CHARISMA -= amount
	print "\t**You lose %d charisma. Now you have %d charisma**" % (amount, CHARISMA)


def add_stamina(amount):
	global STAMINA
	STAMINA += amount
	print "\t**You gain %d stamina. Now you have %d stamina**" % (amount, STAMINA)

def add_money(amount):
	global MONEY
	MONEY += amount
	print "\t**$%d added to your wallet. Now you have $%d**" % (amount, MONEY)

def remove_money(amount):
	global MONEY
	MONEY -= amount
	print "\t**$%d removed from your wallet. Now you have $%d**" % (amount, MONEY)

def remove_stamina(amount):
	global STAMINA
	STAMINA -= amount
	print "\t**You lose %d stamina. Now you have %d stamina**" % (amount, STAMINA)

def wrong_choice():
	idiot = [
		"You lunkhead. That wasn't an option. Try again.",
		"Maybe you should go to school instead of the gym. Try again.",
		"You're an idiot. That wasn't an option. Try again."
		]
	print idiot[randint(0, len(idiot)-1)]
	print "\n"
	remove_strength(1)

def gym_bag():
	print "You unzip your gym bag and look inside. Right now, you have:"
	if not GYMBAG and not COLLECTIBLES:
		print "\t - Nothing"
	for i in GYMBAG:
		print "\t- %s" % i 
	for i in COLLECTIBLES:
		print "\t- [Gym Equipment] %s" %i

def add_item(item):
	POSSE.append(item)
	print "\t**%s was added to your gym bag**" % (item)

def remove_item(item):
	POSSE.remove(item)
	print "\t**%s was removed from your gym bag**" % (item)


def gym_POSSE():
	print "You glance at FB Messenger to see who is going to hit the gym with you:"
	if not POSSE:
		print "\t- No one"
	for i in POSSE:
		print "\t- %s" % i 

def add_member(member):
	POSSE.append(member)
	print "\t**%s was added to the group 'Gym Broz'**" % (member)

def remove_member(member):
	POSSE.remove(member)
	print "\t**%s was removed from the group 'Gym Broz'**" % (member)