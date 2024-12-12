import nltk
from nltk.chat.util import chat,reflection

pairs = [
    [
        r"Hi|Hey|Hello",
        ["Hello","Hey"]
    ],
    [
        r"What is your name ?",
        ["You can call me chatbot",]
    ],
    [
        r"How are you ?",
        ["I am doing good","I'm fine"]
    ],
    [
        r"Sorry",
        ["Its alright","its ok ,never mind"]
    ],
    [
        r"I love you",
        ["I love you too"]
    ],
    [
        r"Bye",
        ["Bye , it was nice taking to you :)"]
    ],
]
chatbot=chat(pairs,reflections)
chatbot.converse()