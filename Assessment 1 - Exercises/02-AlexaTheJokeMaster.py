
from tkinter import *
import random
from PIL import Image, ImageTk

#main setup
root = Tk()
root.title("Alexa, The Joke Master")
root.geometry("500x700")
root.resizable(False, False)  #size is not resizable for this window, as i believe it was not needed
root.configure(bg="#F0EFF5") #main bg color
root.iconbitmap('alexa.ico') #icon for alexa

#loads both alexa images
alexa_image = Image.open("alexa.png")
alexa_image = alexa_image.resize((185, 185), Image.Resampling.LANCZOS)
alexa_photo = ImageTk.PhotoImage(alexa_image)

alexa_off_image = Image.open("alexa_off.png")
alexa_off_image = alexa_off_image.resize((185, 185), Image.Resampling.LANCZOS)
alexa_off_photo = ImageTk.PhotoImage(alexa_off_image)


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

    #turns alexa's light on
    alexa_label.config(image=alexa_photo)

    tell_joke_button.pack_forget()
    quit_button.pack_forget()

    punchline_button.pack(pady=5)
    next_joke_button.pack(pady=5)
    quit_button.pack(pady=5)

#function to display the punchline
def show_punchline():
    punchline_label.config(text=current_punchline)

#function to get the next joke
def next_joke():
    tell_joke()


#main heading
title_label = Label(root,
    text="Alexa, The Joke Master",font=("Poppins", 24, "bold"),bg="#F0EFF5",fg="#252238"
)
title_label.pack(pady=(20, 2))

subtitle_label = Label(root,text="She's the funniest comedian!",font=("Poppins", 12),bg="#F0EFF5",fg="#7054C8"
)
subtitle_label.pack(pady=(0, 15))


#joke display frame
joke_frame = Frame(root,bg="#DCD9E8",padx=20,pady=14
)
joke_frame.pack(padx=35, fill="x")

#joke setup label
setup_label = Label(joke_frame,text="Click the button below to hear a joke!",font=("Poppins", 13, "bold"),bg="#DCD9E8",fg="#252238",wraplength=390,justify="center"
)
setup_label.pack(pady=(4, 6))

#punchline label
punchline_label = Label(joke_frame,text="",font=("Poppins", 12),bg="#DCD9E8",fg="#7054C8",wraplength=390,justify="center"
)
punchline_label.pack(pady=(0, 4))


#displays an image of alexa below the joke frame
alexa_label = Label(root, image=alexa_off_photo, bg="#F0EFF5")
alexa_label.pack(pady=10)


#tell a joke button
tell_joke_button = Button(root,text="Alexa tell me a joke!",command=tell_joke,font=("Poppins", 12, "bold"),width=24,bg="#7054C8",fg="#ffffff",activebackground="#A18AE8",activeforeground="#ffffff",relief="flat",bd=0,pady=8
)
tell_joke_button.pack(pady=5)

#show punchline button
punchline_button = Button(root, text="Punchline!",command=show_punchline,font=("Poppins", 12, "bold"),width=24, bg="#A18AE8",fg="#252238",activebackground="#DCD9E8",activeforeground="#252238",relief="flat", bd=0,pady=8
)

#next joke button
next_joke_button = Button(root,text="HAHA! next please!",command=next_joke,font=("Poppins", 12, "bold"),width=24,bg="#DCD9E8",fg="#252238",activebackground="#A18AE8",activeforeground="#252238",relief="flat", bd=0, pady=8
)

#quit button
quit_button = Button(root,text="Quit",command=root.destroy,font=("Poppins", 12, "bold"),width=24,bg="#252238",fg="#ffffff",activebackground="#7054C8",activeforeground="#ffffff",relief="flat",bd=0,pady=8
)
quit_button.pack(pady=5)

#runs the app
root.mainloop()
#thanks for checking out the code!!
