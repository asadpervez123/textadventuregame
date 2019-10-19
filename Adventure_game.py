"""Created on Thu October 17 02:22:45 2019
@author: Mohammad Asad Pervez"""

"""
DocString:    

A) Introduction:

    A game many Job Seekers can related to.

    For you, things aren't going as you had hoped. You are nearing the end of your degree in Data Science
    and you still haven't landed a job. But don't worry! You are in a DATA SCIENCE CONFERENCE and the person 
    who can give you your dream job is here too. But there is a problem! You don't know who that person is 
    and how to reach them. However, you have expert networking skills. You can find your way to anyone!

Stage 1: You spot an HR Manager
Stage 2: You Socialize with a Project Manager
Stage 3: You find Waldo


B) Run this file on a terminal with Python 3 installed

c) Make sure you have the 'waldo.jpg' file provided with this document saved in the same location as this file.

D) EASTER EGG : if you type 'ignore her' as your answer in Stage 1, it will unlock a BONUS ROUND! (Warning: Your game time will increase)

E) Known Bugs and/or Errors: None.

"""

#Importing Necessary Libraries
import time
import random
from PIL import Image,ImageFilter  

# Creating a Yes an No list of possible Yes or No values for future use in the code
yes_list = ['Y', 'y', 'yes', 'Yes', 'YES']
no_list  = ['N', 'n', 'NO', 'no', 'No']



#Start of the Game
print (f"""


 $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\  $$$$$$$$\ $$\   $$\  $$$$$$\  $$$$$$$$\       $$\   $$\ $$\   $$\ $$\   $$\ $$$$$$$$\        $$$$$$\  $$\      $$\  $$$$$$\   $$$$$$\        $$\ $$\ $$\ 
$$  __$$\ $$  __$$\ $$$\  $$ |$$  _____|$$  _____|$$  __$$\ $$  _____|$$$\  $$ |$$  __$$\ $$  _____|      $$ |  $$ |$$ |  $$ |$$$\  $$ |\__$$  __|      $$  __$$\ $$ | $\  $$ |$$  __$$\ $$  __$$\       $$ |$$ |$$ |
$$ /  \__|$$ /  $$ |$$$$\ $$ |$$ |      $$ |      $$ |  $$ |$$ |      $$$$\ $$ |$$ /  \__|$$ |            $$ |  $$ |$$ |  $$ |$$$$\ $$ |   $$ |         $$ /  \__|$$ |$$$\ $$ |$$ /  $$ |$$ /  \__|      $$ |$$ |$$ |
$$ |      $$ |  $$ |$$ $$\$$ |$$$$$\    $$$$$\    $$$$$$$  |$$$$$\    $$ $$\$$ |$$ |      $$$$$\          $$$$$$$$ |$$ |  $$ |$$ $$\$$ |   $$ |         \$$$$$$\  $$ $$ $$\$$ |$$$$$$$$ |$$ |$$$$\       $$ |$$ |$$ |
$$ |      $$ |  $$ |$$ \$$$$ |$$  __|   $$  __|   $$  __$$< $$  __|   $$ \$$$$ |$$ |      $$  __|         $$  __$$ |$$ |  $$ |$$ \$$$$ |   $$ |          \____$$\ $$$$  _$$$$ |$$  __$$ |$$ |\_$$ |      \__|\__|\__|
$$ |  $$\ $$ |  $$ |$$ |\$$$ |$$ |      $$ |      $$ |  $$ |$$ |      $$ |\$$$ |$$ |  $$\ $$ |            $$ |  $$ |$$ |  $$ |$$ |\$$$ |   $$ |         $$\   $$ |$$$  / \$$$ |$$ |  $$ |$$ |  $$ |                  
\$$$$$$  | $$$$$$  |$$ | \$$ |$$ |      $$$$$$$$\ $$ |  $$ |$$$$$$$$\ $$ | \$$ |\$$$$$$  |$$$$$$$$\       $$ |  $$ |\$$$$$$  |$$ | \$$ |   $$ |         \$$$$$$  |$$  /   \$$ |$$ |  $$ |\$$$$$$  |      $$\ $$\ $$\ 
 \______/  \______/ \__|  \__|\__|      \________|\__|  \__|\________|\__|  \__| \______/ \________|      \__|  \__| \______/ \__|  \__|   \__|          \______/ \__/     \__|\__|  \__| \______/       \__|\__|\__|
                                                                                                                                                                                                                     
  

""")

input ('<Press Enter to know your story> ')

#Initial Instructions
input (f"""

{'-'*220}
    
    Find your way to the person by navigating your way through this text adventure and land your dream job 
    as a prize!


<Press Enter to continue>

{'-'*220}
""")


