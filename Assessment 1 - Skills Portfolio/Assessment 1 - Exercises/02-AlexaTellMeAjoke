
from tkinter import *
import random
from PIL import Image, ImageTk

#main setup
root = Tk()
root.title("Alexa, The Joke Master")
root.geometry("500x700")
root.resizable(False, False)  #size is not resizable for this window, as i believe it was not needed 
root.configure(bg="#F7FAFC") #main bg color
root.iconbitmap('alexa.ico') #icon for alexa 
alexa_image = Image.open("alexa.png")
alexa_image = alexa_image.resize((200, 200), Image.Resampling.LANCZOS)
alexa_photo = ImageTk.PhotoImage(alexa_image)

#displays an image of alexa permanently near the bottom
alexa_label = Label(root, image=alexa_photo, bg="#F7FAFC")
alexa_label.pack(side=BOTTOM, pady=5)


#important variables for this code
jokes = []
current_punchline = ""

#read jokes from the text file given in resources
with open("Assessment 1 - Skills Portfolio/A1 - Resources/randomJokes.txt", "r") as file:
    for line in file:
        if "?" in line:
            setup, punchline = line.strip().split("?", 1)
            jokes.append((setup + "?", punchline))

#function to display a random joke
def tell_joke():
    global current_punchline

    joke = random.choice(jokes)

    setup_label.config(text=joke[0])
    punchline_label.config(text="")
    current_punchline = joke[1]

    
    tell_joke_button.pack_forget() 
    quit_button.pack_forget()

    
    punchline_button.pack(pady=5)
    next_joke.pack(pady=5)
    quit_button.pack(pady=5)

#function to display the punchline
def show_punchline():
    punchline_label.config(text=current_punchline)

#function to get the next joke
def next_joke():
    tell_joke()

#main heading
title_label = Label(root,
    text="Alexa, The Joke Master",font=("Poppins", 20, "bold"),bg="#F7FAFC",fg="#172B3A"
)
title_label.pack(pady=(20, 5))

subtitle_label = Label(root,text="She's the funniest comedian!",font=("Poppins", 10),bg="#F7FAFC",fg="#0086B3"
)
subtitle_label.pack(pady=(0, 15))

#joke display frame
joke_frame = Frame(root,bg="#E8F4FA",padx=14,pady=8
)
joke_frame.pack(padx=55)

#joke setup label
setup_label = Label(joke_frame,text="Click the button below to hear a joke!",font=("Poppins", 10, "bold"),bg="#E8F4FA",fg="#172B3A",wraplength=320,justify="center"
)
setup_label.pack(pady=(8, 5))

#punchline label
punchline_label = Label(joke_frame,text="",font=("Poppins", 10),bg="#E8F4FA",fg="#44B7DD",wraplength=320,justify="center"
)
punchline_label.pack(pady=(0, 8))

#tell a joke button
tell_joke_button = Button(root,text="Alexa tell me a joke!",command=tell_joke,font=("Poppins", 10, "bold"),width=22,bg="#00A8E0",fg="#ffffff",activebackground="#0086B3",activeforeground="#ffffff",relief="flat",bd=0,pady=7
)
tell_joke_button.pack(pady=(15, 5))

#show punchline button
punchline_button = Button(root, text="Punchline!",command=show_punchline,font=("Poppins", 10, "bold"),width=22, bg="#00A8E0",fg="#ffffff",activebackground="#0086B3",activeforeground="#ffffff",relief="flat", bd=0,pady=7
)

#next joke button
next_joke = Button(root,text="HAHA! next please!",command=next_joke,font=("Poppins", 10, "bold"),width=22,bg="#00A8E0",fg="#ffffff",activebackground="#0086B3",activeforeground="#ffffff",relief="flat", bd=0, pady=7
)

#quit button
quit_button = Button( root,text="Quit",command=root.destroy,font=("Poppins", 10, "bold"),width=22,bg="#D94B4B",fg="#ffffff",activebackground="#B93838", activeforeground="#ffffff",relief="flat",bd=0,pady=7
)
quit_button.pack(pady=5)

#runs the app
root.mainloop()
#thanks for checking out the code!!
