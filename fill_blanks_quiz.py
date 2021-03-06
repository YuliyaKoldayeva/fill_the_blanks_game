import textwrap
'''
This program has the following logic:
1 - User choose the level of difficulty (number of guesses per problem)
2 - It will continue till one of game_over condition happens
3 - It has the number of levels = len(quiz_list). quiz_list is a nested list
4 - Inside of each level it restart the counting of the blank spaces and for each of them it creates current_blank_string = "__{0}__".format(str(current_blank_number))
5 - It asks for the user guess for each blank and compare with the correct answer
6 - If the answer is ok, it  replace the blank string and print it to user to see, than it goes to the next blank
7 - If the answer is wrong, it checks if the user has reached the maximum of the wrong answers

Extras:
* It asks for user name for more personalized game
* It controls the line length for better paragraph format when printing. 
'''

# This function asks for user's name for more personalized game.
# inputs: none
# outputs: user's name for further references for more personalized game
def user_name():
    name = raw_input("Hello! I would like to know your name. Could you please type it here: ")
    print "Thank you for your answer! Nice to meet you " + str(name)+"!"
    return name

# The function is asking the user to choose the difficulty level of the game and establishes the number of guesses accordingly.
# Variable game_level is used to store the user's level choice
# It will be running till user chooses one of the proposed options.  If his choice is not acceptable, the question will appear once again.
# inputs: variable name is used to personalise the interaction with the user. Any other input is necessary.
# outputs: variable maximum_failed will defines the maximum of wrong answers accepted before game over
def choose_the_level(name):
    while True:
        game_level = raw_input(str(name) + ', now you can choose the difficulty level. Type one of the following options: 1=easy; 2=medium; 3=hard: ')
        if game_level == "1" or game_level == "easy":
            maximum_failed = 5
            break
        else:
            if game_level == "2" or game_level == "medium":
                maximum_failed = 3
                break
            else:
                if game_level == "3" or game_level == "hard":
                    maximum_failed = 1
                    break
                else:
                    print "That's not an option! Please choose another one."
    print "Perfect! The chosen difficulty level is: "+ str(game_level)+". That means you have " + str(maximum_failed)+ " guesses per problem. Good luck!"
    return maximum_failed

# A list of test strings to pass in to the play_game function and their correct answers.
quiz_list = [["The capital of the USA is __1__. The capital of Russia is __2__. The capital of the UK is __3__. Canberra is the capital city of __4__. ", ["Washington", "Moscow", "London", "Australia"]],
                ["The __1__ System is the gravitationally bound system comprising the __2__ and the objects that orbit it. The __1__ System formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. The vast majority of the system's mass is in the __2__, with the majority of the remaining mass contained in __3__. The four smaller inner planets, Mercury, Venus, __4__ and __5__, are terrestrial planets, being primarily composed of rock and metal. __4__ (the third planet from the __2__) is the largest and densest of the inner planets, the only place where life is known to exist. The four outer planets are giant planets, being substantially more massive than the terrestrials. The two largest, __3__ and Saturn, are gas giants, being composed mainly of hydrogen and helium. The __1__ System also contains smaller objects. The asteroid belt, which lies between the orbits of __5__ and __3__.  Source: https://en.wikipedia.org/ ", ["Solar", "Sun", "Jupiter", "Earth", "Mars"]],
                ["__1__ is a country in the northern part of North America. Its ten provinces and three territories extend from the __2__ to the Pacific and northward into the Arctic Ocean, making it the world's second-largest country by total area. __1__'s southern __3__ with the United States is the world's longest bi-national land __3__. The majority of the country has a cold or severely cold winter climate, but southerly areas are warm in summer. __1__ is sparsely populated, the majority of its land territory being dominated by forest and tundra and the Rocky Mountains. It is highly urbanized with 82 per cent of the 35.15 million people concentrated in large and medium-sized cities, many near the southern __3__. Its capital is __4__, and its largest metropolitan areas are __5__, Montreal and Vancouver. Source: https://en.wikipedia.org/ ", ["Canada", "Atlantic", "border", "Ottawa", "Toronto"]]]

# This function is for paragraph format to be print. paragraph_border is to make more emphasis
# The number for symbols_in_line was chosen arbitrary, without any special meaning. So you can change it to fit better the avalable space
# inputs: test_string is the text to be formatted
# outputs: variable paragraph_separator is a graphical output to embellish the printing presentation, it will not be used further
def shorter_line_print(test_string):
    print "Here is your paragraph: "
    symbols_in_line = 80
    paragraph_separator = "*"*symbols_in_line
    print paragraph_separator
    print textwrap.fill(test_string,symbols_in_line)
    return paragraph_separator

# - This function checks if the maximum of the wrong answers was reached
# inputs:
#       guess_failed_number - keeps tracking of the wrong answers made by user
#       game_over - is the result of check for some special situation which should result in game over. It has True/False values
#       maximum_failed - is the maximum of the wrong answers accepted before game over. It was defined by user at the begining of the quiz
# outputs:
#       game_over has True/False values and it will be returned based on the value of the input variables
def check_maximum_failed (guess_failed_number,game_over,maximum_failed):
    if guess_failed_number > maximum_failed:
        game_over = True
        print "It was your last guess. You can not continue, but you can restart the quiz."
    return game_over