#Game Starts and prompts name entries
name = input (f"""


    Enter you Name: """)
 
name_so = input (f"""

    What is the name of your significant other? (If you are single, write any name): """)

print(f"""

{'-'*220}

    Nice! Welcome {name}.                                                                                                                                                                                                                                                                                                                                                                                              
""")

time.sleep(1.5)

#Defining BONUS STAGE or EASTER EGG STAGE
def bonus_stage():
    """ Defining Stage 1 of the game"""
   
    input(f"""
    
    {'-'*220}

      ______     ___           _______.___________. _______ .______          _______   _______   _______    .______        ______    __    __  .__   __.  _______  
    |   ____|   /   \         /       |           ||   ____||   _  \        |   ____| /  _____| /  _____|   |   _  \      /  __  \  |  |  |  | |  \ |  | |       \ 
    |  |__     /  ^  \       |   (----`---|  |----`|  |__   |  |_)  |       |  |__   |  |  __  |  |  __     |  |_)  |    |  |  |  | |  |  |  | |   \|  | |  .--.  |
    |   __|   /  /_\  \       \   \       |  |     |   __|  |      /        |   __|  |  | |_ | |  | |_ |    |      /     |  |  |  | |  |  |  | |  . `  | |  |  |  |
    |  |____ /  _____  \  .----)   |      |  |     |  |____ |  |\  \----.   |  |____ |  |__| | |  |__| |    |  |\  \----.|  `--'  | |  `--'  | |  |\   | |  '--'  |
    |_______/__/     \__\ |_______/       |__|     |_______|| _| `._____|   |_______| \______|  \______|    | _| `._____| \______/   \______/  |__| \__| |_______/ 
         

        You ignore {name_so} and talk the person standing next to her; Darrin.


    <Press Enter to talk to him>

    
    """)

    #Start of Conversation
    print(f"""

        You    : Hi, I’m {name}. Can you help me find a position in your comapny? 

    """)

    {time.sleep(2)} #Delaying Printing


    print(f"""

        Darrin : Hi! I'm Darrin. I would love that! Do you mind if I stay in touch with you? 

    """)

    {time.sleep(5)} #Delaying Printing


    #Question
    ans_1 = input ("""

    What do you do? >

    A.	Give him your LinkedIn.
    B.	Give him your LinkedIn and your phone number.
    C.	Give him the keys of your house.


    Enter A, B or C -> """)

    #LowerCase the Answer
    ans_1 = ans_1.lower()

    #MCreating List of possible and acceptable answers
    s1ans_1_list = ['a','A','linkedin','LinkedIn','linked in', '1', 'a.', 'A.', 'linkedin only']
    s1ans_2_list = ['b', 'B', 'linkedin and phone', 'linkedin and phone number', 'linkedin and number', '2', 'b.', 'B.']
    s1ans_3_list = ['c', 'C', 'keys', 'keys of house', 'key', '3', 'c.', 'C.']

    #Checking if Answers Match
    if (ans_1 in s1ans_1_list):
        input("""
        
    Darrin : Great! Thanks for connecting with me. I’m just an intern here and will be looking for a permanent job 
             soon. I’ll touch base with you soon. Maybe Michael, our product manager can help you.


    <Press Enter to Continue>

            """)
        

    elif (ans_1 in s1ans_2_list):
        input ("""
        
    Darrin : Amazing! I’m just an intern here and need a job urgently. I’ll call you on the weekends.
             Maybe Michael, our product manager can help you.

            
    <Press Enter to Continue>      
            """)

    elif (ans_1 in s1ans_3_list):
        input ("""
    Darrin : Oh, Thank God! I’m just an intern here and needed a place to stay in San Francisco. 
             I’ll be crashing at your place from now. Maybe Michael, our product manager can help you.


    <Press Enter to Continue>

            """)

    #Prompting an invalid input and re-asking the code
    elif (ans_1 not in s1ans_1_list and ans_1 not in s1ans_2_list and ans_1 not in s1ans_3_list):
        print ("""
    
    That's not a valid input. Please try again""")
        bonus_stage()

    else:
        print ("""
    Something went wrong!""")



#Start of Stage 1 and conversations
input (f"""

{'-'*220}



     _______.___________.    ___       _______  _______     __  
    /       |           |   /   \     /  _____||   ____|   /_ | 
   |   (----`---|  |----`  /  ^  \   |  |  __  |  |__       | | 
    \   \       |  |      /  /_\  \  |  | |_ | |   __|      | | 
.----)   |      |  |     /  _____  \ |  |__| | |  |____     | | 
|_______/       |__|    /__/     \__\ \______| |_______|    |_| 
                                                                



    You look around for people to network with. You notice a woman sitting alone staring at her phone and another person 
    that has (HR) written on their name tag under their name. And the name is...can it be? The name is {name_so}.
    Perfect! you have something to start conversation. You approach them and begin talking.


<Press Enter to Start Conversation>

""")

