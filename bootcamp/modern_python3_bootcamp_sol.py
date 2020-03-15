 # Set the message variable equal to any string containing a new-line escape sequence
message = "printing in \nnewline"


# Add a string to the mountains variable that when printed results in: /\/\/\
# You will need to use an escape sequence more than once!
mountains = '//\\/\\/\\'


# Set the quotation variable to any string that contains an escaped double quotation mark

quotation = "\"hekki\""

##**************************************************************************************************************##

first = "Rocket"
last = "Raja"

formatted = "First Name: {}, Last Name: {}".format(first,last)
print(formatted)
##**************************************************************************************************************##

# NO TOUCHING PLEASE---------------
from random import randint
choice = randint(1,10)
# NO TOUCHING PLEASE---------------

# YOUR CODE GOES HERE:
if choice == 7:
    print("lucky")
else:
    print("unlucky")
##**************************************************************************************************************##

# NO TOUCHING ======================================
from random import randint
x = randint(-100, 100)
while x == 0:  # make sure x isn't zero
    x = randint(-100, 100)
y = randint(-100, 100)
while y == 0:  # make sure y isn't zero
    y = randint(-100, 100)
# NO TOUCHING ======================================
 
# Don't change the print statements so the tests can pass!
# YOUR CODE GOES HERE vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
 
if x > 0 and y > 0:
    print("both positive")
elif x < 0 and y < 0:
    print("both negative")
elif x > 0 and y < 0:
    print("x is positive and y is negative")
else:
    print("y is positive and x is negative")

##**************************************************************************************************************##

# NO TOUCHING ======================================
from random import choice, randint
 
actually_sick = choice([True, False])
kinda_sick = choice([True, False])
hate_your_job = choice([True, False])
sick_days = randint(0, 10)
# NO TOUCHING ======================================
 
 
calling_in_sick = None  # set this to True or False with Boolean Logic and Conditionals!
 
# Note, we don't need to check if actually_sick == True
#  Instead, just check if actually_sick, since it's a boolean
 
if actually_sick and sick_days > 0:
    calling_in_sick = True
elif kinda_sick and hate_your_job and sick_days > 0:
    calling_in_sick = True
else:
    calling_in_sick = False

##**************************************************************************************************************##


from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	else:
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	else:
		print("computer wins!")	
else:
	print("Please enter a valid move!")
##**************************************************************************************************************##
x = 0
 
for i in range(11,21,2):
        x += i

from random import randint  # use randint(a, b) to generate a random number between a and b
 
number = 0 #store random number in here, each time through
i = 0  # i should be incremented by one each iteration
 
while number != 5: #keep looping while number is not 5
    i += 1
    number = randint(1, 10) #update number to be a new random int from 1-10

##**************************************************************************************************************##

import random

random_number = random.randint(1,10)  # numbers 1 - 10
guess = None

