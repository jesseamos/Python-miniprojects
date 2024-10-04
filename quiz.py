import requests
from pprint import pprint
import random
import time
import sys
def quiz_game(name="PlayerOne"):
    print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐\n")
    print(f"\n{name}, welcome to the quiz game🤖..     \n")
    print("\n⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  ")
    question_count = 0
    player_wins = 0
    def select_options():
        difficulties = input("\nSelect Difficulties:\n1. Easy🍳\n2. Medium🧑🏽‍🎓\n3. Hard😓\n\n")
        if difficulties not in ["1","2","3"]:
            print(f"\n🤖 {name}, you must enter a number around 1, 2 or 3")
            return select_options()    
        categories = input("\nSelect categories:\n1. General Knowledge\n2. Science: Computers\n3. History\n4. Entertainment: Japanese Anime & Manga\n\n")     
        if categories not in ["1","2","3","4"]:
            print(f"\n🤖 {name}, you must enter a number around 1, 2 or 3")
            return select_options()
        level_type = input("\nSelect Type:\n1. Multiple Choice\n2. True or False\n\n")
        if level_type not in ["1","2"]:
            print(f"\n🤖 {name}, you must enter a number around 1 or 2")
            return select_options()
        def get_quiz_question():
            nonlocal categories
            nonlocal difficulties
            nonlocal level_type
            nonlocal question_count


            if categories == "1":
                categories = "9"
            elif categories == "2":
                categories = "18"     
            elif categories == "3":
                categories = "23"
            else:
                categories = "31"   
                
            #For Difficulities
            if difficulties == "1":
                difficulties = "easy"
            elif difficulties == "2":
                difficulties = "medium"     
            else :
                difficulties = "hard"

            # For Types
            if level_type == "1":
                level_type = "multiple"
            else :
                level_type = "boolean"
            def countdown(t): 
            
                mins, secs = divmod(t, 60) 
                timer = '{:02d}:{:02d}'.format(mins, secs) 
                print(f"you have {timer} left to answer the question ⌛") 
                time.sleep(1) 
                t -= 1
                
                exc_time =input(f"\n🤖{name}, you have exceed your time limit⌛😞\n'T' to try again") 
                print(exc_time)
                if exc_time.lower() == "t":
                    return get_quiz_question
                else:
                    print("you must enter 'T' to try again")
                    get_quiz_question()



            request_url = f"https://opentdb.com/api.php?amount=1&category={categories}&difficulty={difficulties}&type={level_type}"
            quiz_data= requests.get(request_url).json()
            

            question =f"\n\n{quiz_data['results'][0]['question']}🤔❔\n\n"
            correct_answer = f"{quiz_data['results'][0]['correct_answer']}"
            in_correct_answers = quiz_data['results'][0]['incorrect_answers']

            nonlocal question_count
            question_count =+ 1
            print(f"\nQuestion {question_count}🤓:\n{question}\n")
            num = 1
            options_list = in_correct_answers + [correct_answer]
            options = random.sample(options_list,len(options_list))
            for x in options:
                if num <= 4:
                     print( f"\n{num}. {x}")
                     num += 1

            # countdown(10)   
            # print(f"\nyou must answer the question in 10 second⌚\n")
            answer = input("\nAnswer:\n\n")
                   

            
            if answer not in ["1","2","3","4"]:
                print(f"\n🤖 {name}, you must be either 1, 2, 3 or 4")
                return select_options()
            if answer == "1":
                chosen_answer = options[0]
            elif answer == "2":
                chosen_answer = options [1]
            elif answer == "3":
                chosen_answer = options [2]
            else:
                chosen_answer = options [3]

            def next_or_quit_game():
                next_or_quit = input("\nN for Next ⏭️ or \nU to update Options ⬆️ your selection or\nQ to Quit 🚪:\n\n")
                if next_or_quit.lower() not in ["n","q","u"]:
                    print(f"\n🤖Hey {name}, you must either \n'N'⏭️ to go to the next question or \n'U' to update your selection⬆️ \n'Q' to quit the game🚪.\n")
                if next_or_quit.lower() == "n":
                    return get_quiz_question()
                if next_or_quit.lower() == "q":
                    print("\nThanks for Playing🙏🫂")
                    sys.exit(f"\nBye,{name}👋") 
                if next_or_quit.lower() == "u":
                    print("\n🤖Update your selection:\n\n")
                    return select_options()
                return next_or_quit_game
            nonlocal player_wins
            if chosen_answer == correct_answer :
                score =player_wins =+ 1
                print(f"\n🤖Very Impressive {name}, you picked {chosen_answer} and you're correct✅🥳🍾")
                print(f"\nScore: {score}")
                return next_or_quit_game()
            else:
                print(f"\n🤖Sorry {name}, you are wrong❌, you picked {chosen_answer}\nwhile the correct answer is {correct_answer}✅")
                return next_or_quit_game() 
        return get_quiz_question()    

    return  select_options()    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="provides a personalized game experience." 
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of the person playing the game."
    )
    args = parser.parse_args()
    quiz_game(args.name)