print (f"""

    You : Hi! Did you know you share the same name as my significant other? 

""")

time.sleep (2.5)
print (f"""

    {name_so} : Really? What a coincidence! How can I help you? 

""")

time.sleep (3)
print (f"""

    You : I was wondering if there are any open positions at your company. And whether you can help me find a suitable position? 

""")

time.sleep (6)

print (f"""

    {name_so} : I suggest you apply on the company's website.

""")

time.sleep (2.5)

#Defining Stage 1
def stage_2 ():
    """ Defining Stage 2 of the game"""

    ans_2 = input(f"""

    You know applying online never works! It's the most standard answer HR managers give to get rid of you. What do you do?

        A.	Say ‘Ok’ and walk away.
        B.	Rant about how that never works.
        C.	Ask if that is how she got her job.

Enter A, B or C -> """)
    
    ans_2 = ans_2.lower()
    
    #Creating List of all acceptable answers.
    s2ans_1_list = ['A', 'a', '1', 'okay', 'ok', 'Ok', 'walk away', 'walk', 'A.', 'a.']
    s2ans_2_list = ['B', 'b', '2', 'rant', 'Rant', 'b.', 'B.']
    s2ans_3_list = ['C', 'c', '3', 'ask about job', 'ask her', 'ask', 'C.', 'c.', 'job']

    #Checking if Answers match
    if (ans_2 == 'ignore her'):
        bonus_stage()

    elif (ans_2 in s2ans_1_list):

            #Defining Retry argument
            def trag():
                """ Defining a retry function for users wanting to try again"""

                try_again = input("""
                
                 C’mon, don’t give up that easy. Try again? (Y/N) : 

                    """)            
                
                #Checking Inputs
                if try_again in yes_list:
                            stage_2()
                
                elif try_again in no_list:
                    time.sleep(5)
                    exit()
                
                elif try_again not in yes_list and try_again not in no_list:
                    print ("""
                    Not a valid input. Please answer again""")
                    trag()
                
                else :
                    print ('Something went wrong!')

            trag() #Calling Retry Argument

    elif (ans_2 in s2ans_2_list):

            def trag_2():  #Defining Retry Argument
                """ Defining a retry function for users wanting to try again"""
        
                try_again_B = input (f"""
        
                {name_so} :  “I don’t know how your significant other puts up with you. Back off or I am calling the cops.” 
            
                Try again? (Y/N) ->
            
                 """)
                
                #Checking in Yes and No Lists

                if try_again_B in yes_list:
                    stage_2()
        
                elif try_again_B in no_list:
                    print ('Thank you for playing!')
                    time.sleep (5)
                    exit()
                
                elif try_again_B not in yes_list and try_again_B not in no_list:
                    print ("""
                    Not a valid input. Please try again""")
                    trag_2()
                
                else :
                    print ('Something went wrong!')    

            trag_2()


    elif (ans_2 in s2ans_3_list):
        print (f"""
    {name_so} : It’s a funny story, a friend of mine referred me for this position…..oh, I get your point. 
                I would love to help. But I can’t, you see, I am leaving the company myself and serving my notice. 
                I think I saw ‘Michael’, one of our Project Managers by the game table. I’m sure he can help you out.
                    
            """)
    
        
    elif (ans_2 not in s2ans_1_list and ans_2 not in s2ans_2_list and ans_2 not in s2ans_3_list): #Invalid Entry
        print("""That's not a valid entry. Please try again.""")
        stage_2() #Calling Stage 1
    
    
    
    else:
        print ('Something went wrong!')

stage_2() #Calling Stage 1

time.sleep(3)

#Start of Stage 2
input(f"""

{'-'*220}

     _______.___________.    ___       _______  _______     ___   
    /       |           |   /   \     /  _____||   ____|   |__ \  
   |   (----`---|  |----`  /  ^  \   |  |  __  |  |__         ) | 
    \   \       |  |      /  /_\  \  |  | |_ | |   __|       / /  
.----)   |      |  |     /  _____  \ |  |__| | |  |____     / /_  
|_______/       |__|    /__/     \__\ \______| |_______|   |____| 
                                                                  

    You look for Michael at the games table and find him playing some sort of ‘Number’ game. You walk up to him and introduce yourself.

<Press Enter to Start Conversation>

""")

