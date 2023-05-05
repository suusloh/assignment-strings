# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from os import WCOREDUMP


player1 = 'Ruud Gullit'
player2 = 'Marco van Basten' 

goal_0 = 32
goal_1 = 54

scorers = player1 + " " + str(goal_0) + "," + " " + player2 + " " + str(goal_1)

#print (scorers)

report = f"{player1} scored in the {goal_0}nd minute" +"\n" f"{player2} scored in the {goal_1}th minute"
print (report)

player = 'Ronald Koeman'

first_name = 'Ronald'
first_name_start = first_name.find('R')
first_name_end = first_name.find('d')

print(first_name)

last_name = 'Koeman'
last_name_start = last_name.find('K')
last_name_end = last_name.find('n') + 1
last_name_len = len(last_name[last_name_start:last_name_end])

print(last_name_len)

name_short = f"{first_name[0]}. {last_name}"

print(name_short)

chant = 'Ronald! '  *5 +  'Ronald!'

print(chant)

good_chant = True
bad_chant = False
print(good_chant != bad_chant)





