while True:
	guess = input("Pick a number from 1 to 10: ")
	guess = int(guess)
	if guess < random_number:
		print("TOO LOW!")
	elif guess > random_number:
		print("TOO HIGH!")
	else:
		print("YOU WON!!!!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = random.randint(1,10)  # numbers 1 - 10
			guess = None
		else:
			print("Thank you for playing!")
			break


##**************************************************************************************************************##

#########LIST #################

# Define my_stuff
my_stuff = [1, 2, 3, 4, "Camera", 2.5]
# Define nums
nums = list(range(1,100))

# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hanna"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"

sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()

instructors = []
# Add the following strings to the instructors list 
    # "Colt"
    # "Blue"
    # "Lisa"
# Use any of the list methods we've seen to accomplish this:
instructors.extend(["Colt", "Blue", "Lisa"])
instructors.pop()
# Remove the first value in the list
instructors.pop(0)
# Add the string "Done" to the beginning of the list
instructors.insert(0,"Done")
# Run the tests to make sure you've done this correctly!
print(instructors)

#####swap 

name[1],name[0] = name[0],name[1]
##**************************************************************************************************************##


#Using list comprehensions:

    answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
    answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

#Using good old manual loops:

    answer = []
    for person in ["Elie", "Tim", "Matt"]:
        answer.append(person[0])

    answer2 = []
    for num in [1,2,3,4,5,6]:
        if num % 2 == 0:
            answer2.append(num)


##**************************************************************************************************************##
#Using list comprehensions(the more Pythonic way): 

    answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
    #the slice [::-1] is a quick way to reverse a string
    answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

#Without list comprehensions, things are a bit longer:

    answer = []
    for x in [1,2,3,4]:
        if x in [3,4,5,6]:
            answer.append(x)
    answer2 = []
    for name in ["Elie", "Tim", "Matt"]:
        answer2.append(name[::-1].lower())

answer = [val for val in range(1,101) if val % 12 == 0] 

#Using a string (preferable solution):

answer = [char for char in "amazing" if char not in "aeiou"] 

#Using a list:

answer = [char for char in "amazing" if char not in ["a", "e", "i", "o", "u"]] 

answer = [[i for i in range(0,3)] for num in range(0,3)] 

#To generate the following using a nested list comprehension:

    [
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
     ]

#My solution looks like this:

answer = [[i for i in range(0,10)] for num in range(0,10)] 


##**************************************************************************************************************##

#######################DICTIONARY 

artist = {
    "first": "Neil",
    "last": "Young",
}
 
full_name = "{} {}".format(artist["first"],artist["last"])



##**************************************************************************************************************##
donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
 
total_donations = 0
 
for donation in donations.values():
	total_donations += donation

 total_donations = sum(donation for donation in donations.values())

 total_donations = sum(donations.values())

##**************************************************************************************************************##
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!
 
#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}


quantity = bakery_stock.get(food)
if quantity:
    print("{} left".format(quantity))
else:
    print("we don't make that")


##**************************************************************************************************************##
game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]
initial_game_state = dict.fromkeys(game_properties, 0)

##**************************************************************************************************************##

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1} #DON'T CHANGE THIS LINE!
# Make a copy of inventory and save it to a variable called stock_list
stock_list = inventory.copy()
# add the value 18 to stock_list under the key "cookie"
stock_list['cookie'] = 18
# remove 'cake' from stock_list
stock_list.pop('cake')

##**************************************************************************************************************##
playlist = {
	'title': 'patagonia bus', 
	'author': 'colt steele', 
	'songs': [
		{'title': 'song1', 'artist': ['blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['kitty', 'djcat'], 'duration': 5.25},
		{'title': 'meowmeow', 'artist': ['garfield'], 'duration': 2.0}
	]
}

total_length = 0
for song in playlist['songs']:
	total_length += song['duration']

print(total_length)

##**************************************************************************************************************##
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
answer = {list1[i]: list2[i] for i in range(0,3)}

list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
 
dict(zip(list1,list2))  
##**************************************************************************************************************##

person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {thing[0]: thing[1] for thing in person}

answer = {k:v for k,v in person}

answer = dict(person)

##**************************************************************************************************************##
#Using a dictionary comprehension:

answer = {char:0 for char in 'aeiou'} 

#Using dict.fromkeys:


answer = dict.fromkeys("aeiou", 0) 

answer = {count: chr(count) for count in range(65,91)} 

##**************************************************************************************************************##

#################TUPLE 
##########SET

# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1,2,3,4)
 
# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)
 
# 3 - Given the following variable:
values = [10,20,30]
# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
 
# 3 - Given the following variable
stuff = [1,3,1,5,2,5,1,2,5]
 
# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)

s = set([1, 2, 3])

s.add(4)

set1 = {1,2,3,4,5,6}

set1.remove(3)



Set Comprehension

{x**2 for x in range(10)}

# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

def are_all_vowels_in_string(string):
    return len({char for char in string if char in 'aeiou'}) == 5


##**************************************************************************************************************##


def yell(word):
    return f"{word.upper()}!"

def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

def speak(animal='dog'):
    noises = {'pig':'oink', 'duck':'quack', 'cat':'meow', 'dog':'woof'}
    return noises.get(animal, '?')    
##**************************************************************************************************************##
def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0 
        return days[num-1]
    return None

def return_day(week_num):
    day_of_week={1:"Sunday",2:"Monday",3:"Tuesday",4:"Wednesday",5:"Thursday",
    6:"Friday",7:"Saturday"}
    if day_of_week.get(week_num) is None:
        return None
    return day_of_week[week_num]

def return_day(num):
    try:
        return ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"][num-1]
    except IndexError as e:
        return None


def last_element(l):
    if l:
        return l[-1]
    return None

def single_letter_count(string,letter):
	return string.lower().count(letter.lower())   

'''
multiple_letter_count("awesome") # {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1}
'''

# flesh out multiple_letter count:
def multiple_letter_count(word):
    return {x:word.count(x) for x in word}

def list_manipulation(collection, command, location, value=None):
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0,value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection
##**************************************************************************************************************##
def is_palindrome(string):
    return string == string[::-1]
    
def is_palindrome(string):
    stripped = string.replace(" ", "")
    return stripped == stripped[::-1]
##**************************************************************************************************************##


##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']


# returns dict with {student:highest score} USING LIST COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]:max(t[1], t[2]) for t in zip(students, midterms, finals)}


# returns dict with {student:highest score} USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
	zip(
		students,
		map(
			lambda pair: max(pair),
			zip(midterms, finals)
		)
	)
)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
	zip(
		students,
		map(
			lambda pair: ((pair[0]+pair[1])/2),
			zip(midterms, finals)
		)
	)
)




