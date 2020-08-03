import random
things_that_have_happened = {"a"} #set
things_that_have_happened.remove("a")
food_list = ["protein bar", "trail mix"] #list
satchel_list = [food_list, "empty water bottle"] #list within a list
equipment = ["bandages", "scalpel", "morphine", "stitches"]
password = (7, 5, 2, 9) #tuple
password_possibilities = {"5729":1, "5792":2, "5279":3, "5297":4, "5927":5, "5972":6} #dictionary

class Satchel:
    """This class is for storing anything the character picks up during their journey,
            the satchel will have a maximum content of 10 items."""
    def __init__(self, item):
        self.item = item

    def gather_item(self):
        a = 0
        while a < 1:
            if (len(satchel_list) + len(food_list)-1) in range(0, 6):
                satchel_list.append(self.item)
                a += 1
            else:
                print("Sorry, but you cannot pick up this item, your satchel is full.")
                drop_item = input("Your satchel contains " + str(satchel_list) + ". Would you like to drop one of your items?" ).lower()
                b = 0
                while b < 1:
                    if drop_item == "yes":
                        choose_item_to_drop = input("Which item would you like to drop? ").lower()
                        c = 0
                        while c < 1:
                            if choose_item_to_drop in satchel_list:
                                Satchel(choose_item_to_drop).consume_item()
                                c = 1
                            elif choose_item_to_drop in food_list:
                                Satchel(choose_item_to_drop).consume_food()
                                c = 1
                            else:
                                choose_item_to_drop = input("That item is not in your list, try a different item: ").lower()
                        b += 1
                    elif drop_item == "no":
                        print("Then you cannot pick up this item.")
                        b += 1
                    else:
                        drop_item = input("Just enter yes or no: ").lower()
                a += 1

    def gather_food(self):
        a = 0
        while a < 1:
            if (len(satchel_list) + len(food_list)-1) in range(0, 6):
                food_list.append(self.item)
                a += 1
            else:
                print("Sorry, but you cannot pick up this item, your satchel is full.")
                drop_item = input("Your satchel contains " + str(satchel_list) + ". Would you like to drop one of your items?" ).lower()
                b = 0
                while b < 1:
                    if drop_item == "yes":
                        choose_item_to_drop = input("Which item would you like to drop? ").lower()
                        Satchel(choose_item_to_drop).consume_food()
                        b += 1
                    elif drop_item == "no":
                        print("Then you cannot pick up this item.")
                        b += 1
                    else:
                        drop_item = input("Just enter yes or no: ").lower()
                a += 1

    def consume_item(self):
        a = 0
        while a < 1:
            if self.item in satchel_list:
                satchel_list.remove(self.item)
                print("You have dropped the " + str(self.item) + ".")
                a += 1
            elif self.item == "cancel":
                a += 1
            elif self.item == "check satchel":
                check_satchel()
                self.item = input("Type an item to remove it or cancel to return to what you were doing. ").lower()
            else:
                self.item = input("Sorry, but you do not have this item in your satchel. Type check satchel to see what you have. "
                                  "\nTry again or type cancel to return to what you were doing. ").lower()

    def consume_food(self):
        a = 0
        while a < 1:
            if self.item in food_list:
                food_list.remove(self.item)
                print("You have consumed the " + str(self.item) + ".")
                things_that_have_happened.add("full")
                a += 1
            elif self.item == "cancel":
                a += 1
            elif self.item == "check satchel":
                check_satchel()
                self.item = input("Type an item to remove it or cancel to return to what you were doing. ").lower()
            else:
                self.item = input("Sorry, but you do not have this item in your satchel. Try again or type cancel to return to what you were doing. ").lower()

def check_satchel():
    if len(satchel_list) == 0:
        print("Your satchel is empty.")
    elif len(satchel_list) == 1:
        print("Your satchel contains this item: " + str(satchel_list))
    else:
        print("Your satchel contains these items: " + str(satchel_list))

