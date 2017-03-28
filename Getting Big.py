from time import sleep
from sys import exit
import time
import sys
from random import randint


# Character Stats

STRENGTH = 5
STAMINA = 100
DAYS = 1
CHARISMA = 0
NAME = ""
MONEY = randint(5,7)
GYMBAG = []
POSSE = []
LOCKERNUMBER = 0
LOCKERCOMBO = 0
COLLECTIBLES = []

def watch():
	print "You glance down at your Ultra Gym Bro Watch Plus XL(TM)"
	print "\n\t Your Strength is " + str(STRENGTH)
	print "\t Your Stamina is " + str(STAMINA)
	print "\t It is Day " + str(DAYS)
	print "\n"

def add_day():
	global DAYS
	DAYS += 1

def add_strength(amount):
	global STRENGTH
	STRENGTH += amount
	print "\t**You gain %d strength. Now you have %d strength**" % (amount, STRENGTH)
	if 'Dumbbell' in COLLECTIBLES and 'Treadmill' in COLLECTIBLES and 'Barbell' in COLLECTIBLES and STRENGTH > 40:
		a_map = Map('you_win')
		a_game = Engine(a_map)
		a_game.play()


def add_collectible(item):
	COLLECTIBLES.append(item)
	print "\t**You unlocked '[COLLECTIBLE] %s'**" % (item)
	if 'Dumbbell' in COLLECTIBLES and 'Treadmill' in COLLECTIBLES and 'Barbell' in COLLECTIBLES and STRENGTH > 40:
		a_map = Map('you_win')
		a_game = Engine(a_map)
		a_game.play()

def remove_strength(amount):
	global STRENGTH
	STRENGTH -= amount
	print "\t**You lose %d strength. Now you have %d strength**" % (amount, STRENGTH)
	if STRENGTH <= 0:
		a_map = Map('you_lose')
		a_game = Engine(a_map)
		a_game.play()
	
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
	if STAMINA <= 0:
		a_map = Map('no_stamina')
		a_game = Engine(a_map)
		a_game.play()

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
	print "You look inside your gym bag. Right now, you have:"
	if not GYMBAG and not COLLECTIBLES and MONEY == 0:
		print "\t - Nothing"
	for i in GYMBAG:
		print "\t- %s" % i 
	for i in COLLECTIBLES:
		print "\t- [COLLECTIBLE] %s" %i
	if MONEY > 0:
		print "\t - $%d" % MONEY 

def add_item(item):
	GYMBAG.append(item)
	print "\t**%s was added to your gym bag**" % (item)

def remove_item(item):
	GYMBAG.remove(item)
	print "\t**%s was removed from your gym bag**" % (item)


def gym_posse():
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


# Scenes

class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('you_win')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
		current_scene.enter()

# Welcome

class Welcome(Scene):


	titles = [
		"Tiny",
		"Little Boy",
		"the smallest man alive,",
		"Small",
		"Weakling",
		"Chicken Legs",
		"Spaghetti Arms",
		"Little Boy",
	]

	def enter(self):
		if DAYS == 1:
			print "\n"
			print "=" * 60
			print "\n"
			sleep(1)
			print "Welcome to 'Getting Big' featuring... Wait, what is your name?"
			print "\n"
			global NAME 
			NAME = raw_input("[Name] ")
			if NAME.lower() != 'ardo':
				sleep(1)
				print "\nHmm... I don't really like %s. I'm going to call you Ardo." % NAME
			sleep(1)
			print "\nWelcome to 'Getting Big' featuring %s Ardo!\n" % (Welcome.titles[randint(0, len(self.titles)-1)])
			sleep(1)
			print "The Objectives of this game are:"
			print "\t - Get to 40 STRENGTH"
			print "\t - Gather all 3 COLLECTIBLE items"
			print "\t - Do this in as few days as possible"
			print "\n"
			sleep(1)
			next_step = raw_input("Press Enter to get started \n")
			if next_step == "":
				sleep(1)				
				return '555_office'
			else:

				return next_step


# Locations

