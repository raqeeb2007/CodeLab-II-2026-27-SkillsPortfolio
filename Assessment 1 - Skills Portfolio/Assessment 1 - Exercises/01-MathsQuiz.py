
from tkinter import *
import random

#main setup
root = Tk()
root.title("Maths Quiz")
root.geometry("480x550")
root.resizable(True, True) #size is resizable now
root.configure(bg="#EAF2F8") #main bg color
root.iconbitmap('abacus.ico') #icon for the math quiz

#important variables for the quiz
difficulty = ""
score = 0
question_number = 0
attempts = 0
correct_answer = 0

#clears all widgets from window
def clearWindow():
    for widget in root.winfo_children():
        widget.destroy()

#shows the main menu alongside the difficulty buttons
def displayMenu():
    clearWindow()

    main_frame = Frame(root, bg="#DCEAF4")
    main_frame.pack(fill="both", expand=True, padx=35, pady=25)

    title = Label(#main title for the quiz
        main_frame,
        text="Math Quiz For Codelab II", font=("Poppins", 20, "bold"),bg="#DCEAF4", fg="#18334D"
    )
    title.pack(pady=(15, 5)) #i chose poppins as my font of choice by dowbloading it through google fonts

    subtitle = Label( #subtitle below the title
        main_frame, text="Can you pass this math quiz?",font=("Poppins", 9), bg="#DCEAF4", fg="#52718A"
    )
    subtitle.pack(pady=(0, 25))

    instruction = Label(
        main_frame,
        text="Select your difficulty level", font=("Poppins", 12, "normal"),bg="#DCEAF4",fg="#24476A"
    ) #frame for difficulty choices
    instruction.pack(pady=10)

    def selectDifficulty(level): #the function that sets the difficulty chosen
        global difficulty
        difficulty = level
        startQuiz()

    button_options = {
        "font": ("Poppins", 10, "normal"), "width": 20,"bg": "#24476A","fg": "#ffffff","activebackground": "#527A9E","activeforeground": "#ffffff","relief": "flat","bd": 0,"pady": 7
    }

    easyButton = Button( main_frame,text="Easy",command=lambda: selectDifficulty("Easy"),**button_options
    )
    easyButton.pack(pady=5)

    mediumButton = Button( main_frame,text="Medium",command=lambda: selectDifficulty("Medium"),**button_options
    )
    mediumButton.pack(pady=5)

    HardButton = Button(main_frame,text="Hard",command=lambda: selectDifficulty("Hard"),**button_options
    )
    HardButton.pack(pady=5) 

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

    main_frame = Frame(root, bg="#DCEAF4")
    main_frame.pack(fill="both", expand=True, padx=30, pady=20)

    progress_label = Label(
        main_frame,text="QUESTION " + str(question_number + 1) + " OF 10",font=("Poppins", 10, "bold"),bg="#DCEAF4",fg="#52718A" 
        #simple progress check
    )
    progress_label.pack(pady=5)

    score_label = Label(main_frame,text="Score: " + str(score),font=("Poppins", 10),bg="#DCEAF4",fg="#24476A" 
        #keeps track of the score 
    )
    score_label.pack(pady=5)

    question_frame = Frame( main_frame,bg="#EAF2F8",padx=20,pady=20 
    )#simple frame for the question
    question_frame.pack(fill="x", pady=15)

    question_label = Label(question_frame,text=str(num1) + " " + operation + " " + str(num2) + " = ?",font=("Poppins", 25, "bold"),bg="#EAF2F8",fg="#18334D"
    )
    question_label.pack(pady=5)

    answer_entry = Entry( main_frame,font=("Poppins", 13),width=15,justify="center",bg="#ffffff",fg="#24476A",relief="flat",bd=0
    )#The space for the user to give an answer
    answer_entry.pack(pady=10, ipady=7)
    answer_entry.focus()

    feedback_label = Label(  main_frame,text="Enter your answer below",font=("Poppins", 9),bg="#DCEAF4",fg="#52718A"
    )
    feedback_label.pack(pady=5)

    submit_button = Button( main_frame,text="SUBMIT ANSWER",font=("Poppins", 10, "bold"),width=20,bg="#24476A",fg="#ffffff",activebackground="#527A9E",activeforeground="#ffffff",relief="flat",bd=0,pady=8,
        command=lambda: isCorrect(answer_entry.get())
    )
    submit_button.pack(pady=10)

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
                text="Right on! +10 points.", fg="#1CDA42"#user gets 10 points for getting it right on the first try
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

    main_frame = Frame(root, bg="#DCEAF4")
    main_frame.pack(fill="both", expand=True, padx=30, pady=30)

    title = Label( main_frame,text="QUIZ FINISHED!", font=("Poppins", 20, "bold"),bg="#DCEAF4",fg="#18334D"
    )
    title.pack(pady=(20, 15))

    results_frame = Frame(main_frame,bg="#EAF2F8",padx=25,pady=20
    )
    results_frame.pack(fill="x", pady=10)

    result_label = Label(results_frame,text="Your final results!",font=("Poppins", 11),bg="#EAF2F8",fg="#52718A"
    )
    result_label.pack(pady=5)

    result_label = Label(
        results_frame,text=str(score) + " / 100",font=("Poppins", 26, "bold"),bg="#EAF2F8",fg="#18334D"
    )
    result_label.pack(pady=5)

    #uses the the total score the user has achieved to come up with a final grade
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
        results_frame,text="Grade: " + grade, font=("Poppins", 15, "bold"),bg="#EAF2F8",fg="#52718A"
    )
    grade_label.pack(pady=5)

    button_options = {
        "font": ("Poppins", 10, "bold"),"width": 20,"bg": "#24476A","fg": "#ffffff","activebackground": "#527A9E","activeforeground": "#ffffff", "relief": "flat", "bd": 0,"pady": 8
    }
#buttons for replays and retrys
    retry_button = Button(main_frame,text="RETRY!",command=displayMenu,
        **button_options
    )
    retry_button.pack(pady=(15, 5))

    quit_button = Button(main_frame,text="QUIT.",command=root.destroy,
        **button_options
    )
    quit_button.pack(pady=5)

#show initial menu
displayMenu()

#runs the app
root.mainloop()
#thanks for reading the code!
