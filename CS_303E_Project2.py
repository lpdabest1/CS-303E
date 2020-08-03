def main():
    print("Ooh-de-la-lay! Ooh-de-la-lay! Fortune tellers!")
    print("Fortunes forecast! Lucky charms!")
    user_name = str(input("Hmmm… the future is cloudy. What is your name?"))

    user_fortunes = eval(input("Oo-dee-lally! How exciting! How many fortunes do you wish to get today?"))
    price_fortune = (1.99*user_fortunes)+ (.09*user_fortunes*1.99)
    print("Your total for today's session will be: " + str(price_fortune))
    user_lucky_list = []
    fortune_phrase_list = ["You will get an A", "You will learn to program", "You are destined to become a master coder", "May the force be with you", "Wow. You look like a programmer", "The code is strong with this one", "You will be testing your code often", "Taco cat spelled backwards is taco cat", "Your name will go down, down, down in history","You will master python"]
      
    for i in range(user_fortunes):
        user_lucky_integer_number = eval(input("I will tell your fortune. " + user_name + ", " + "enter your lucky integer number."))
        if user_lucky_integer_number < 0 or user_lucky_integer_number > 100:
            user_lucky_integer_number = eval(input("Oops " + user_name + ". " +"I cannot tell your fortune until you enter a valid number."))
        if user_lucky_integer_number >= 0 and user_lucky_integer_number <= 100:
            user_lucky_list.append(user_lucky_integer_number)
            print(user_name+ "! This is your lucky day!")            
            while (str(len(fortune_phrase_list)) < (str(user_lucky_integer_number))):
                fortune_phrase_corresponding = ((int((user_lucky_integer_number))%(int(len(fortune_phrase_list)))) - 1)
                print(fortune_phrase_list[fortune_phrase_corresponding])
                break
            while (str(len(fortune_phrase_list)) >= (str(user_lucky_integer_number))):
                fortune_phrase_corresponding = ((int((user_lucky_integer_number))%(int(len(fortune_phrase_list)))) - 1)
                print(fortune_phrase_list[fortune_phrase_corresponding])
                break

    print("You entered the following lucky numbers:")
    print(user_lucky_list)
                
   
main()