class Office_555(Scene):

	things = [
		"your last meeting.",
		"eating a large pizza.",
		"staring longingly out the window.",
		"acting like you've been working for a few hours.",
		"daydreaming about being big.",
		"wondering if the pope ever just wears regular clothes.",
		]

	workout = [
		"bicep day",
		"chest day",
		"back day",
		"shoulder day",
		"tricep day",
		"leg day",
		]

	def enter(self):
		print "\n"
		print "=" * 60
		print "\n"
		print "You're sitting at 555." 
		print "You look at the clock; It's 5:%dpm on %s (your favorite day)." % (randint(10,50), self.workout[randint(0, len(self.workout)-1)]) 
		print "You just finished %s" % self.things[randint(0, len(self.things)-1)]
		print "\n"
		sleep(1)
		gym_bag()
		print "\n"
		sleep(1)
		watch()
		sleep(1)
		print "Do you SKIP the gym and eat pizza or GO get big?"

		while True:
			action = raw_input("\n['SKIP' or 'GO'] ")

			if action.lower() == "skip":
				return 'try_again'
	
			elif action.lower() == "go":
				print "\nThat's how you get big."
				print "Are you going to go to GLOBO FITNESS or WELLNESS CENTER?\n"
					
				while True:
					action = raw_input("['GLOBO FITNESS' or 'WELLNESS CENTER'] ")
					if action.lower() == "globo fitness":
						print "\n"
						print "Nice choice, broseph!"
						print "Before you go, do you grab some MONEY or your MEMBERSHIP CARD?\n"
						while True:
							action = raw_input("['MONEY' or 'CARD'] ")
							if action.lower() == "money":
								print "\n"
								add_money(randint(7,12))								
								break
							elif action.lower() == "card":
								print "\n"
								add_item("MEMBERSHIP CARD")
								break
							else:
								wrong_choice()
						print "\n"
						print "=" * 60
						print "\n\t ** You leave the office to hop on MUNI **"

						return 'muni_station'
		
					elif action.lower() == "welness center":
						print "\n"
						print "There's no saving you."
						remove_strength(2)
						return 'try_again'
	
					else:
						wrong_choice()
				
			else:
				wrong_choice()


class MuniStation(Scene):

	def enter(self):
		print "\n"
		sleep(1)
		print "You enter the dark, seedy, underbelly of the SF Muni."
		print "The station is packed with people."
		print "As you're walking down the stairs, the train comes to screeching halt."
		print "You have to run to catch the train.\n"
		remove_stamina(5)
		print "\nWhen you get to the train, you find a PROTEIN SHAKE under the seat.\n"
		while True:
			action = raw_input("[Drink the PROTEIN SHAKE? 'Y/N'] ")
			if action.lower() == "y":
				print "\nThat's disgusting. It was very moldy.\n"
				remove_strength(2)
				remove_stamina(20)
				break
			elif action.lower() == "n":
				print "\nSmart move. I think it was super moldy.\n"
				break
			else:
				wrong_choice()
		print "\nMuni arrives at Van Ness Station -- this is your stop."
		return 'passing_1455'


class Passing1455(Scene):

	def enter(self):
		print "\n"
		sleep(1)
		print "As you exit the Muni station, your next move is to cross the"
		print "deserted plains of the 1455 Market Street entrance, dodging"
		print "invitations to 'hit the gym' from unwanted gym bros."
		sleep(1)
		print "\n Do you continue or turn back?"
		while True:
			action = raw_input("['CONTINUE' or 'TURN BACK'] ")

			if action.lower() == "turn back":
				return 'try_again'
	
			elif action.lower() == "continue":
				print "\nBrave man. You continue your journey to the Mecca."
				break
	
			else:
				wrong_choice()
		sleep(1)
		print "\n\t**A pack of WILD GYM BROS appear!**"
		print "\nGYM BRO TIM: What's up dude. Ready to be small?"
		print "GYM BRO JAMES: You know what I always say. Triceps are just as"
		print "GYM BRO JAMES: important to filling out your shirt sleeves as biceps."
		print "GYM BRO ALEX is nowhere to be found"
		print "GYM BRO PETER is with one of his ex-girlfriends"
		sleep(1)
		print "\nWho are you going to visit the Swole Palace with?"
		while True:
			action = raw_input("[Invite GYM BRO TIM? 'Y/N'] ")
			if action.lower() == "y":				
				print "\n"
				add_member("GYM BRO TIM")
				print "\t**GYM BRO TIM slows your party down**"
				remove_strength(2)
				remove_stamina(5)
				print "\n"
				break
			elif action.lower() == "n":
				print "Good move."
				print "\n"
				break
			else:
				wrong_choice()
		while True:
			action = raw_input("[Invite GYM BRO JAMES? 'Y/N'] ")
			if action.lower() == "y":
				print "\n"
				add_member("GYM BRO JAMES")
				print "\t**GYM BRO JAMES boosts your party**"
				add_strength(5)
				remove_stamina(20)
				print "\n"
				break
			elif action.lower() == "n":
				print "\nThat was a mistake."
				print "\n"
				break
			else:
				wrong_choice()
		if not POSSE:
			print "Looks like you're alone today."
		print "You continue towards the Muscle Factory."
		return 'gym_entrance'		