print("""

    Michael: Hey! I would love to talk but I’m too involved in his game and I am really trying hard to win.

""")

time.sleep(4.5)

input("""

    You take a look and the rule of the game is simple, a 6-face dice is rolled 10 times. If you guess how many 3s show up. You win. 
    You feel that if you can help Michael win, he can help you. You get three guesses.


<Press Enter to Play>
""")

print(f"""

    You : I think I got this. Let me give it a shot.
""")

def stage_3(): #Defining Stage 2
    """Defining Stage 3 of the game"""

    dice_rolls = [] #Create Empty List to fill in values with Dice Rolls

    time.sleep(1.5)

    input(f"""
    Michael : You sure? Be my guest...



<Press enter to roll the dice 10 times.>

    """)
    chances = 3                                     #Set Initial value of chances to 3 for 3 tries

    for number in range (1,11):
        number = random.randint(1,6)                #Generate Random Number
        dice_rolls.append(number)                   #Add generated number in the created list

    count_of_three = dice_rolls.count(3)            #Get the count of '3' rolled
    
    while chances > 0 :                             #While Loop
        
        while True:
            
            try:        
                guess = int(input ("""              

How many 3s were rolled? Guess the number ->

                """))
                break
            
            except ValueError:                      #Handling Value Error
                print("""
That's not a number silly! Please enter a number. """)
                
            
        if guess == count_of_three:                 #If the Guess is corrent

            input(f"""

    Michael: That’s exactly right. The numbers were {dice_rolls} and there were {count_of_three} 3s. 
             That’s Amazing! But I’m afraid I can’t help you, my team is already full.

<Press Enter to Continue>

            """)
            break
            
            
        elif guess != count_of_three:               #Loosing a Chance if the guess is incorrect
            chances -= 1

            if chances > 0:
                print(f"""
That's incorrect. You have {chances} guesses remaining.

""")
                continue
            
            elif chances == 0:                      #When no more guesses left
                input (f"""
                
    Michael: Oh no! The numbers were. {dice_rolls} and there were {count_of_three} 3s.
             You lost the game for me. This is unacceptable! Please leave me alone.
                
<Press Enter to Continue>

                """)
            break

        else:
                print ("Something went wrong!")

stage_3 ()


input (f"""
{'-'*220}

    You lose all hope. Feeling defeated you go and sit next to the lady you noticed staring at her phone earlier. 
    She is still staring at it, like she is looking at something important. You get curious:

<Press Enter to talk to her>

""")

#Last Stage Starts
print (f"""


     _______.___________.    ___       _______  _______     ____   
    /       |           |   /   \     /  _____||   ____|   |___ \  
   |   (----`---|  |----`  /  ^  \   |  |  __  |  |__        __) | 
    \   \       |  |      /  /_\  \  |  | |_ | |   __|      |__ <  
.----)   |      |  |     /  _____  \ |  |__| | |  |____     ___) | 
|_______/       |__|    /__/     \__\ \______| |_______|   |____/  
                                                                      


    You : Hi! I’m {name}. What are you looking at?

""")

time.sleep (3)

print (f"""

    Sarah : Hi, I’m Sarah. I need your help. I have a 3-year-old daughter, Amelia. She is at home and the babysitter says 
            she won’t go to sleep until she has found Waldo in all of the pictures in her book. She is stuck on the last 
            picture. Can you help spot him? I’ll owe you one.

""")


time.sleep(6)

waldo = input ("""

    You squint your eyes and take a hard look. Your evening comes down to this. Finding Waldo. 
                
<Press enter to find 'Waldo' and answer the next question>
                
                """)



#Read image
im = Image.open('waldo.jpg')

#Display image  
im.show()

#Defining Final Stage
def stage_4():
    """Defining Stage 4 of the game"""
    
    #Listing all acceptable answers
    s4ans_1_list = ['A','a','1','b','B','center stage', 'stage', 'circus', 'center', 'centre', 'c', 'C', 'C.','c.','A.','a.','B.','b.','2','3', 'behind lion', 'next to circus master']

    waldo_ans = input ("""

    Where's Waldo?

    A. In the center of the stage
    B. A
    C. B

    Please enter your answer: 

    """)

    waldo_ans = waldo_ans.lower()
    
    #Checking if Answers match
    if waldo_ans in s4ans_1_list:
        print(f"""

        Sarah : That's right! Thank you so much!!! She will finally go to sleep now. I suddenly feel so blind. 
                It’s been a pleasure meeting you {name}. What do you do?

                """)
    elif waldo_ans not in s4ans_1_list:
        wrong_ans = input(f"""
        
        That's the wrong answer. Look again? (Y/N): """)

        if wrong_ans in yes_list:
            stage_4()
        
        elif wrong_ans in no_list:
            print('Thank You for playing!')
            time.sleep(5)
            exit()

    else:
        print ('Something went wrong!')