##**************************************************************************************************************##
import keyword as kw

def contains_keyword(*args):
    return any(x for x in args if keyword.iskeyword(x))

import keyword
 
def contains_keyword(*args):
    for item in args:
        if keyword.iskeyword(item): return True
    return False

args = ["hello","False"]

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##
'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''

def extract_full_name(names):
    return [na['first']+' '+na['last'] for na in [n for n in names]]
        
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
##**************************************************************************************************************##


# Introduction

# Your goal in this exercise is to implement two classes, Card  and Deck .

# Specifications

# Card 

#     Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
#     Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
#     Card 's __repr__  method should return the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)

# Deck 

#     Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
#     Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
#     Deck 's __repr__  method should return information on how many cards are in the deck (e.g. "Deck of 52 cards", "Deck of 12 cards", etc.)
#     Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards from the deck (it may need to remove fewer if you request more cards than are currently in the deck!). If there are no cards left, this method should return a ValueError  with the message "All cards have been dealt".
#     Deck  should have an instance method called shuffle  which will shuffle a full deck of cards. If there are cards missing from the deck, this method should return a ValueError  with the message "Only full decks can be shuffled".  shuffle should return the shuffled deck.
#     Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card from the deck and return that single card.
#     Deck  should have an instance method called deal_hand  which accepts a number and uses the _deal  method to deal a list of cards from the deck and return that list of cards.


from random import shuffle

class Card:
    def __init__(self,value,suit):
    	self.suit = suit 
    	self.value = value 
    
    def __repr__(self):
        return "{} of {}".format(self.value,self.suit)


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(value, suit) for suit in suits for value in values]
    
    def __repr__(self):
        return "Deck of {} cards".format(self.count())
    
    def count(self):
        return len(self.cards)
    
    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
        	raise ValueError("All cards have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def deal_card(self):
        return self._deal(1)[0]
    
    def deal_hand(self, hand_size):
        return self._deal(hand_size)
    
    def shuffle(self):
        if self.count() < 52:
        	raise ValueError("Only full decks can be shuffled")
        
        shuffle(self.cards)
        return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()



##**************************************************************************************************************##

-- multiple Inheritance 

class D(B,C):
	pass

Method Resolution Order 


D.__mro__
D.mro()
help(D)

##**************************************************************************************************************##

class User:
	active_users = 0

	@classmethod
	def display_active_users(cls):
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1

	def __repr__(self): #representation method 
		return f"{self.first} is {self.age}"

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,value):
		if value >=0:
			self._age = value
		else:
			raise ValueError("Age shouldn't be negative")
	
	