class GymEntrance(Scene):

	def enter(self):
		sleep(1)
		print "\nYou finally made it to the Temple of Gains"
		print "Now you have to face YOUSEF, the Entrance Troll."
		print "\nYOUSEF: Welcome to the Monastery of Muscle, bro!"
		print "YOUSEF: To enter this santuary, you must scan your MEMBERSHIP CARD."
		print "\n"
		while True:
			action = raw_input("[Scan your MEMBERSHIP CARD? 'Y/N'] ")
			if action.lower() == "y":
				if "MEMBERSHIP CARD" in GYMBAG:
					print "You scan your MEMBERSHIP CARD and are granted access into the Temple."
					print "\n\t**YOUSEF gives you a fistbump**"
					add_strength(2)
					break
				else:
					print "You didn't grab your MEMBERSHIP CARD."
					print "\nDo you bribe YOUSEF with $5?"
					while True:
						bribe = raw_input("[BRIBE YOUSEF? 'Y/N'] ")
						if bribe.lower() == "y":
							print "You slip YOUSEF a $5 bill\n"
							remove_money(5)
							break							
						elif bribe.lower() == "n":
							print "You can't get into the gym."
							return 'try_again'
						else:
							wrong_choice()
					break
			elif action.lower() == "n":
				return 'try_again'
			else:
				wrong_choice()
		print "\nNow that you made it inside, do you purchase PREWORKOUT for $5?"
		while True:
			action = raw_input("[Purchase PREWORKOUT? 'Y/N'] ")
			if action.lower() == "y":
				if MONEY >= 5:
					print "You purchased PREWORKOUT\n"
					add_item("PREWORKOUT")
					add_stamina(10)
					remove_money(5)
				else:
					print "You don't have enough money"
					print "You feel tired.\n"
					remove_stamina(10)
				break
			elif action.lower() == "n":
				print "You decide not to purchase PREWORKOUT."
				print "You feel tired.\n"
				remove_stamina(10)
				break
			else:
				wrong_choice()
		print "\nHow about an awesome TEMPLE OF GAINZ TANKTOP for $5?"
		while True:
			action = raw_input("[Purchase TANKTOP? 'Y/N'] ")
			if action.lower() == "y":
				if MONEY >= 5:
					print "You purchased TANKTOP\n"
					add_item("TANKTOP")
					remove_money(5)
				else:
					print "\nYou don't have enough money"
				break
			elif action.lower() == "n":
				print "You decide not to purchase TANKTOP."
				break
			else:
				wrong_choice()
		sleep(1)
		print "\n\t** YOUSEF looks around, suspiciously **"
		sleep(1)
		print "\nYOUSEF (whispering): Hey buddy - got a hot tip for you."
		print "YOUSEF (whispering): What do you say, five bucks?"
		while True:
			action = raw_input("[Give YOUSEF $5 for tip? 'Y/N'] ")
			if action.lower() == "y":
				if MONEY >= 5:
					print "\nYOUSEF (whispering): Check out locker 88, combo 2828."
					remove_money(5)
				else:
					print "\nYou don't have enough money. Maybe tomorrow."
				break
			elif action.lower() == "n":
				print "You tell YOUSEF that you're not interested."
				break
			else:
				print "\nYOUSEF (whispering): I'm not sure what that means..."
		print "\n"
		print "You walk into the Temple of Brodin and grab a towel."
		print "\n"
		return 'locker_room'