#This is how we walk through the game and the various choices that the player will make.
def intro():
    introduction = input("You wake up on a cold metal floor and from what you can tell, you are unharmed, aside from "
        "\nyour mildly concussed head. Your sense of identity is foggy and you can't recall exactly what's going on. "
        "\nYou're supposed to be on a mission to pluto, what went wrong? The spaceship is mostly dark, but you can "
        "\nsee some light filtering in from a space that you know leads outside. Welp, looks like the atmosphere "
        "\nis at least partially breathable, because otherwise you wouldn't have woken up at all. You notice you have "
        "\na satchel slung over your shoulder, if at any point you want to check it's contents, type 'check satchel'."
        "\nDo you explore the ship or venture outside? Enter explore or venture: ").lower()
    cont = 0
    while cont < 1:
        if introduction == "explore":
            explore_spaceship()
            cont = 1
        elif introduction == "venture":
            venture_outside()
            cont = 1
        elif introduction == "check satchel":
            check_satchel()
            introduction = input("Now please type explore or venture to continue: ").lower()
        else:
            introduction = input("This is not an option, try again, enter explore or venture: ").lower()

def explore_spaceship():
    if "injured" in things_that_have_happened:
        spaceship_start = input(
            "You have returned to the vessel a little worse for wear. You recognize a potentially useful object nearby, "
            "\npick up the flashlight? Enter yes or no: ").lower()
    else:
        spaceship_start = input("You have decided to explore the vessel. You recognize a potentially useful object nearby, "
        "\npick up the flashlight? Enter yes or no: ").lower()
    cont = 0
    while cont < 1:
        if spaceship_start == "yes":
            Satchel("flashlight").gather_item()
            print("You have picked up the flashlight.")
            explore_spaceship_with_flashlight()
            cont += 1
        elif spaceship_start == "no":
            print("For some reason you have chosen not to pick up the flashlight, whatever man, you do you.")
            explore_spaceship_without_flashlight()
            cont = 1
        elif spaceship_start == "check satchel":
            check_satchel()
            spaceship_start = input("Now please type yes or no to continue: ").lower()
        else:
            spaceship_start = input("This is not a valid response to the question, a simple yes or no will suffice: ").lower()

def explore_spaceship_without_flashlight():
    print("You try to feel your way forward because you didn't pick up the super convenient "
        "\nflashlight that was just freaking lying there for you but whatever. You trip over a "
        "\nhard object on the ground and slam head first into a wall.")
    if "injured" in things_that_have_happened:
        print("You bleed out on the floor. You are dead.")
    else:
        explore_without_flashlight = input("Do you pick up the flashlight now? ").lower()
        cont = 0
        while cont < 1:
            if explore_without_flashlight == "yes":
                Satchel("flashlight").gather_item()
                print("You have picked up the flashlight.")
                things_that_have_happened.add("injured")
                explore_spaceship_with_flashlight()
                cont = 1
            elif explore_without_flashlight == "no":
                print("You flounder in the dark until you trip over the same object again and crack your skull open, congratulations,"
                      "\nyou are dead.")
                cont = 1
            elif explore_without_flashlight == "check satchel":
                check_satchel()
                explore_without_flashlight = input("Now please type yes or no to continue: ").lower()
            else:
                explore_without_flashlight = input("This is not a valid response to the question, a simple yes or no will suffice: ").lower()

def explore_spaceship_with_flashlight():
    explore_with_flashlight_part_1 = input("You turn the flashlight on, turn away from the exit, and glance around, you seem to be in a somewhat "
                                           "\ncircular hallway with paths to the left and right, which do you follow? ").lower()
    cont = 0
    while cont < 1:
        if explore_with_flashlight_part_1 == "left":
            print("You have chosen to go left.")
            explore_with_flashlight_left()
            cont = 1
        elif explore_with_flashlight_part_1 == "right":
            print("You have chosen to go right.")
            explore_with_flashlight_right()
            cont = 1
        elif explore_with_flashlight_part_1 == "check satchel":
            check_satchel()
            explore_with_flashlight_part_1 = input("Now please type left or right to continue: ").lower()
        else:
            explore_with_flashlight_part_1 = input("Enter left or right: ").lower()

def explore_with_flashlight_right():
    right = input("You walk down the hallway, shining the flashlight ahead of you and notice that the end of the "
                  "\nhallway has been blocked off by wreckage from the ship. There is, however, an opening to the "
                  "\nright, explore or go back down the hallway to search the other path? Enter right or other: ").lower()
    a = 0
    while a < 1:
        if right == "right":
            explore_cockpit()
            a = 1
        elif right == "other":
            explore_with_flashlight_left()
            a = 1
        elif right == "check satchel":
            check_satchel()
            right = input("Now please type right or other to continue: ").lower()
        else:
            right = input("This is not a valid response. Please type right or other: ").lower()

