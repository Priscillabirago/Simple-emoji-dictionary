# creating a dictionary contains some moods with their corresponding emojis
mood = {
    "sad": "☹",
    "happy": "☺",
    "angry": "😠",
    "annoyed": "😒",
    "confused": "🤨",
    "shocked": "😮",
    "silent": "🤐",
    "tired": "🥱",
    "frustrated": "😫",
    "calm": "😌",
}
#user inputs their mood
Mood = input("Which of the word above best describes your mood today:")
#iterates through the dictionary to find the emoji that corresponds with the user's mood and prints the appropriate message depending on if the mood could be found or not
for item in mood:
    if Mood in mood:
        result = mood.get(Mood)
        print("You are " + str(result) + " today")
        break
    if Mood not in mood:
        print("Sorry,your mood cannot be found in this dictionary:( Check the spelling of the word or try another word that can be found in the options provided.")
        break