##**************************************************************************************************************##

'''
generator :

kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''

def make_song(num=99,song="soda"):
    while num >= 0:
        if num >= 2:
            yield "{} bottles of {} on the wall.".format(num,song)
            num -= 1
        elif num == 1:
            yield "Only 1 bottle of {} left!".format(song)
            num -= 1
        elif num == 0:
            yield "No more {}!".format(song)
            num -= 1
    

##**************************************************************************************************************##

# WITHOUT A GENERATOR....
# To generate first 1,000,000 fib numbers, it has to store all of them in a list
def fib_list(max):
     nums = []
     a, b = 0, 1
     while len(nums) < max:
         nums.append(b) 
         a, b = b, a+b
     return nums

# fib_list(1000000)


# USING A GENERATOR...
# To generate first 1,000,000 fib numbers,no list needed!
def fib_gen(max):
    x = 0
    y = 1
    count = 0
    while count < max:
        x, y = y, x + y
        yield x
        count+=1


for n in fib_gen(1000000):
	print(n)


##**************************************************************************************************************##
'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

def get_multiples(num=1,cnt=10):
    for c in range(1,cnt+1):
        yield num*c
        
def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num

##**************************************************************************************************************##
'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''

def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield num
        num += next_num
    
##**************************************************************************************************************##
import time


# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time() # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time # end time - start time
 
 
# SUMMING 10,000,000 Digits With List Comprehension 
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")
##**************************************************************************************************************##

'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(f1,f2):
    with open(f1,"r") as f_r:
        with open(f2,"w") as f_w:
            f_w.write(f_r.read())

##**************************************************************************************************************##
'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(f1):
    with open(f1,"r") as f:
        file_str = f.readline()
        new_dict = dict(lines=len(file_str))
        print(new_dict)

##**************************************************************************************************************##
'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()

        
##**************************************************************************************************************##
'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''

def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
             "words": sum(len(line.split(" ")) for line in lines),
             "characters": sum(len(line) for line in lines) }
        
    
##**************************************************************************************************************##

""" BEAT """

from time import sleep

def current_beat(n):
	i=1
	while i <= n:
		for m in range(1,5):
			yield m
			i += 1

user_ent = int(input())
cb = current_beat(user_ent)
for b in range(user_ent):
	print(next(cb))
	sleep(1)
print("Beat Ends here !! ")
##**************************************************************************************************************##

""" Decorator print list multiples """

from functools import wraps

def double_return(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        return [result,result]
    return wrapper


@double_return
def add(x, y):
    return x + y
add(1, 2)  # [3, 3]

@double_return
def greet(name):
    return "Hi, I'm " + name

greet("colt")

##**************************************************************************************************************##

'''
@ensure_authorized
def show_secrets(*args, **kwargs):
    return "Shh! Don't tell anybody!"

show_secrets(role="admin") # "Shh! Don't tell anybody!"
show_secrets(role="nobody") # "Unauthorized"
show_secrets(a="b") # "Unauthorized"
'''

from functools import wraps

def ensure_authorized(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs.get("role") == "admin":
            return fn(*args, **kwargs)
        return "Unauthorized"
    return wrapper

##**************************************************************************************************************##

'''
@delay(3)
def say_hi():
    return "hi"

