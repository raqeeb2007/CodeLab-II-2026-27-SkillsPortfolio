
from tkinter import *
import random
from PIL import Image, ImageTk

#main setup
root = Tk()
root.title("Maths Quiz")
root.geometry("730x600")
root.resizable(False, False) #removed resize as the background image would start to not fit anymore, also removed the background color as it was not need anymore
root.iconbitmap('abacus.ico') #icon for the math quiz

#loads the background image
bg_image = Image.open("maths_background.png")
bg_image = bg_image.resize((740, 635))
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#important variables for the quiz
difficulty = ""
score = 0
question_number = 0
attempts = 0
correct_answer = 0

#clears all widgets from window
def clearWindow():
    for widget in root.winfo_children():
        if widget != background_label:
            widget.destroy()

#shows the main menu alongside the difficulty buttons
def displayMenu():
    clearWindow()

    main_frame = Frame(root, bg="#DCEAF4", padx=35, pady=25)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    title = Label(#main title for the quiz
        main_frame,
        text="Math Quiz For Codelab II", font=("Poppins", 24, "bold"),bg="#DCEAF4", fg="#18334D"
    )
    title.pack(pady=(15, 8)) #i chose poppins as my font of choice by downloading it through google fonts

    subtitle = Label( #subtitle below the title
        main_frame, text="Can you pass this math quiz?",font=("Poppins", 11), bg="#DCEAF4", fg="#52718A"
    )
    subtitle.pack(pady=(0, 25))

    instruction = Label(
        main_frame,
        text="Select your difficulty level", font=("Poppins", 14, "normal"),bg="#DCEAF4",fg="#24476A"
    ) #frame for difficulty choices
    instruction.pack(pady=10)

    def selectDifficulty(level): #the function that sets the difficulty chosen
        global difficulty
        difficulty = level
        startQuiz()

        #different colours for each difficulty level
    easyButton = Button(main_frame,text="Easy",command=lambda: selectDifficulty("Easy"),font=("Poppins", 12, "normal"),width=22,bg="#2E8B57", fg="#ffffff",activebackground="#246B45",activeforeground="#ffffff",relief="flat",bd=0,pady=10
    )
    easyButton.pack(pady=7)

    mediumButton = Button(main_frame,text="Medium",command=lambda: selectDifficulty("Medium"),font=("Poppins", 12, "normal"),width=22,bg="#D99A26",fg="#ffffff",activebackground="#B7801E",activeforeground="#ffffff",relief="flat",bd=0,pady=10
    )
    mediumButton.pack(pady=7)

    HardButton = Button(main_frame,text="Hard",command=lambda: selectDifficulty("Hard"),font=("Poppins", 12, "normal"),width=22,bg="#C94C4C",fg="#ffffff",activebackground="#A83B3B",activeforeground="#ffffff",relief="flat",bd=0,pady=10
    )
    HardButton.pack(pady=7)

#generates a random number based on the button chosen (the difficulty)
def randomInt(level):
    if level == "Easy":
        return random.randint(1, 9)

    elif level == "Medium":
        return random.randint(10, 99)

    elif level == "Hard":
        return random.randint(1000, 9999)

#randomly decides between addition and subtraction
def decideOperation():
    return random.choice(["+", "-"])

#starts the quiz
def startQuiz():
    global score, question_number, attempts

    score = 0
    question_number = 0
    attempts = 0

    displayProblem()

