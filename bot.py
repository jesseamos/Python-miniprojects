import requests
import sys
def get_chat_bot_response(user_query,name):
    url = "https://chat-gpt-ai-bot.p.rapidapi.com/GenerateAIWritter"

    querystring = {"prompt": user_query}

    headers = {
        "x-rapidapi-key": "e5067dc6bamsh8d2b7c842fd530dp103b7ejsn4542ff994181",
        "x-rapidapi-host": "chat-gpt-ai-bot.p.rapidapi.com"
    }
    isloading = False
    try:
        isloading = True
        if isloading : print("\n🤖 loading...\n") 
        response = requests.get(url, headers=headers, params=querystring)
        isloading = False
        print(f"\nChat_bot🤖:\n\n{response.text}\n\n") 
        if response.headers.get('Content-Type') == 'application/json':
            data = response.json()
            print(data)
        else:
            print("\n")
        
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    finally :
        isloading = False    

def chat_bot (name="User"):
    print(f"\nChat_bot🤖:\nHello {name}, What is on your mind🤯")
    
    def user_prompt():
        print(f"\n{name}👤:\n")
        user_query = input()
        get_chat_bot_response(user_query,name)
        prompt_or_exit=input(f"\n{name}, to exit the prompt 'e' \n to prompt again 'r'")
        if prompt_or_exit.lower() not in ["e", "r"]:
            print("\n{name}, you must enter either 'e' or 'r'")

        if prompt_or_exit.lower() == 'e':
            sys.exit()
        else :
            user_prompt()    
    user_prompt()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="provides a personalized chat experience." 
    )

    parser.add_argument(
        "-n","--name",metavar="name",
        required=True,help="The name of the person chatting."
    )
    args = parser.parse_args()
    chat_bot(args.name)