say_hi()
# should print the message "Waiting 3s before running say_hi" to the console
# should then wait 3 seconds
# finally, should invoke say_hi and return "hi"
'''

from functools import wraps
from time import sleep

def delay(tm):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print("Waiting {}s before running {}".format(tm,fn.__name__)
            sleep(tm)
            return fn(*args, **kwargs)
        return wrapper
    return inner
    

##**************************************************************************************************************##
## Enforcing the types using decorator nested for a given args 

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            #convert args into something mutable   
            newargs = []        
            for (a, t) in zip(args, types):
               newargs.append( t(a)) #feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator

@enforce(str, int)
def repeat_msg(msg, times):
	for time in range(times):
		print(msg)

@enforce(float, float)
def divide(a,b):
	print(a/b)
# repeat_msg("hello", '5')
divide('1', '4')

##**************************************************************************************************************##

## Web scrapping / crawling / BeautifulSoup
from bs4 import BeautifulSoup as BS
import requests
from time import sleep
from csv import DictWriter

def web_crawl(base_url):
    pg_url = "/page/1"
    all_quotes = []

    while pg_url:
        response = requests.get("{}{}".format(base_url,pg_url))
        print("Scrapping url : {}{}".format(base_url,pg_url))
        soup = BS(response.text, "html.parser")
        quotes = soup.find_all(class_="quote")
        for q in quotes:
            all_quotes.append({
                "text": q.find(class_="text").get_text(),
                "author": q.find(class_="author").get_text(),
                "bio-link": q.find("a")["href"]})

        next_btn = soup.find(class_="next")
        pg_url = next_btn.find("a")["href"] if next_btn else None
        sleep(2)
    return all_quotes

def write_quotes(quotes):
    with open("quotes.csv", "w") as csv_file:
        headers = ['text', 'author', 'bio-link']
        csv_writer = DictWriter(csv_file, fieldnames= headers)
        csv_writer.writeheader()
        for q in quotes:
            csv_writer.writerow(q)


if __name__ == '__main__':
    base_url = "http://quotes.toscrape.com"
    quotes = web_crawl(base_url)
    write_quotes(quotes)



##**************************************************************************************************************##
###regular expression
import re
def parse_name(input):
	name_regex = re.compile(r'^(Mr\.|Mrs\.|Ms\.|Mdme\.) (?P<first>[A-Za-z]+) (?P<last>[A-Za-z]+)$')
	matches = name_regex.search(input)
	print(matches.group())
	print(matches.group('first'))
	print(matches.group('last'))

parse_name("Mrs. Tilda Swinton")


##**************************************************************************************************************##
# pick 8 bit using re
import re
def parse_bytes(bt_str):
    pattern = re.compile(r'(\b[01]{8}\b)')
    p_result = pattern.findall(bt_str)
    return p_result
##**************************************************************************************************************##

import re

def parse_date(dt):
    pattern = re.compile(r'^(?P<day>\d{2})[\/\.,]{1}(?P<month>\d{2})[\/\.,]{1}(?P<year>\d{4})$')
    try:
        result = pattern.search(dt)
        date_dict = {}
        date_dict['d'] = result.group('day')
        date_dict['m'] = result.group('month')
        date_dict['y'] = result.group('year')
        if result:
            return date_dict
    except AttributeError:
        return None

print(parse_date("03,34,1223"))

##**************************************************************************************************************##

# RE sub

import re

def censor(frack):
    pattern = re.compile(r'\bfrack[a-z]*\b',re.I)
    rep = pattern.sub("CENSORED",frack)
    return rep


##**************************************************************************************************************##


##-------------------------------------
'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''

def remove_every_other(li):
    return [ li[x] for x in range(0,len(li)) if x % 2 ==0 ]

def remove_every_other(lst):
    return [val for i,val in enumerate(lst) if i % 2 == 0]   
##**************************************************************************************************************##

def vowel_count(s):
    s = s.lower()
    return { k : s.count(k) for k in s if k in 'aeiou' }

print(vowel_count('awesome'))

##**************************************************************************************************************##
'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(s):
    l_s = s.split(' ')
    new_l = [x[0].upper() + x[1:] for x in l_s]
    return " ".join(new_l)


##**************************************************************************************************************##

'''
find_factors(10) # [1,2,5,10 ]
find_factors(11) # [1,11]
find_factors(111) # [1,3,37,111 ]
find_factors(321421) # [1,293,1097,321421 ]
find_factors(412146) # [1,2,3,6,7,9,14,18,21,42,63,126,3271,6542,9813,19626,22897,29439,45794,58878,68691,137382,206073,412146]
'''

def find_factors(n):
    num_g = (d for d in range(1,n+1))
    return [fact_n for fact_n in num_g if n % fact_n == 0]

##**************************************************************************************************************##
'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(s,t_v):
    if t_v <3:
        return "Truncation must be at least 3 characters."
    elif t_v > len(s)+3:
        return s
    return s[ : t_v-3]+"..."

##**************************************************************************************************************##
'''
two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]) # {'a': 1, 'b': 2, 'c': 3, 'd': None}
two_list_dictionary(['a', 'b', 'c']  , [1, 2, 3, 4]) # {'a': 1, 'b': 2, 'c': 3}
two_list_dictionary(['x', 'y', 'z']  , [1,2]) # {'x': 1, 'y': 2, 'z': None}
'''

def two_list_dictionary(a_list, b_list):
    if len(a_list) > len(b_list):
        new_d = {a_list[i]:b_list[i] for i in range(0,len(b_list))}
        extra_d = {}.fromkeys(a_list[len(b_list):],None)
        new_d.update(extra_d)
        return new_d
    return {a_list[i]:b_list[i] for i in range(0,len(a_list))}

##**************************************************************************************************************##
'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(a,b):
    set_a = set(''.join(str(a).split()))
    set_b = set(''.join(str(b).split()))
    return not any(set_a.symmetric_difference(set_b))

##**************************************************************************************************************##

'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''

def find_the_duplicate(l):
    dup_d = {dup:l.count(dup) for dup in l}
    res = [key for key,val in dup_d.items() if val>1]
    if res:
        return res[0]
    return None

##**************************************************************************************************************##

'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]

sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]

sum_up_diagonals(list2) # 30
'''
def sum_up_diagonals(*args):
    li_cnt = len(*args)
    arg_li = args[0]
    #diag_1,diag_2 = 0,0
    diag_s = 0
    for i in range(0,li_cnt):
        diag_s += arg_li[i][i] + arg_li[i][li_cnt-1-i]
    return diag_s