#shows the questions
def displayProblem():
    global correct_answer, attempts
    global question_label, answer_entry, feedback_label
    global submit_button

    clearWindow()
    attempts = 0

    num1 = randomInt(difficulty)
    num2 = randomInt(difficulty)
    operation = decideOperation()

    #makes sure that the subtraction questions cant give negative answers (to simplify the quiz)
    if operation == "-" and num1 < num2:
        num1, num2 = num2, num1

    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    main_frame = Frame(root, bg="#DCEAF4", padx=35, pady=25)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    progress_label = Label(
        main_frame,text="QUESTION " + str(question_number + 1) + " OF 10",font=("Poppins", 12, "bold"),bg="#DCEAF4",fg="#102739"
        #simple progress check
    )
    progress_label.pack(pady=7)

    score_label = Label(main_frame,text="Score: " + str(score),font=("Poppins", 12),bg="#DCEAF4",fg="#24476A"
        #keeps track of the score
    )
    score_label.pack(pady=7)

    question_frame = Frame( main_frame,bg="#EAF2F8",padx=30,pady=25
    )#simple frame for the question
    question_frame.pack(fill="x", pady=20)

    question_label = Label(question_frame,text=str(num1) + " " + operation + " " + str(num2) + " = ?",font=("Poppins", 30, "bold"),bg="#EAF2F8",fg="#18334D"
    )
    question_label.pack(pady=8)

    answer_entry = Entry( main_frame,font=("Poppins", 16),width=17,justify="center",bg="#ffffff",fg="#24476A",relief="flat",bd=0
    )#The space for the user to give an answer
    answer_entry.pack(pady=15, ipady=9)
    answer_entry.focus()

    feedback_label = Label(  main_frame,text="Enter your answer below",font=("Poppins", 11),bg="#DCEAF4",fg="#52718A"
    )
    feedback_label.pack(pady=7)

    submit_button = Button( main_frame,text="SUBMIT ANSWER",font=("Poppins", 12, "bold"),width=22,bg="#24476A",fg="#ffffff",activebackground="#527A9E",activeforeground="#ffffff",relief="flat",bd=0,pady=10,
        command=lambda: isCorrect(answer_entry.get())
    )
    submit_button.pack(pady=12)

#checking the user's answer
def isCorrect(answer):
    global score, question_number, attempts

    try:
        user_answer = int(answer)
    except ValueError:
        feedback_label.config(
            text="Please enter a valid number.",fg="#a33d3d"
        )
        return

    if user_answer == correct_answer:

        if attempts == 0:
            score += 10
            feedback_label.config(
                text="Right on! +10 points.", fg="#1CDA42" #user gets 10 points for getting it right on the first try
            )
        else:
            score += 5
            feedback_label.config(
                text="Not bad! +5 points.", fg="#45E89C" #while they get 5 on the second try
            )

        submit_button.config(state="disabled")
        question_number += 1

        if question_number == 10:
            root.after(800, displayResults)
        else:
            root.after(800, displayProblem)

    else:

        if attempts == 0:
            attempts += 1

            feedback_label.config(
                text="Incorrect! Try again.", fg="#a33d3d" #even if the user gets an answer wrong, they get a 2nd try
            )

            answer_entry.delete(0, END)

        else:
            feedback_label.config(
                text="Incorrect again. No more attempts.", fg="#a33d3d" #this was the user's last try
            )

            submit_button.config(state="disabled")
            question_number += 1

            if question_number == 10:
                root.after(800, displayResults)
            else:
                root.after(800, displayProblem)

#shows final scores
def displayResults():
    clearWindow()

    main_frame = Frame(root, bg="#DCEAF4", padx=35, pady=25)
    main_frame.place(relx=0.5, rely=0.5, anchor="center")

    title = Label( main_frame,text="QUIZ FINISHED!", font=("Poppins", 24, "bold"),bg="#DCEAF4",fg="#18334D"
    )
    title.pack(pady=(20, 15))

    results_frame = Frame(main_frame,bg="#EAF2F8",padx=35,pady=25
    )
    results_frame.pack(fill="x", pady=15)

    result_label = Label(results_frame,text="Your final results!",font=("Poppins", 13),bg="#EAF2F8",fg="#52718A"
    )
    result_label.pack(pady=7)

    result_label = Label(
        results_frame,text=str(score) + " / 100",font=("Poppins", 32, "bold"),bg="#EAF2F8",fg="#18334D"
    )
    result_label.pack(pady=7)

    #uses the total score the user has achieved to come up with a final grade
    if score >= 90:
        grade = "A*"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    elif score >= 40:
        grade = "E"
    else:
        grade = "F"

    grade_label = Label(
        results_frame,text="Grade: " + grade, font=("Poppins", 18, "bold"),bg="#EAF2F8",fg="#52718A"
    )
    grade_label.pack(pady=7)

    retry_button = Button(results_frame,text="RETRY!",command=displayMenu,font=("Poppins", 12, "bold"),width=22,bg="#24476A",fg="#FFFFFF",activebackground="#527A9E",activeforeground="#FFFFFF",relief="flat",bd=0,pady=10
    )
    retry_button.pack(pady=5)

    quit_button = Button(results_frame,text="QUIT.",command=root.destroy,font=("Poppins", 12, "bold"),width=22,bg="#B83232",fg="#FFFFFF",activebackground="#922626",activeforeground="#FFFFFF", relief="flat",bd=0,pady=10
    )
    quit_button.pack(pady=5)
#show initial menu
displayMenu()

#runs the app
root.mainloop()

#thanks for reading the code!