def explore_cockpit():
    cockpit = input("You enter the cockpit of the ship, memories of your time with the other crew members in here start "
                    "\nto become less blurry in your head. You walk over to the control system and open the ships logs. "
                    "\nType read to see if you can find out what happened or ignore to move on: ").lower()
    a = 0
    while a < 1:
        if cockpit == "read":
            captains_entries()
            a = 1
        elif cockpit == "ignore":
            print("You are ignoring the ships logs.")
            send_transmission()
            a = 1
        elif cockpit == "check satchel":
            check_satchel()
            cockpit = input("Now please type read or ignore to continue: ").lower()
        else:
            cockpit = input("This is not a valid response. Please type read or ignore: ").lower()

def captains_entries():
    try:
        ship_log = open("captains_log.py", "r")
        print(ship_log.read())
        ship_log.close()
        new_entry = open("captains_log_last_entry.txt", "w")
        write_a_log = input(
            "Hmm, this entry doesn't tell you anything about how you ended up on this strange planet, but perhaps "
            "\nyou can add an entry in case someone might read it later to find out what happened to you or maybe "
            "\neven send help. Add an entry? ").lower()
        a = 0
        while a < 1:
            if write_a_log == "yes":
                write = input("Write an entry: ")
                new_entry.write(write)
                new_entry.close()
                send_transmission()
                a = 1
            elif write_a_log == "no":
                send_transmission()
                a = 1
            elif write_a_log == "check satchel":
                check_satchel()
                write_a_log = input("Now please type yes or no to continue: ").lower()
            else:
                write_a_log = input("This is not a valid response. Please type yes or no: ").lower()
    except FileNotFoundError:
        print("The computer is malfunctioning, this action cannot be performed.")
        send_transmission()

def send_transmission():
    print("You notice an option on the computer for sending an emergency transmission, it requires a password.")
    if "password" in things_that_have_happened:
        send = input("Would you like to check the numbers you wrote down or enter a password: ").lower()
        a = 0
        while a < 1:
            if send == "check":
                print(str(password) + " Looking at the list, you recall that the 5 is the first number in the password.")
                write_out = input("Write out all possible variations of the password? ").lower()
                b = 0
                while b < 1:
                    if write_out == "yes":
                        for x in password_possibilities:
                            print(x)
                        b = 1
                    elif write_out == "no":
                        print("You do not make a handy list.")
                        b = 1
                    else:
                        write_out = input("This is not a valid response, type yes or no to continue: ").lower()
                enter_password()
                a = 1
            elif send == "enter":
                enter_password()
                a = 1
            elif send == "check satchel":
                check_satchel()
                send = input("Now please type check or enter to continue: ").lower()
            else:
                send = input("This is not a valid response, type check or enter to continue: ").lower()
    else:
        send = input("You recall a security procedure that will allow you to send an emergency transmission, but you can't "
                 "\nremember the password. Try entering a password anyway or return to take the path to the left? ").lower()
        a = 0
        while a < 1:
            if send == "try":
                enter_password()
                a = 1
            elif send == "return":
                print("You exit the cockpit and pass the place where you woke up.")
                explore_with_flashlight_left()
                a = 1
            elif send == "check satchel":
                check_satchel()
                send = input("Now please type try or return to continue: ").lower()
            else:
                send = input("This is not a valid response, type try or return to continue: ").lower()

def enter_password():
    enter = input("Enter password: ").lower()
    number = "5927"
    attempts = 0
    a = 0
    while a < 1:
        if attempts < 4:
            if len(enter) == 4:
                if enter == number:
                    print("This is the correct password! Your transmission signal is sent successfully, you and your ship are teleported home "
                          "\nbecause your people invented teleportation during your travel, how convenient.")
                    a = 1
                elif enter != number:
                    attempts += 1
                    enter = input("Incorrect password, try again: ")
            elif enter == "cancel":
                print("You exit the cockpit and pass the place where you woke up.")
                explore_with_flashlight_left()
                a = 1
            else:
                enter = input("Invalid, enter a four digit number or type cancel to leave the cockpit and return to the hallway: ").lower()
        else:
            print("The computer locks you out after getting the password wrong so many times. It believes you are a threat to the system and"
                  "\nblows up the ship. You are dead.")
            a = 1