##**************************************************************************************************************##
'''
find_greater_numbers([1,2,3]) # 3
find_greater_numbers([6,1,2,7]) # 4
find_greater_numbers([5,4,3,2,1]) # 0
find_greater_numbers([]) # 0
'''

def find_greater_numbers(li):
    if not li:
        return 0
    max_v = max(li)
    li_max_ind = li.index(max_v)
    if li_max_ind == 0:
        return li_max_ind
    return li_max_ind+1

def find_greater_numbers(arr):
    count = 0
    i = 0
    j = 1
    while i < len(arr):
        while j < len(arr):
            if arr[j] > arr[i]:
                count += 1
            j+=1
        j = i+1
        i+=1
    return count;

##**************************************************************************************************************##
# reverse vowels

def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)


##**************************************************************************************************************##
'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''

def three_odd_numbers(arr):
    i = 0
    while(i < (len(arr) -2)):
        total = 0
        j = i
        while(j <= i+2):
            total += arr[j]
            j+=1
            
        if (j-i) % 3 == 0 and total % 2 != 0:
            return True
            
        i+= 1
    return False

##**************************************************************************************************************##

'''
CLOSURE 

counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

def letter_counter(s):
    initial_str = s.lower()
    counter = 0
    def inner(l):
        counter = initial_str.count(l)
        return counter
    return inner

##**************************************************************************************************************##

'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

import csv
 
def update_users(old_first, old_last, new_first, new_last):
    with open("users.csv") as csvfile:
        csv_reader = csv.reader(csvfile)
        rows = list(csv_reader)
 
    count = 0
    with open("users.csv", "w") as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in rows:
            if row[0] == old_first and row[1] == old_last:
                csv_writer.writerow([new_first, new_last])
                count += 1
            else:
                csv_writer.writerow(row)
 
    return "Users updated: {}.".format(count)

    
##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

##**************************************************************************************************************##

