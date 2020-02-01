list_of_objects = []
pet_name = []

def Intro():
    line_1 = " Once upon a time..."
    line_2 = "There was a young boy named jack who lived on a farm with his widowed mother.\n"
    line_3 = "This was not a great farm, as they only had one old dairy cow.\n"
    line_4 = "When the cow stopped giving milk, Jack's mother asked him to sell the cow at the market.\n"
    line_5 = "On the way, Jack meets a hooded figure who offers magic beans in exchange for the cow.\n"
    line_6 = "Entranced by his story of terrifying giants and gold,\n he makes the trade and excitedly brings the magic beans home.\n"
    line_7 = "His mother is furious that Jack made such an idiotic trade and tosses the beans out the window.\n"
    line_8 = "Jack goes to bed.\n"
    line_9 = "The next morning, he wakes up and sees a giant beanstalk that reaches to the clouds right outside his window.\n"
    line_10 = "Remembering the hooded stranger's stories, he climbs up the beanstalk to a land high in the sky.\n"
    line_11 = "In the distance you see an old castle.  You have two options.  Would you like to:\n"
    line_12 = "A:  Go into the castle\n"
    line_13 = "B:  Explore outside first"
    print(line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9, line_10, line_11, line_12, line_13)

def Explore():
    print("You decide to explore outside the castle first.")
    print("While walking around, you notice something shiny under a nearby bush.")
    print("Upon closer inspection, you discover a golden key!")
    print("Thinking that it may prove useful later, you decide to pocket it.")
    list_of_objects.append("key")

def Door():
    print("Unfortunately you have chosen incorrectly!  You have stumbled into the kitchen and there is a giant standing at the sink with her back towards you.")
    print("She turns around and although you try to hide, sees you running behind the leg of one of her chairs.")
    print("To be able to leave the room, she says, you must play her favorite game...")
    print("Hangman!")
    print("Welcome to Hangman!")
    print("The game is about to begin.")
    print("You have ten tries to guess the word")
    print("Go!")
    word = "golden"
    word_list = []
    guessed = []
    for char in word:
        word_list.append(char)
    for i in range (len(word)):
        guessed.append("_")
    times = 0
    while guessed != word_list and times < 10:
        print(*guessed, sep=' ')
        guess = input("enter a letter: ")
        if guess in word_list:
            print("correct")
            position = [i for i, x in enumerate(word_list) if x == guess]
            for i in position:
                guessed[i] = guess
        else:
            print("incorrect")
            times += 1
        if times == 10:
            print("you lose):\nthe word was", word, "unfortunately the giant will not let you go on your way")
            print("the game is over")
        elif guessed == word_list:
            print("you won! the word was GOLDEN")
            print("you were able to escape the giant! you may now continue on your way!")
        else:
            print("you have guessed incorrectly", times, "times")
     
def Hallway():
    l1 = "Near the end of the hallway, you notice a frightening animal approach you."
    print(l1)
    print("A: Run away? Or\nB: Let it approach you?")
    option = input("What do you do?: ")
    if option == "A":
        print("Surprisingly, it doesn’t chase you. You go on your way.")
    if option == "B":
        print("The animal nuzzles into your hand and starts following you.")
        pet = input("What would you like your pet's name to be?: ")
        pet_name.append(pet)
        list_of_objects.append("pet")

def follow_noise():
    print("Good job! By following the noise you have stumbled across the giant's golden goose!\nThe goose and the giant seem to be having an argument.")
    if "key" in list_of_objects:
        print("Because you chose to go outside and got the key...")
    else:
        print("Because you did not chose to first explore outside...")
        print("RIDDLE")
        print("to open the cage, you must complete this riddle")

def Ignore_Noise():
    print("You continue down the hallway and stumble across a door leading outside. You open the door.")
    if "pet" in list_of_objects: #pet rolls in grass
        print(pet_name[0], "bounds outside excitedly and rolls around in the grass.") 
    if "key" in list_of_objects: #if you already have the key, nothing happens
        print("You see a familiar bush. \n 'Well that was pointless.'")
    else: #you find the key
        print("You find a golen key in a bush! You decide to pocket it.")
        list_of_objects.append("key")
    print("You head back inside.")
    if "pet" in list_of_objects: #pet follows
        print(pet_name[0], "follows, happily covered in grass stains.")
        


def Story():
    Intro()
    castle_or_explore = input("enter A or B: ")
    if castle_or_explore == "B":
        Explore()
    if castle_or_explore == "A" or "B":
        print("You enter the castle.  On your left, you notice a big door.  In front of you, there is a long hallway.")
        print("Which way do you go?\nA:  through the big door\nB:  down the long hallways")
        door_or_hallway = input("enter A or B: ")
        if door_or_hallway == "A":
              Door()
        elif door_or_hallway == "B":
            Hallway()
    print("As you continue on your way, you hear a noise down the West Wing.\nYou are met with another decision.")
    print("Do you\nA: Follow the noise\nB: Ignore the noise.")
    noise = input("enter A or B: ")
    if noise == "A":
        follow_noise()
    elif noise == "B":
        Ignore_Noise()

    
        
        
    

    