class LockerRoom(Scene):

	def enter(self):
		global LOCKERNUMBER
		if LOCKERNUMBER == 0:	
			print "Upon entering the LOCKER ROOM, you look around for a locker."
			print "Which locker number do you choose?"
			while True:
				LOCKERNUMBER = raw_input("[Which Locker Number?] ")
				if LOCKERNUMBER.isdigit() is False:
					print "The lockers have NUMBERS on them."
				elif int(LOCKERNUMBER) == 88 and "Dumbbell" not in COLLECTIBLES:
					print "It looks like this one is already locked. Try a combo?"
					while True:
						action = raw_input("[Attempt a combo] ")
						if action == str(2828):
							print "Huh... That worked.\n"
							sleep(1)
							print "\t*Zelda treasure chest opening sound*\n"
							sleep(1)
							add_collectible("Dumbbell")
							print "\n"
							print "Now which locker do you want to put your stuff in?"
							break
						else:
							print "Didn't work. Back to the drawing board."
							break
				elif int(LOCKERNUMBER) > 0 and int(LOCKERNUMBER) < 200 and int(LOCKERNUMBER) % 2 == 0:
					break
				elif int(LOCKERNUMBER) > 0 and int(LOCKERNUMBER) < 200 and int(LOCKERNUMBER) % 2 == 1:
					print "That locker is taken. Try another."
				else:
					print "There isn't a locker with that number. Look again."
			print "You've chosen locker %d." % int(LOCKERNUMBER)
			while True:
				action = raw_input("[Choose your 4-digit combo] ")
				if action.isdigit() and len(action) == 4:
					LOCKERCOMBO = action
					print "You've chosen combination %d." % int(LOCKERCOMBO)
					break
				else:
					print "Error: Combo must be 4 numbers"
			print "You're all set. Time to go get swole."
			sleep(1)
			return 'gym_floor'
		else:
			print "Back in the Locker Room. What was your locker number again?"
			count = 0
			while (count < 5):
				GUESS = raw_input("[Which Locker Number?] ")
				if GUESS == LOCKERNUMBER:
					print "Good thing you remembered. Now, to get into your locker."
					count2 = 0
					while (count2 < 4):
						GUESS2 = raw_input("[What was your combo?] ")
						if GUESS2 == LOCKERCOMBO:
							print "Good job!"
							break
						else:
							print "Incorrect guess. You have ",(4 - count2)," guesses left"
							count2 += 1
				else:
					print "Incorrect guess. You have ",(5 - count)," guesses left"
					count += 1
			print "You got your stuff"

class GymFloor(Scene):

	def enter(self):
		sleep(2)
		if "GYM BRO ALEX" not in POSSE:
			print "\n\t ** GYM BRO ALEX appears **"
			print "\nGYM BRO ALEX: What's up guys? What workout are you doing today?"
			workout = raw_input("[What are you doing today?] ")
			print "\nGYM BRO ALEX: Nice dude. I just did that yesterday, but I can work in with you."
			option = raw_input("\n[Let GYM BRO ALEX join 'GYM BROZ'?] Y/N ")
			if option.lower() == "y" or option.lower() == "yes":
				add_member("GYM BRO ALEX")
			else:
				print "\n\t ** You walk away **"
		print "\nWhere do you go next?"
		print """
Enter "BACK" for Deadlift (+10 Strength, -50 Stamina)
Enter "CHEST" for Bench Press (+7 Strength, -32 Stamina)
Enter "BICEPS" for Bicep Busters (+2 Strength, -9 Stamina)
Enter "SHOULDERS" for Military Press (+2 Strength, -14 Stamina)
Enter "LEGS" for Squats (+30 Strength, -90 Stamina)
Enter "TRICEPS" for Skull Crushers (+3 Strength, -12 Stamina)
Enter "LOCKER" to return to the Locker Room
Enter "WATCH" to check your stats
Enter "SHOWER" to hit the showers
Enter "BROZ" to check who is in your group
Enter "BAG" to check your gym bag
Enter "HOME" to leave the gym
			"""
		while True:
			action = raw_input("[Choose an option] ")
			if action.lower() == "back":
				return 'deadlift_platform'
			elif action.lower() == "chest":
				return 'bench_press'
			elif action.lower() == "biceps":
				return 'bicep_busters'
			elif action.lower() == "shoulders":
				return 'military_press'
			elif action.lower() == "legs":
				return 'squats'
			elif action.lower() == "triceps":
				return 'skull_crushers'
			elif action.lower() == "locker":
				return 'locker_room'
			elif action.lower() == "home":
				return 'try_again'
			elif action.lower() == "shower":
				return 'showers'
			elif action.lower() == 'watch':
				watch()
				return 'gym_floor'
			elif action.lower() == 'broz':
				gym_posse()
				return 'gym_floor'	
			elif action.lower() == 'bag':
				gym_bag()
				return 'gym_floor'
			else: 
				wrong_choice()