def explore_with_flashlight_left():
    explore_with_flashlight_part_2_left = input("You walk down the hallway until you see an opening on the left, shining the flashlight inside "
                                                "\nyou see several unused escape pods in what appears to be an engineering bay. Would you like "
                                                "\nto go in and look around? ").lower()
    a = 0
    while a < 1:
        if explore_with_flashlight_part_2_left == "yes":
            explore_the_engineering_bay()
            a = 1
        elif explore_with_flashlight_part_2_left == "no":
            go_forward()
            a = 1
        elif explore_with_flashlight_part_2_left == "check satchel":
            check_satchel()
            explore_with_flashlight_part_2_left = input("Now please type yes or no to continue: ").lower()
        else:
            explore_with_flashlight_part_2_left = input("This is not a valid response. Please type yes or no: ")

def explore_the_engineering_bay():
    explore_engineering_bay = input(
        "You walk in and let your eyes take in the details, some vague memories of times spent in here flicker through "
        "\nyour head and you recall several crew-mates that you know should be here with you. You want to find them. "
        "\nYou notice that the engine has been damaged from the crash and is leaking fuel. Attempt to repair the engine? ").lower()
    a = 0
    while a < 1:
        if explore_engineering_bay == "yes":
            repair_engine()
            a = 1
        elif explore_engineering_bay == "no":
            leave_engine_room()
            a = 1
        elif explore_engineering_bay == "check satchel":
            check_satchel()
            explore_engineering_bay = input("Now please type left or right to continue: ").lower()
        else:
            explore_engineering_bay = input("This is not a valid response, type yes or no to continue: ").lower()

def repair_engine():
    x = random.randint(1, 25)
    if x == 1:
        print("You messed up the wiring cause you don't have any experience trying to fix engines, "
              "\nwhat made you think you were an engineer? You blew up the ship, you are dead.")
    elif x in range(2, 9):
        print("You have failed to repair the engine, you could not figure out how to do it.")
        leave_engine_room()
    else:
        print("You have repaired the engine!")
        things_that_have_happened.add("engine repaired")
        leave_engine_room()

def leave_engine_room():
    if "engine repaired" in things_that_have_happened:
        leave_room = input("Would you like to leave this room?")
    else:
        leave_room = input("Would you like to leave this room while the engine is still broken? ").lower()
    a = 0
    while a < 1:
        if leave_room == "yes":
            go_forward()
            a = 1
        elif leave_room == "no":
            stay_in_engine_room()
            a = 1
        elif leave_room == "check satchel":
            check_satchel()
            leave_room = input("Now please type yes or no to continue: ").lower()
        else:
            leave_room = input("This is not a valid response, type yes or no to continue: ").lower()

def stay_in_engine_room():
    if "engine repaired" in things_that_have_happened:
        stay = input(
            "You have chosen to stay in the engine room, you look around again and see nothing new,"
            "\nthe engine is still repaired. Would you like to leave this room? ").lower()
        a = 0
        while a < 1:
            if stay == "yes":
                print("You exit the room and turn left.")
                go_forward()
                a = 1
            elif stay == "no":
                return stay_in_engine_room()
            elif stay == "check satchel":
                check_satchel()
                stay = input("Now please type yes or no to continue: ").lower()
            else:
                stay = input("This is not a valid response, type yes or no to continue: ").lower()
    else:
        stay = input(
            "You have chosen to stay in the engine room, would you like to try to fix the broken engine? ").lower()
        b = 0
        while b < 1:
            if stay == "yes":
                print("You attempt to fix the engine.")
                repair_engine()
                b = 1
            elif stay == "no":
                print("You do not try to fix the engine.")
                leave_engine_room()
                b = 1
            elif stay == "check satchel":
                check_satchel()
                stay = input("Now please type yes or no to continue: ").lower()
            else:
                stay = input("This is not a valid response, type yes or no to continue: ").lower()

