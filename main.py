from tkinter import *

import speech_recognition
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import pyttsx3
import speech_recognition
import threading

bot = ChatBot('Bot')
trainer = ListTrainer(bot)

# code for training the data from files

# for files in os.listdir('data/english/'):
#     data = open('data/english/' + files, 'r', encoding='utf-8').readlines()
#     trainer.train(data)


#CODE TO TRAIN SINGLE DIRECT FILE
# data = open('data/english/greetings.yml', 'r', encoding='utf-8').readlines()
# trainer.train(data)

#code to train data directly
# conversations = [
#     ("What is your name?", "I am a chatbot."),
#     ("How are you?", "I am doing well, thank you."),
#     ("Tell me a joke.", "Why did the chicken cross the road? To get to the other side."),
#
# ]
# dialogues = [Statement(text=question, in_response_to=answer) for question, answer in conversations]
# training_data = [(statement.text, statement.in_response_to) for statement in dialogues]
# trainer.train(training_data)



def botReply():
    question = questionfield.get()
    question = question.capitalize()
    answer = bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END, 'Bot: '+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionfield.delete(0,END)

def audio_to_text():
    while True:
        sr=speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone()as m:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                query=sr.recognize_google(audio)


                questionfield.delete(0,END)
                questionfield.insert(0,query)
                botReply()
        except Exception as e:
            print(e)





root = Tk()

root.geometry('500x570+100+30')
root.title('RailRoute Bot')
root.config(bg='black')

logoPic = PhotoImage(file='images/bot22.png')

logopiclabel = Label(root,image=logoPic,bg='black')
logopiclabel.pack()


centerframe =Frame(root)
centerframe.pack(pady=8)

scrollbar = Scrollbar(centerframe)
scrollbar.pack(side = RIGHT)

textarea = Text(centerframe,font=('times new roman',14,'italic'),height=15,yscrollcommand=scrollbar.set,bg='grey',wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)


questionfield = Entry(root,font=('times new roman',14,'italic'))
questionfield.pack(pady=15,fill=X)
askpic=PhotoImage(file='images/ask1.png')
askbutton = Button(root,image=askpic,bg='black',command=botReply)
askbutton.pack()
def click(event):
    askbutton.invoke()


root.bind('<Return>',click)
thread=threading.Thread(target=audio_to_text)
thread.setDaemon(True)
thread.start()

root.mainloop()