# - This function asks the user's guess for each blank and compares it with the correct answer
# - It replace the blank string and print it to user to see, than it goes to the next blank if the answer is ok
# inputs:
#       current_blank_string - is the blank to be filled in that is under the analysis
#       current_correct_answer - is the expected correct answer taken from initial data set
#       game_over - is the result of check for some special situation which should result in game over. It has True/False values
#       maximum_failed - is the maximum of the wrong answers accepted before game over. It was defined by user at the begining of the quiz
# outputs:
#       game_over will be returned True or False based on the value of the input variables
#       accepted_answer will be returned True (correct answer) or False(wrong answer) based on the value of the input variables
#                       and it will determinate if the program will move forward to the next blank to fill in
def ask_user_and_check(current_blank_string,current_correct_answer,game_over,maximum_failed):
    guess_failed_number = 0
    accepted_answer = False
    while accepted_answer == False:
        user_answer = raw_input("What is YOUR guess for this blank " + current_blank_string + " : ")
        if user_answer == current_correct_answer:
            accepted_answer = True
        else:
            guess_failed_number += 1
            game_over = check_maximum_failed(guess_failed_number,game_over,maximum_failed)
            if game_over == False:
                print  "It is not the correct answer. Please, check the spelling and use Capital Letters, if necessary. You have "+str(maximum_failed - guess_failed_number)+" guesses left. Try again! "
        if game_over == True:
            break
    return accepted_answer, game_over

# This function restarts the counting of the blank spaces for each new game level and
#   for each of them it creates "current" values. current_blank_string = "__{0}__".format(str(current_blank_number))
# inputs:
#       test_string - is the text of the current quiz(paragraph) proposed to the user that is under the analysis.
#       correct_answers_list - is the list of all expected correct answer for the current level taken from initial data set.
#       game_over - is the result of check for some special situation which should result in game over. It has True/False values
#       maximum_failed - is the maximum of the wrong answers accepted before game over. It was defined by user at the begining of the quiz
# outputs:
#       game_over will be returned True or False based on the value of the input variables
#       level_completed will be returned True (correct answer) or False(wrong answer) based on the value of the input variables
#                       and it will determinate if the program will move forward to the next level
def test_string_blanks_number(correct_answers_list,game_over,test_string,maximum_failed):
    current_blank_number = 1
    level_completed = False
    while current_blank_number <= len(correct_answers_list):
        current_blank_string = "__{0}__".format(str(current_blank_number))
        current_correct_answer = correct_answers_list[current_blank_number-1]
        accepted_answer, game_over = ask_user_and_check(current_blank_string,current_correct_answer,game_over,maximum_failed)
        if accepted_answer:
            print "Yes, it is a correct answer!",
            test_string = test_string.replace(current_blank_string, current_correct_answer,maximum_failed)
            print shorter_line_print(test_string)
            current_blank_number += 1
        if game_over:
            break
    if current_blank_number > len(correct_answers_list):
        print "This quiz has ", len(correct_answers_list)," blanks. You have filled all of them!!!"
        level_completed = True
    return game_over,level_completed

# The main goal of this function is to detect the number of levels in the game and to extract
# quiz question (to be stored in the variable test_string) and a list of the correct answers (variable correct_answers_list) for each level
# It has the number of levels = len(quiz_list). quiz_list is a nested list
# inputs:
#       quiz_list - is the nested list of all quiz questions and their respective correct answers for ALL levels (initial data set).
#       game_over - is the result of check for some special situations which should result in game over. It has True/False values
#       maximum_failed - is the maximum of the wrong answers accepted before game over. It was defined by user at the begining of the quiz
# outputs:
#       game_over will be returned True or False based on the value of the input variables
#       level_completed will be returned True (correct answer) or False(wrong answer) based on the value of the input variables
#                       and it will determinate if the program will move forward to the next level
def current_quiz_set(quiz_list,game_over,maximum_failed):
    current_level = 0
    while current_level < len(quiz_list):
        print "Current Quiz Level = ", current_level+1
        current_quiz = quiz_list[current_level]
        test_string = current_quiz[0]
        print shorter_line_print(test_string)
        correct_answers_list = current_quiz[1]
        game_over, level_completed = test_string_blanks_number(correct_answers_list,game_over,test_string,maximum_failed)
        if game_over:
            break
        if level_completed:
            current_level += 1
    game_over = True
    return game_over

# This function is to start and to finish the game. It also asks for user's name for more personalised interaction.
# - User chooses the level of difficulty (number of guesses per problem) and the value is stored in maximum_failed
# - It will continue till one of the game_over conditions happen
# inputs:
#       quiz_list - is the nested list of all quiz questions and their respective correct answers for ALL levels (initial data set).
# outputs:
#       final message issued when the game over confirmation is received
def play_game(quiz_list):
    name = user_name()
    maximum_failed = choose_the_level(name)
    game_over = False
    while game_over == False:
        game_over = current_quiz_set(quiz_list,game_over,maximum_failed)
    return "Game over! Thank you for playing, "+ str(name)+" !"
    
print play_game(quiz_list)