class DeadliftPlatform(Scene):

	def enter(self):
		print "Has anyone ever told you that deadlifts"
		print "are God's favorite exercise? Well, now you know."
		print "Deadlifts require a lot of STAMINA, but you are"
		print "rewarded with a lot of STRENGTH. How many sets"
		print "do you want to do?"
		while True:
			action = raw_input("[How many sets of Deadlifts?] ")
			if action.isdigit() and STAMINA - (50 * int(action)) >= 0:
					add_strength(int(action) * 10)
					remove_stamina(int(action) * 50)
					break
			elif action.isdigit() and STAMINA - (50 * int(action)) < 0:
				print "You don't have enough STAMINA."
				break
			else:
				wrong_choice()
		return 'gym_floor'


class BenchPress(Scene):

	def enter(self):
		print "\nBench press. Nice."
		sleep(1)
		print "\nYou see a cute CUTE SMALL ASIAN GYM CHICK checking you out at the other bench."
		print "Do you talk to her?"
		while True:
			action = raw_input("[Chat with cute CUTE SMALL ASIAN  CHICK? 'Y/N'] ")
			if action.lower() == "y":
				print "You approach the CUTE SMALL ASIAN CHICK."
				sleep(1)
				print "\n\t** CUTE SMALL ASIAN CHICK suddenly turns into a GAINZ GOBLIN **"
				print "\nGAINZ GOBLIN: If you give me a TANKTOP, I won't steal your gainz.\n"
				sleep(1)
				action = raw_input("[Give TANKTOP to GAINZ GOBLIN? 'Y/N'] ")
				if "TANKTOP" in GYMBAG:
					if action.lower() == "y":
						print "You give TANKTOP to GAINZ GOBLIN"
						remove_item("TANKTOP")
						print "GAINZ GOBLIN turns back into CUTE SMALL ASIAN CHICK"
						add_member("CUTE SMALL ASIAN CHICK")
						add_strength(2)
				else:
					print "You have no TANKTOP to give.\n"
					remove_strength(5)
				break
			elif action.lower() == "n":
				while True:
					action = raw_input("[How many sets of Bench Press?] ")
					if action.isdigit() and STAMINA - (32 * int(action)) >= 0:
						add_strength(int(action) * 7)
						remove_stamina(int(action) * 32)
						break
					elif action.isdigit() and STAMINA - (32 * int(action)) < 0:
						print "You don't have enough STAMINA."
						break
					else:
						wrong_choice()
				break

			else:
				print "You really are socially awkward. Try again."				
		return 'gym_floor'

