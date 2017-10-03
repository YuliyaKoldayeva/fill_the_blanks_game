
# Ask for user name to make the game more personalized
def user_name():
    name = raw_input("Hello! I would like to ask you your name. Could you please type the answer here: ")
    print "Thank you for the answer! Nice to meet you " + str(name)+"!"
    return name


# Here the program is asking the user to choose the difficulty level of the game and establish the number of guesses accordingly.
def choose_the_level(name):
    while True:
        print str(name)+ ", now you can choose the difficulty level."
        game_level = raw_input("type one of the following options: 1=easy; 2=medium; 3=hard: ")
        if game_level == "1" or game_level == "easy":
            print "Easy level means you have 5 guesses per problem. Good luck!"
            attempts_number = 5
            break
        else:
            if game_level == "2" or game_level == "medium":
                print "Medium level means you have 3 guesses per problem. Good luck!"
                attempts_number = 3
                break
            else:
                if game_level == "3" or game_level == "hard":
                    print "Hard level means you have only 1 guess per problem. Good luck!"
                    attempts_number = 1
                    break
                else:
                    print "That's not an option! Please choose another one."
    return attempts_number


# A list of test strings to pass in to the play_game function and their correct answers.
# Each string for test should finish with " ".

game_rounds_list = [["The capital of the USA is __1__. The capital of Russia is __2__. The capital of the UK is __3__. Canberra is the capital city of __4__. ", ["Washington", "Moscow", "London", "Australia"]],
                ["The __1__ System is the gravitationally bound system comprising the __2__ and the objects that orbit it. The __1__ System formed 4.6 billion years ago from the gravitational collapse of a giant interstellar molecular cloud. The vast majority of the system's mass is in the __2__, with the majority of the remaining mass contained in __3__. The four smaller inner planets, Mercury, Venus, __4__ and __5__, are terrestrial planets, being primarily composed of rock and metal. __4__ (the third planet from the __2__) is the largest and densest of the inner planets, the only place where life is known to exist. The four outer planets are giant planets, being substantially more massive than the terrestrials. The two largest, __3__ and Saturn, are gas giants, being composed mainly of hydrogen and helium. The __1__ System also contains smaller objects. The asteroid belt, which lies between the orbits of __5__ and __3__.  Source: https://en.wikipedia.org/ ", ["Solar", "Sun", "Jupiter", "Earth", "Mars"]],
                ["__1__ is a country in the northern part of North America. Its ten provinces and three territories extend from the __2__ to the Pacific and northward into the Arctic Ocean, making it the world's second-largest country by total area. __1__'s southern __3__ with the United States is the world's longest bi-national land __3__. The majority of the country has a cold or severely cold winter climate, but southerly areas are warm in summer. __1__ is sparsely populated, the majority of its land territory being dominated by forest and tundra and the Rocky Mountains. It is highly urbanized with 82 per cent of the 35.15 million people concentrated in large and medium-sized cities, many near the southern __3__. Its capital is __4__, and its largest metropolitan areas are __5__, Montreal and Vancouver. Source: https://en.wikipedia.org/ ", ["Canada", "Atlantic", "border", "Ottawa", "Toronto"]]]

# This function is to print line breaks in long strings.
# paragraph_border is to make more emphasis
# i is for the number of symbols withing one line, j is to memorize the previous i number before line break
# The number 150 for the line length was chosen arbitrary, without any special meaning

def shorter_line_print(test_string):
    paragraph_separator = "*"*150
    print paragraph_separator
    i = 0
    j = 0
    while i <=  len(test_string):
        i += 150
        if i >= len(test_string):
            i = len(test_string)
            print test_string[j:i]
            break
        else:
            while test_string[i] != " ":
                i += 1
        print  test_string[j:i]
        j = i + 1
    return paragraph_separator






# This part is to ask for the user' s answer
def user_type_and_check(test_string, correct_answers, attempts_number, name):
    # Print the paragraph for user to see
    print "Here is the text to fill in the blanks: "
    print shorter_line_print(test_string)
    # Definition of counters. current_blank_number is to count the blanks to fill. current_attempt is for wrong guesses counting
    current_blank_number = 1
    current_attempt = 0
    test_list = test_string.split()
    # condition to finish the game
    game_over = False
    while (current_blank_number <= len(correct_answers)):
        # current_blank_string is to create the string to search for. Its format is "__number__"
        current_blank_string = "__{0}__".format(str(current_blank_number))
        # asking the user for the guesse to fill in the blank
        for word in test_list:
            if current_blank_string in word:
                user_answer = raw_input("WHAT IS YOUR GUESS FOR THIS BLANK " + current_blank_string + " : ")
                # compare the user's answer with the correct one
                if user_answer == correct_answers[current_blank_number-1]:
                    print "It is a good choice, " + str(name) + ". Your answer is correct."
                    #correct_answers_counter += 1
                    # replace all occurrences
                    test_string = test_string.replace(current_blank_string, correct_answers[current_blank_number-1])
                    print  "After you fill in this blank, the current version of the paragraph is: "
                    print shorter_line_print(test_string)
                    current_blank_number += 1
                    break
                # if the user's answer is not correct, it is necessary to reduce the number of guesses/attempts
                else:
                    current_attempt += 1
                    if current_attempt > attempts_number:
                        print "Oh no! It is not a good answer and it was your last guess... I have some bad news for you, " + str(name) + ", you have lost..."
                        game_over = True
                        break
                    print str(name) + ", it is not a good answer. Try again! You have " + str(attempts_number - current_attempt) + " guesses left. Make it count!"
        if game_over:
            break
        if current_blank_number > len(correct_answers):
            print "Congrats, " + str(name) + "! You have filled correctly all the blanks in this paragraph!"
            break
    return game_over



# This part is the main game logic. The list game_rounds_list structure has the following structure [[test_string, [correct_answers]]]
def play_game(game_rounds_list):
    # To introduce the user
    name = user_name()
    # To ask for the difficulty level of the game
    chosen_attempts_number = choose_the_level(name)
    # to define the number of paragraphs
    game_rounds = len(game_rounds_list)
    current_game_round = 0
    while current_game_round < game_rounds:
        # To choose the question and the correct answer from our list of questions and answers
        current_test = game_rounds_list[current_game_round]
        attempts_number = chosen_attempts_number
        test_string = current_test[0]
        correct_answers = current_test[1]
        if current_game_round < game_rounds:
            print "So, I have the total of " + str(game_rounds) + " paragraphs to fill in the blanks. Here is the paragraph number "+ str(current_game_round+1)
            game_over = user_type_and_check(test_string, correct_answers, attempts_number, name)
            current_game_round += 1
        if game_over:
            break
        if current_game_round == game_rounds:
            print str(name) + '! You have answered ALL my questions. WOW!!!'
            break


    final_message = "Game over! Thank you for playing!"
    return final_message

print play_game(game_rounds_list)

