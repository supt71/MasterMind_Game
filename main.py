'''
Sajid Kamal
CS21
Oct 9, 2021
'''


from random import choice
#to import choice for getting arbirary choices from the given list
def print_introduction():

    print("\n"*2 + "-"*65)
    print("Welcome to Mastermind!" + "\n\nYour goal is to guess a sequence of" +\
    " four colors." + "\nEach color can be blue, green, red, orange,"+\
    " purple, or yellow." +\
    "\nThen I'll tell you how many times you guessed the correct color" +\
    "\nin the correct position, and how many times you guessed the" +\
     "\ncorrect color, but in the wrong position." + "\nIt's up to you how "+\
     "many guesses you choose!" +\
    "\nGood Luck!")
    print( "-"*65)

    return ("")

def print_color(color_list):

    '''
    purpose: to print the color list in a nice way
    parameter: color_list -- the list of the six colors from the main function
    return: none
    '''
    str = " "
    str = str + color_list[0] + ", "
    str = str + color_list[1] + ", "
    str = str + color_list[2] + ", "
    str = str + color_list[3] + ", "
    str = str + color_list[4] + ", "
    str = str + color_list[5] + ", "
    str = str + color_list[6]
    print(str)

def get_guess(colors):

    '''
    purpose: to take input of four colors from the user.
    parameter: color -- the list of six colors from the main function.
    return: a list of four colors from the user.
    '''

    printing_line = "Please enter four legal colors. Your choices are:" +\
                                "\nred, orange, yellow, green, blue, purple"

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]

    print(printing_line)

    color_input1 = str(input("Enter color 1: "))

    while color_input1 not in colors:
        print(color_input1 + " is not a valid color.\n" + printing_line)
        print("")
        color_input1 = str(input("Enter color 1: "))

        continue

    color_input2 = str(input("Enter color 2: "))
    while color_input2 not in colors:
        print(color_input2 + " is not a valid color.\n" + printing_line)
        print("")
        color_input2 = str(input("Enter color 2: "))

        continue

    color_input3 = str(input("Enter color 3: "))
    while color_input3 not in colors:
        print(color_input3 + " is not a valid color." + printing_line)
        print("")
        color_input3 = str(input("Enter color 3: "))

        continue

    color_input4 = str(input("Enter color 4: "))
    while color_input4 not in colors:
        print(color_input4 + " is not a valid color." + printing_line)
        print("")
        color_input4 = str(input("Enter color 4: "))

        continue

    color_record = (str(color_input1) + ", " + str(color_input2) + ", " + \
                                str(color_input3) + ", "+ str(color_input4))
    color_record2 = [color_input1] + [color_input2] + [color_input3] + \
    [color_input4]
    print("")
    print("So you have guessed: ")
    print(color_record)

    return color_record2

def generate_code(colors):

    '''
    purpose: to get an arbitrary list of four color from the computer every time
    parameter: colors -- the list of six colors from the main function
    return: an arbitraty list of four colors -- as the secret code
    '''
    comp1 = choice(colors)
    comp2 = choice(colors)
    comp3 = choice(colors)
    comp4 = choice(colors)



    comp_ultimate = [comp1] + [comp2] + [comp3] + [comp4]
    color_record = (str(comp1) + ", " + str(comp2) + ", " + str(comp3) + ", " + str(comp4))
    print("Computer has guessed: ")
    print(color_record)
    return comp_ultimate

def exact_matches(secret_code, guess, status):
    '''
    purpose: matching the computer colors with the user colors to figure out how
            many exact choices are there.
    paramter: secret_code -- the arbitrary list of four colors from the computer
            guess -- the list of four colors given by the user.
            status -- showing the times when the user won (exact matched with the
            computer)
    return: an integer of how many times the user won.
    '''

    exact_count = 0
    i = 0
    for i in range(4):
        while guess[i] == secret_code[i]:
            status[i] = "exact"
            exact_count +=1

            break


    return exact_count

def inexact_matches(secret_code, guess, status):
    '''
    purpose: matching the computer colors with the user colors to figure out how
            many inexact choices are there.
    paramter: secret_code -- the arbitrary list of four colors from the computer
            guess -- the list of four colors given by the user.
            status -- showing the times when the user lost (the user input was
            in the list but did not match exactly)
    return: an integer of how many times the inexact match happened.
    '''
    inexact_count = 0
    i = 0
    for i in range(4):
        while ((status[i] != "exact") and (status[i] != "inexact")):
            if guess[i] in secret_code:
                status[i] = "inexact"
                inexact_count +=1
            break
    return inexact_count


def is_game_over(num_exact_matches, turn, how_many_round):
    if (((num_exact_matches) == 4) or ((turn) == (how_many_round))):
        return True

def player_won(num_exact_matches):
    if ((num_exact_matches) == 4):
        return True



def main():
    print(print_introduction())
    print("")
    how_many_round = int(input("How many rounds would you like to play? "))
    print("")


    round = how_many_round + 1

    for i in range(1, int(round)):
        turn = int(i)
        print("Round " + str(i))
        print("")
        status = ["", "", "", ""]
        color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
        user_choices = get_guess(color_list)
        #print(user_choices)

        comp_choices = generate_code(color_list)
        #print(comp_choices)
        exact= exact_matches(comp_choices, user_choices, status)
        print("There are %s exact count"%(exact))
        #print(status)
        inexact = inexact_matches(comp_choices, user_choices, status)
        print("There are %s inexact count"%(inexact))
        print("")
        game_over = is_game_over(exact, turn, how_many_round)
        if game_over == True:
            print("The game is over!!!")
        judement = player_won(exact)
        if judement == True:
            print("Hurrah! You won the game!")
            print("It took you " +  str(i) + " turns" +\
            " to get the answer")
            print("")
            break
        #print(status)
        i +=1


    print("Oh no! You lost :( Better luck next time! :)")
    print("")

main()