def go_forward(circuit_room_explored = False):
    move_forward = input("You move forward through the hallway. You come across two doors, one on the left and one on the right, "
                         "\nthe hallway continues in front of you. Do you go left, right, or forward? ").lower()
    a = 0
    while a < 1:
        if move_forward == "left":
            explore_crew_quarters()
            a = 1
        elif move_forward == "right":
            if not circuit_room_explored:
                move_forward = input("You glance into the room on the right and see a lot of circuit boards, there isn't anything to do in here, "
                                     "\ngo through the other door or keep moving forward? Enter left or forward: ").lower()
                circuit_room_explored = True
            if move_forward == "right":
                move_forward = input("This room has been explored. Enter left or forward: ").lower()
        elif move_forward == "forward":
            print("You try to move forward through the hallway and see that it is blocked off, realising that it is inevitable, your feet pull you into the "
                "\nroom on the right.")
            return explore_crew_quarters()
        elif move_forward == "check satchel":
            check_satchel()
            move_forward = input("Now please type left, right, or forward to continue: ").lower()
        else:
            if circuit_room_explored:
                move_forward = input("Not a valid response. Enter left or forward: ").lower()
            else:
                move_forward = input("Not a valid response, type left, right, or forward to continue: ").lower()

def explore_crew_quarters():
    crew_quarters = input("You enter a disheveled room full of beds and hear a soft groan coming from the back corner. Investigate or leave? ").lower()
    a = 0
    while a < 1:
        if crew_quarters == "investigate":
            meet_crew_mate()
            a = 1
        elif crew_quarters == "leave":
            print("You cannot leave, your feet will not let you.")
            meet_crew_mate()
            a = 1
        elif crew_quarters == "check satchel":
            check_satchel()
            crew_quarters = input("Now please type investigate or leave to continue: ").lower()
        else:
            crew_quarters = input("This is not a valid response, type investigate or leave to continue: ").lower()

def meet_crew_mate():
    meet = input('You walk over to the back corner and see a man laying in one of the beds, his hand clutching a large chunk of metal projecting '
                 '\nout of his lower abdomen, covered in thick blood, you notice now that a significant amount of the red liquid is spread throughout '
                 '\nthe room. You remember him, but not his name, you approach. The man looks up at you, "Captain! I cannot tell you how good it is to '
                 '\nsee-", a fit of coughing interrupts his greeting. You notice that when his hand draws away from his mouth, it is covered in blood. '
                 '\nHe notices the look in your eye, "It isn' + "'" + 't as bad as it looks, I am going to need your help though, can you go to the med bay '
                                                                      '\nand grab me the supplies I need to patch this up?" Enter yes or no: ').lower()
    a = 0
    while a < 1:
        if meet == "yes":
            print("You enter the med bay that you instinctively know is next door while wondering to yourself if it's too late to ask "
                    "\nfor this guys' name, you're clearly supposed to know him so it would be uncomfortable to bring up your memory loss "
                    "\nat the moment. ")
            help_crew_mate()
            a = 1
        elif meet == "no":
            print('A shadow falls over the face of your crew mate, "So that' + "'" + 's how it' + "'" + 's gonna be huh? You shoot someone ONE TIME and they '
                '\nthink they can ditch you when you have shrapnel sticking out of your chest. So be it.". He pulls a big red button out of his '
                '\npocket and slams his hand into it. Your ship blows up, you both die, your last thought is that maybe you should not have just '
                '\ntried to leave your medical officer to die.')
            a = 1
        elif meet == "check satchel":
            check_satchel()
            meet = input("Now please type yes or no to continue: ").lower()
        else:
            meet = input("This is not a valid response, type yes or no to continue: ").lower()

def help_crew_mate():
    med_bay = input("You enter the med bay and glance around, there are a lot of things in here that could be useful. You search the drawers and "
                    "\nfind " + str(equipment) + ", what would you like to take? Enter (nothing) if you've changed your mind: ").lower()
    a = 0
    while a < 1:
        if med_bay in equipment:
            if med_bay == "bandages":
                Satchel("bandages").gather_item()
                if "bandages" in satchel_list:
                    equipment.remove("bandages")
                med_bay = input("What else would you like to pick up? ").lower()
            elif med_bay == "scalpel":
                Satchel("scalpel").gather_item()
                if "scalpel" in satchel_list:
                    equipment.remove("scalpel")
                med_bay = input("What else would you like to pick up? ").lower()
            elif med_bay == "morphine":
                Satchel("morphine").gather_item()
                if "morphine" in satchel_list:
                    equipment.remove("morphine")
                med_bay = input("What else would you like to pick up? ").lower()
            elif med_bay == "stitches":
                Satchel("stitches").gather_item()
                if "stitches" in satchel_list:
                    equipment.remove("stitches")
                med_bay = input("What else would you like to pick up? ").lower()
        elif len(equipment) == 0:
            print("You have taken all of the supplies.")
            leave = input("Would you like to return to your crew mate? Enter yes or no: ").lower()
            leave_med_bay(leave)
            a= 1
        elif med_bay == "nothing":
            leave = input("Would you like to return to your crew mate? Enter yes or no: ").lower()
            leave_med_bay(leave)
            a = 1
        elif med_bay == "check satchel":
            check_satchel()
            med_bay = input("Now please type an item or (nothing) to continue: ").lower()
        else:
            med_bay = input("This is not a valid response, type an item or (nothing) to continue: ").lower()