#Calling the Final Stage
stage_4()



time.sleep(5)

print(f"""

    You : I’m a student 6 months away from finishing my Master in Data Science.

""")

time.sleep(2)

final_ans = input("""

    Sarah : That’s so nice. I work for Microsoft as a project manager and I’m always looking for Analysts to joining my team. 
            We specially need someone with a good eye like yours to go through all that code. I’m sure offers must be pouring 
            in for you but do consider joining my team after you graduate. I would love to stay in touch:

    A.	“Yes. I would love that.”
    B.	“I’ll think about it.” And walk away like a cool guy walking away from an explosion without looking.
    C.	“I don’t have any offers. And I would love to join your team.”

Enter your answer -> 

""")

# Final Message

time.sleep(3)
print (f"""
{'-'*220}

RING! RING! RING! You wake up from your dream. Your alarm clock wakes you up. It’s time to get ready for your 
Data Science in Python class with Professor Chase Kusterer. He has always liked you and your work. You should 
probably tell him about this dream you had...Maybe code it.


Good Luck with you Job Search!


                                                                                                                                                                      
                                                                   dddddddd                                                                                           
        GGGGGGGGGGGGG                                              d::::::d     LLLLLLLLLLL                                                   kkkkkkkk            !!! 
     GGG::::::::::::G                                              d::::::d     L:::::::::L                                                   k::::::k           !!:!!
   GG:::::::::::::::G                                              d::::::d     L:::::::::L                                                   k::::::k           !:::!
  G:::::GGGGGGGG::::G                                              d:::::d      LL:::::::LL                                                   k::::::k           !:::!
 G:::::G       GGGGGG   ooooooooooo      ooooooooooo       ddddddddd:::::d        L:::::L               uuuuuu    uuuuuu      cccccccccccccccc k:::::k    kkkkkkk!:::!
G:::::G               oo:::::::::::oo  oo:::::::::::oo   dd::::::::::::::d        L:::::L               u::::u    u::::u    cc:::::::::::::::c k:::::k   k:::::k !:::!
G:::::G              o:::::::::::::::oo:::::::::::::::o d::::::::::::::::d        L:::::L               u::::u    u::::u   c:::::::::::::::::c k:::::k  k:::::k  !:::!
G:::::G    GGGGGGGGGGo:::::ooooo:::::oo:::::ooooo:::::od:::::::ddddd:::::d        L:::::L               u::::u    u::::u  c:::::::cccccc:::::c k:::::k k:::::k   !:::!
G:::::G    G::::::::Go::::o     o::::oo::::o     o::::od::::::d    d:::::d        L:::::L               u::::u    u::::u  c::::::c     ccccccc k::::::k:::::k    !:::!
G:::::G    GGGGG::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        L:::::L               u::::u    u::::u  c:::::c              k:::::::::::k     !:::!
G:::::G        G::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        L:::::L               u::::u    u::::u  c:::::c              k:::::::::::k     !!:!!
 G:::::G       G::::Go::::o     o::::oo::::o     o::::od:::::d     d:::::d        L:::::L         LLLLLLu:::::uuuu:::::u  c::::::c     ccccccc k::::::k:::::k     !!! 
  G:::::GGGGGGGG::::Go:::::ooooo:::::oo:::::ooooo:::::od::::::ddddd::::::dd     LL:::::::LLLLLLLLL:::::Lu:::::::::::::::uuc:::::::cccccc:::::ck::::::k k:::::k        
   GG:::::::::::::::Go:::::::::::::::oo:::::::::::::::o d:::::::::::::::::d     L::::::::::::::::::::::L u:::::::::::::::u c:::::::::::::::::ck::::::k  k:::::k   !!! 
     GGG::::::GGG:::G oo:::::::::::oo  oo:::::::::::oo   d:::::::::ddd::::d     L::::::::::::::::::::::L  uu::::::::uu:::u  cc:::::::::::::::ck::::::k   k:::::k !!:!!
        GGGGGG   GGGG   ooooooooooo      ooooooooooo      ddddddddd   ddddd     LLLLLLLLLLLLLLLLLLLLLLLL    uuuuuuuu  uuuu    cccccccccccccccckkkkkkkk    kkkkkkk !!! 
                                                                                                                                                                      
                                                                                                                                                                      


{'-'*220}
""")

time.sleep(10)

exit() #Game Ends