class BicepBusters(Scene):

	def enter(self):
		print "You approach the cables to hit BICEPS real hard."
		print "It's a trap!"
		print "\n\t**The TALKER approaches you**"
		print "\nTALKER: Hey guys."
		sleep(2)
		print "TALKER: What's up?"
		sleep(2)
		print "TALKER: Crazy busy here, huh?"
		sleep(2)
		print "TALKER: I'm doing some back workouts today."
		sleep(2)
		print "TALKER: Thinking about switching gyms."
		sleep(2)
		raw_input("[Do you 'ENGAGE' or 'IGNORE'?] ")
		sleep(2)
		print "TALKER: How is work?"
		sleep(2)
		print "TALKER: Everything has been crazy lately, know what I mean?"
		sleep(2)
		print "TALKER: Whoa Ardo, did are those new shoes?"
		sleep(2)
		print "TALKER: How do you like my new BOX shirt?"
		sleep(2)
		if "GYM BRO JAMES" in POSSE:
			print "TALKER: GYM BRO JAMES -- haven't shaved in a few days I see!"
			sleep(2)
			print "TALKER: Growing a beard or what?"
			sleep(2)
		if "GYM BRO TIM" in POSSE:
			print "TALKER: What's up GYM BRO TIM?"
			sleep(2)
		print "TALKER: I think this blue is a good color."
		sleep(2)
		print "TALKER: What do you guys normally do on back day?"
		sleep(2)
		print "TALKER: I haven't figured out my routine."
		sleep(2)
		print "TALKER: Anyway. Good talking -- see you guys later."
		sleep(2)
		print "\n\t**The TALKER leaves**"
		sleep(2)
		print "\nThat was painful. You're too tired to do Bicep Busters now."
		remove_stamina(10)
		return 'gym_floor'

class MilitaryPress(Scene):

	def enter(self):
		print "The goal of Military Press is to make it look like you're always shrugging."
		while True:
				action = raw_input("[How many sets of military press?] ")
				if action.isdigit() and STAMINA - (80 * int(action)) >= 0:
					print "\n"
					add_strength(int(action) * 30)
					remove_stamina(int(action) * 90)
					break
				elif action.isdigit() and STAMINA - (80 * int(action)) < 0:
					print "You don't have enough STAMINA."
					break
				else:
					wrong_choice()
		return 'gym_floor'

class Squats(Scene):

	def enter(self):
		if "CUTE SMALL ASIAN CHICK" not in POSSE:
			print "All racks are taken. If you had CUTE SMALL ASIAN CHICK in your party..."
			print "Maybe you could get a rack"
			return 'gym_floor'
		else:
			while True:
				action = raw_input("[How many sets of squats?] ")
				if action.isdigit() and STAMINA - (80 * int(action)) >= 0:
					print "\n"
					add_strength(int(action) * 30)
					remove_stamina(int(action) * 90)
					break
				elif action.isdigit() and STAMINA - (80 * int(action)) < 0:
					print "You don't have enough STAMINA."
					break
				else:
					wrong_choice()
			return 'gym_floor'

class SkullCrushers(Scene):

	def enter(self):
		print "You grabbed a bench to hit some skull crushers"
		while True:
			action = raw_input("[How many sets of skull crushers?] ")
			if action.isdigit() and STAMINA - (12 * int(action)) >= 0:
				print "\n"
				add_strength(int(action) * 3)
				remove_stamina(int(action) * 12)
				break
			elif action.isdigit() and STAMINA - (12 * int(action)) < 0:
				print "You don't have enough STAMINA."
				break
			else:
				wrong_choice()
		sleep(2)
		if "Barbell" not in COLLECTIBLES:
			print "\n\t ** A shadowy figure appears over you **"
			print(".")
			sleep(1)
			print(".")
			sleep(1)
			raw_input("\n[... are you Ready?]")
			sleep(2)
			print "\nSHADOWY BROSEIDON: Answer my riddle and you will be blessed with sleeve-busting Triceps"
			print "SHADOWY BROSEIDON: Fill in the blanks from the 'Flexidus 7:12-16'"
			sleep(2)
			print """
\t>12 - Honor your Sisters and Brothers, so that you may live long in Swolehalla.
\t>13 - You shall push beyond your ____, for there is where Gains lie.
\t>14 - You shall not commit _____.
\t>15 - You shall not _____ Gains.
\t>16 - You shall not give fake lifts. ____ must be impeccable.
				"""
			sleep(1)
			print "\n"
			print "=" * 60
			print "\n"
			print """
SHADOWY BROSEIDON: Choose wisely...

	>1. Limits, Reps, Forego, Spotting
	>2. Reps, Gainz, Give, Physique
	>3. Pump, Cardio, Steal, Form
	>4. Comfort Zone, Swoleshaming, Earn, Lifts
				"""
			print "\n"
			print "=" * 60
			while True:
				action = raw_input("[What do you choose?] ")
				if action.isdigit() and int(action) == 3:
					print "\nSHADOWY BROSEIDON: You have chosen wisely. Take this BARBELL and continue your quest."
					add_collectible("Barbell")
					break
				elif action.isdigit() and (int(action) == 1 or int(action) == 2 or 	int(action) == 4):
					print "\nSHADOWY BROSEIDON: The answer you have chosen is incorrect."
					print "\n"
					remove_strength(3)
					break
				else:
					print "\nSHADOWY BROSEIDON: Try again."
			print "\n\t ** The shadowy figure vanishes in a poof of smoke **"
		return 'gym_floor'