def leave_med_bay(leave):
    a = 0
    while a < 1:
        if leave == "yes":
            hunger()
            a = 1
        elif leave == "no":
            leave = input("Oh my gosh, your crew mate is dying, just go help him! Enter yes: ").lower()
            if leave == "no":
                leave = input("You absolute punk. Try that again and I will smite you. Enter yes: ").lower()
                if leave == "no":
                    x = random.randint(1, 3)
                    if x == 1:
                        print("Heh, I like you, you win. Your ship feels the obstinacy radiating off of you, it powers up and flies you home.")
                    else:
                        print("Have it your way, you are dead.")
                        break
                else:
                    return leave_med_bay(leave)
            else:
                return leave_med_bay(leave)
        elif leave == "check satchel":
            check_satchel()
            leave = input("Now please type yes or no to continue: ").lower()
        else:
            leave = input("This is not a valid response, type yes or no to continue: ").lower()

def hunger():
    if "flashlight" not in satchel_list:
        print("You dropped your flashlight. Foolish move. You trip and die trying to make your way back.")
    else:
        if "full" in things_that_have_happened:
            return_to_crew_mate()
        else:
            eat = input("On your way back, you notice for the first time since waking up that you are desperately hungry. "
                        "\nEat something from your satchel? ").lower()
            if len(food_list) == 0:
                print("You have no food, you are dead.")
            else:
                a = 0
                while a < 1:
                    if eat == "yes":
                        consume = input("What would you like to eat? ").lower()
                        b = 0
                        while b < 1:
                            if consume in food_list:
                                Satchel(consume).consume_food()
                                return_to_crew_mate()
                                b = 1
                            elif consume in satchel_list:
                                print("That is not food, you cannot eat that, you choke on it and die.")
                                b = 1
                            elif consume == "check satchel":
                                check_satchel()
                                consume = input("Now please type a food that you have to continue: ").lower()
                            else:
                                consume = input("This is not in your satchel, type a food that you have to continue: ").lower()
                        a = 1
                    elif eat == "no":
                        print("You pass out and die from your sudden hunger.")
                        a = 1
                    elif eat == "check satchel":
                        check_satchel()
                        eat = input("Now please type yes or no to continue: ").lower()
                    else:
                        eat = input("This is not a valid response, type yes or no to continue: ").lower()

def return_to_crew_mate():
    heal = input("You return to your friend and see that his condition has changed little during your time away. Offer the supplies? ").lower()
    a = 0
    while a < 1:
        if heal == "yes":
            print("You offer him the supplies.")
            offer_supplies()
            a = 1
        elif heal == "no":
            print("He looks at you in confusion because you're just standing there. " + '"Uhh... can I have those supplies now?" ' +
                  "\nYou hand over the supplies because the situation has become uncomfortable and you don't want to deal with that.")
            offer_supplies()
            a = 1
        elif heal == "check satchel":
            check_satchel()
            heal = input("Now please type yes or no to continue: ").lower()
        else:
            heal = input("This is not a valid response, type yes or no to continue: ").lower()

