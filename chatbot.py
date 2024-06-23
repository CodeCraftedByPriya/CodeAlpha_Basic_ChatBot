from responses import bot_charts

def intro(name):
  print(f"HELLO!, {name.upper()}!")

def chat():
  name = input("Enter you name: ")
  intro(name)
  chatbot = input("What do you want to call your chatbot?:")
  print("")
  print("-" * 75)
  print("\t\t\t\tEnter EXIT to exit the chat!")
  print("-" * 75)
  while True:
    you = input(f"{name.capitalize()}: "_.strip()
    if you.lower() == "exit":
        print(bot_chats(you))
        break
else:
        print(f"{chatbot}:, bot_chats(you))

if __name__ == "__main__":
      chat()
