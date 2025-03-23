import random

answers = [
    "Yes - definitely.", "Without a doubt.", "Reply hazy, try again.",
    "Ask again later.", "Better not tell you now.", "My sources say no.",
    "Outlook not so good.", "Very doubtful."
]

questions = [
    "Is codedex better than udemy yet?", "Is the sky blue?", "Is the earth flat?",
    "Is the moon made of cheese?", "Is the sun hot?", "Is the ocean wet?",
    "Is the grass green?", "Is the pope catholic?"
]

while True:
    question = input("Ask the magic 8 ball a question or press Enter for a random question: ")

    if question == "":
        question = random.choice(questions)
        print("Question: " + question)
        print("Magic 8 ball: " + random.choice(answers))
        break # this is to stop the loop after the random question is answered
    if question.lower() == "exit" or "quit":
        print ("Bay")
        break
    else:
        print("Question: " + question)
    print("Magic 8 ball: " + random.choice(answers))