def offer_supplies():
    if "bandages" and "stitches" in satchel_list:
        Satchel("bandages").consume_item()
        Satchel("stitches").consume_item()
        cockpit = input('You shine the flashlight on his chest while he pulls the chunk of metal out of his abdomen, you help him stitch '
              '\nup his injury and wrap the bandages around him. "Thank you.", he says shakily, "Have you found anyone else?" You '
              '\nshake your head. He sighs. "I doubt the others made it, I saw Ethan jump in an escape pod on our way down, not too '
              '\nsurprising really. Our priority right now should be sending a distress signal back to the base. You decide it is '
              '\ntime to explain to him that you cannot quite remember how to do that. "I was wondering why you were being so quiet." '
              '\nHe pauses for a few moments. "Alright, I can' + "'" + 't take you there but I know the password is the numbers 7, 5, 2, and 9. '
                '\nI don' + "'" + 't know what order those are in though." He writes this down on a scrap of paper and you shove it in your pocket. '
                '\nHe then explains to you how to get to the cockpit where the computer is and wishes you luck. Go to cockpit? ').lower()
        things_that_have_happened.add("password")
        a = 0
        while a < 1:
            if cockpit == "yes":
                if "engine repaired" not in things_that_have_happened:
                    print(
                        "You failed to repair the engine in time, the fuel leak causes the ship to blow up. You are dead.")
                else:
                    explore_cockpit()
                a = 1
            elif cockpit == "no":
                explore()
                a = 1
            elif cockpit == "check satchel":
                check_satchel()
                cockpit = input("Now please type yes or no to continue: ").lower()
            else:
                cockpit = input("This is not a valid response, type yes or no to continue: ").lower()
    else:
        print('"These are not the materials I need." You go back to the med bay.')
        help_crew_mate()

def explore():
    go = input('Well where the heck do you want to go then? Your options are "cockpit", "med bay", "engine room", "outside": ').lower()
    a = 0
    while a < 1:
        if go == "cockpit":
            if "engine repaired" not in things_that_have_happened:
                print(
                    "You failed to repair the engine in time, the fuel leak causes the ship to blow up. You are dead.")
            else:
                explore_cockpit()
            a = 1
        elif go == "med bay":
            help_crew_mate()
            a = 1
        elif go == "engine room":
            explore_the_engineering_bay()
            a = 1
        elif go == "outside":
            venture_outside()
            a = 1
        elif go == "check satchel":
            check_satchel()
            go = input("Now please type a place to continue: ").lower()
        else:
            go = input("This is not a valid response, type a place to continue: ").lower()

def venture_outside():
    outside_start = input("You step outside and feel quickly overwhelmed by the moonlight, you glance up and notice that the moon here is either much larger "
        "\nor much closer than the moon on earth, bathing the world in a soft light. As you turn your attention back to the ground, you take in the foreign "
        "\nelements: the brick red dirt is interrupted in many places by large patches of blue moss and some round white structures that looked similar to "
        "\nmushroom caps the size of an elephant. A large gash through the planet shows you the path your ship took when colliding with the surface. Would "
        "\nyou like to (follow) the gash to see if you can learn anything about your crash or (explore) the forest and inspect plant and animal life? ").lower()
    a = 0
    while a < 1:
        if outside_start == "follow":
            print("An alien jumps out from behind a mushroom and shoots you. "
                  "\nYou are dead.")
            a = 1
        elif outside_start == "explore":
            print("A strange four legged creature sprints at you from behind the ship and gores you with his horns.")
            if "injured" in things_that_have_happened:
                print("You are dead.")
            else:
                things_that_have_happened.add("injured")
                attacked()
            a = 1
        elif outside_start == "check satchel":
            check_satchel()
            outside_start = input("Now please type follow or explore to continue: ").lower()
        else:
            outside_start = input("This is not a valid response, type follow or explore to continue: ").lower()

def attacked():
    retreat = input("You have been gored, retreat into the ship? ").lower()
    a = 0
    while a < 1:
        if retreat == "yes":
            print("You return to the ship, holding your open wound.")
            explore_spaceship()
            a = 1
        elif retreat == "no":
            print("You bleed out and die.")
            a = 1
        elif retreat == "check satchel":
            check_satchel()
            retreat = input("Now please type yes or no to continue: ").lower()
        else:
            retreat = input("This is not a valid response, type yes or no to continue: ").lower()

intro()
z = 0
while z < 1:
    play_again = input("Would you like to try again? ").lower()
    if play_again == "yes":
        things_that_have_happened = {"a"}
        things_that_have_happened.remove("a")
        food_list = ["protein bar", "trail mix"]
        satchel_list = [food_list, "empty water bottle"]
        equipment = ["bandages", "scalpel", "morphine", "stitches"]
        password = (7, 5, 2, 9)
        password_possibilities = {"5729": 1, "5792": 2, "5279": 3, "5297": 4, "5927": 5, "5972": 6}
        intro()
    elif play_again == "no":
        z = 1
    else:
        play_again = input("Enter yes or no: ")