class Showers(Scene):

	def enter(self):
		print "After a good workout, it's time to hit the showers."
		if "LOOKER" not in POSSE:
			print "You drop off your clothes and pull back the shower door to be confronted with the LOOKER."
			print "You maintain eye contact with him for a few seconds."
			option = raw_input("\n[Let LOOKER join 'GYM BROZ'?] Y/N ")
			if option.lower() == "y" or option.lower() == "yes":
				add_member("LOOKER")
				add_collectible("Treadmill")
			else:
				print "\n\t ** You walk away **"
				print "\n\t ** You watch the LOOKER put a '[COLLECTIBLE] Treadmill' into his gym bag **"

		return 'gym_floor'

# User State

class TryAgain(Scene):

	motivations = [
		"Time to go home and try again tomorrow.",
		"Stay small, my friend.",
		"There's always tomorrow, I guess.",
		"At this rate, we might have to kick you out of 'Gym Broz'.",
		"A little embarassing, but maybe you'll get big tomorrow.",
	]

	def enter(self):
		global NAME
		print "\n"
		print TryAgain.motivations[randint(0, len(self.motivations)-1)]
		add_day()
		global STAMINA
		STAMINA = randint(90,100)
		global POSSE
		POSSE = []
		global MONEY
		MONEY = randint(4,6)
		global GYMBAG
		GYMBAG = []
		global LOCKERNUMBER
		LOCKERNUMBER = 0
		global LOCKERCOMBO
		LOCKERCOMBO = 0
		sleep(1)
		print "\n"
		print "=" * 60
		print "\n"
		sleep(1)
		print "\t**STARTING DAY %d**" % DAYS
		print "\t**Your Stamina refills to 100**"
		if DAYS % randint(2,5) == 0:
			print "\t**You lose 1 strength for taking so long.**"
			global STRENGTH
			STRENGTH -= 1
		sleep(1)
		return '555_office'

class RanOutOfStamina(Scene):

	def enter(self):
		sleep(1)
		print "You ran out of Stamina."
		print "\n"
		sleep(1)
		return 'try_again'
		

class YouWin(Scene):

	def enter(self):
		print "\n"
		print "=" * 60
		print "\n"
		sleep(1)
		print "\t** Congratulations! You win! **"	
		print "\n\t** It took you %d days **" % DAYS
		print "\n\t** You finished with %d strength **\n\n" % STRENGTH
		print "=" * 60
		print "\n"
		exit(1)

class YouLose(Scene):

	def enter(self):
		print "\n"
		print "=" * 60
		sleep(1)
		print "\n\t** Wow. It's really hard to actually *lose* this game **"
		sleep(1)
		print "\n\t** But you managed to do it **"
		sleep(1)
		print "\n\t** You lost. Forever small. **\n"
		sleep(1)
		print "=" * 60
		print "\n"
		exit(1)




# Start Game

class Map(object):

	scenes = {
		'welcome': Welcome(),
		'555_office': Office_555(),
		'muni_station': MuniStation(),
		'passing_1455': Passing1455(),
		'gym_entrance': GymEntrance(),
		'locker_room': LockerRoom(),
		'deadlift_platform': DeadliftPlatform(),
		'bench_press': BenchPress(),
		'bicep_busters': BicepBusters(),
		'military_press': MilitaryPress(),
		'squats': Squats(),
		'skull_crushers': SkullCrushers(),
		'showers': Showers(),
		'gym_floor': GymFloor(),
		'no_stamina': RanOutOfStamina(),
		'try_again': TryAgain(),
		'you_win': YouWin(),
		'you_lose': YouLose(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val 

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('welcome')
a_game = Engine(a_map)
a_game.play()

