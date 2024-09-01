
mood = input("What are you feeling today? ")
weather = input("What is the temperature today? ")
event = input("Formal or casual? ")

if mood == "happy":
    if weather == "warm" and event == "casual":
        print("Wear a sundress!")
    elif weather == "warm" and event == "formal":
        print("Wear shorts and a nice shirt")
    elif weather == "cold" and event == "casual":
        print("Wear a nice warm suit")
    elif weather == "cold" and event == "formal":
        print("Stay cool but classy")
elif mood == "sad":
    if weather == "warm" and event == "casual":
        print("Wear dark colors for your t-shirt and shorts")
    elif weather == "warm" and event == "formal":
        print("It's warm, but you should still dress nice!")
    elif weather == "cold" and event == "casual":
        print("Have fun with your outfit")
    elif weather == "cold" and event == "formal":
        print("Stay classy but warm and cheery!")
