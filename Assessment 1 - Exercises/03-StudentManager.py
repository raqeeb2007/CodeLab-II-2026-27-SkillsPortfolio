
from tkinter import *
from tkinter import messagebox, simpledialog

#main setup
root = Tk()
root.title("Student Manager") 
root.geometry("700x600")
root.resizable(True, True) #size resizeble for this app as i felt it was appropriate
root.configure(bg="#F5EFE6")
root.iconbitmap('student.ico')


#important variables
students = []


#load student records from file
def load_students():
    try:
        with open("Assessment 1 - Skills Portfolio/A1 - Resources/studentMarks.txt", "r") as file:
            number_of_students = int(file.readline())

            for line in file:
                data = line.strip().split(",")

                if len(data) == 6:
                    student = {
                        "code": data[0],
                        "name": data[1],
                        "mark1": int(data[2]),
                        "mark2": int(data[3]),
                        "mark3": int(data[4]),
                        "exam": int(data[5])
                    }

                    students.append(student)

    except FileNotFoundError:
        messagebox.showerror("Error", "studentMarks.txt could not be found.")

    except ValueError:
        messagebox.showerror("Error", "There is invalid data in the student file.")


#calculate student results
def calculate_results(student):
    coursework_total = (
        student["mark1"] +
        student["mark2"] +
        student["mark3"]
    )

    total_marks = coursework_total + student["exam"]
    percentage = (total_marks / 160) * 100

    if percentage >= 70:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "F"

    return coursework_total, total_marks, percentage, grade


#display an individual student's details
def display_student(student):
    coursework, total, percentage, grade = calculate_results(student)

    output.insert(END, f"Name: {student['name']}\n")
    output.insert(END, f"Student Code: {student['code']}\n")
    output.insert(END, f"Coursework Total: {coursework}/60\n")
    output.insert(END, f"Exam Mark: {student['exam']}/100\n")
    output.insert(END, f"Overall Percentage: {percentage:.2f}%\n")
    output.insert(END, f"Grade: {grade}\n")
    output.insert(END, "-" * 45 + "\n\n")


#removes the output
def clear_output():
    output.delete("1.0", END)


#lets you view all students
def view_all():
    clear_output()

    if len(students) == 0:
        output.insert(END, "No student records available.")
        return

    output.insert(END, "ALL STUDENT RECORDS\n")
    output.insert(END, "=" * 45 + "\n\n")

    total_class_percentage = 0

    for student in students:
        display_student(student)

        coursework, total, percentage, grade = calculate_results(student)
        total_class_percentage += percentage

    class_average = total_class_percentage / len(students)

    output.insert(END, "\nCLASS SUMMARY\n")
    output.insert(END, "=" * 45 + "\n")
    output.insert(END, f"Number of Students: {len(students)}\n")
    output.insert(END, f"Class Average: {class_average:.2f}%\n")


#while this lets you view a single student
def view_individual():
    search_window = Toplevel(root)
    search_window.title("Find Student")
    search_window.geometry("300x180")
    search_window.resizable(False, False)
    search_window.configure(bg="#F5EFE6")
    search_window.iconbitmap("search.ico")

    Label(search_window, text="Enter student name or code:",
          font=("Poppins", 10),
          bg="#F5EFE6", fg="#44232D").pack(pady=15)

    search_entry = Entry(search_window, width=25,
                         font=("Poppins", 10),
                         relief="solid", bd=1)
    search_entry.pack(pady=5)

    def search_student():
        search = search_entry.get().strip().lower()

        for student in students:
            if search == student["name"].lower() or search == student["code"]:
                search_window.destroy()
                clear_output()
                display_student(student)
                return

        messagebox.showinfo("Not Found", "Student not found.")

    Button(search_window, text="Search", command=search_student,font=("Poppins", 10, "bold"), width=18,bg="#702D3C",fg="#FFFFFF",activebackground="#8F4657",activeforeground="#FFFFFF",relief="flat",bd=0,pady=7
    ).pack(pady=15)


#lets you look for the student with the highest grade
def highest_student():
    if len(students) == 0:
        messagebox.showinfo("Student Manager", "No student records available.")
        return

    highest = students[0]

    for student in students:
        if calculate_results(student)[1] > calculate_results(highest)[1]:
            highest = student

    clear_output()
    output.insert(END, "HIGHEST SCORING STUDENT\n")
    output.insert(END, "=" * 45 + "\n\n")
    display_student(highest)


#and this lets you look for the student with the lowest grade
def lowest_student():
    if len(students) == 0:
        messagebox.showinfo("Student Manager", "No student records available.")
        return

    lowest = students[0]

    for student in students:
        if calculate_results(student)[1] < calculate_results(lowest)[1]:
            lowest = student

    clear_output()
    output.insert(END, "LOWEST SCORING STUDENT\n")
    output.insert(END, "=" * 45 + "\n\n")
    display_student(lowest)


#lets you sort the list from ascending or descending order 
def sort_students():
    sort_window = Toplevel(root)
    sort_window.title("Sort Students")
    sort_window.geometry("250x250")
    sort_window.resizable(False, False)
    sort_window.configure(bg="#F5EFE6")
    sort_window.iconbitmap("sort.ico")

    Label(sort_window,text="Choose Sort Order",font=("Poppins", 13, "bold"),bg="#F5EFE6",fg="#44232D"
    ).pack(pady=20)

    def ascending():
        students.sort(key=lambda student: calculate_results(student)[1])
        sort_window.destroy()
        view_all()

    def descending():
        students.sort(key=lambda student: calculate_results(student)[1],reverse=True
        )
        sort_window.destroy()
        view_all()

    Button(sort_window,text="Ascending",command=ascending,font=("Poppins", 10),bg="#702D3C",fg="#FFFFFF",activebackground="#8F4657",activeforeground="#FFFFFF",relief="flat",width=18,pady=7
    ).pack(pady=8)

    Button(sort_window,text="Descending", command=descending,font=("Poppins", 10),bg="#702D3C",fg="#FFFFFF",activebackground="#8F4657", activeforeground="#FFFFFF",relief="flat",width=18,pady=7
    ).pack(pady=8)


#main heading
heading = Label(root,text="STUDENT MANAGER",font=("Poppins", 20, "bold"),bg="#F5EFE6",fg="#44232D"
)
heading.pack(pady=20)


#main layout
main_frame = Frame(root, bg="#F5EFE6")
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)


#menu buttons (placed on the left)
menu_frame = Frame(main_frame, bg="#F5EFE6")
menu_frame.pack(side=LEFT, fill=Y, padx=(0, 20))


Label(menu_frame,text="MENU",font=("Poppins", 13, "bold"),bg="#F5EFE6",fg="#44232D"
).pack(pady=(0, 15))


#button styling
button_options = {"font": ("Poppins", 10, "normal"),"width": 20,"bg": "#702D3C","fg": "#FFFFFF","activebackground": "#8F4657","activeforeground": "#FFFFFF","relief": "flat","bd": 0,"pady": 7
}


Button(menu_frame,text="1. View All Students",command=view_all,
    **button_options
).pack(pady=6)

Button(menu_frame,text="2. Find Individual",command=view_individual,
    **button_options
).pack(pady=6)

Button(menu_frame,text="3. Highest Grade",command=highest_student,
    **button_options
).pack(pady=6)

Button(menu_frame,text="4. Lowest Grade",command=lowest_student,
    **button_options
).pack(pady=6)

Button(menu_frame,text="5. Sort Students",command=sort_students,
    **button_options
).pack(pady=6)


#quit button
quit_options = button_options.copy()
quit_options["bg"] = "#B65F6A"
quit_options["activebackground"] = "#CE7B85"

Button( menu_frame,text="Quit",command=root.destroy,
    **quit_options
).pack(pady=(25, 6))


#results are on the right
results_frame = Frame(main_frame, bg="#F5EFE6")
results_frame.pack(side=RIGHT, fill=BOTH, expand=True)


Label(results_frame,text="STUDENT RECORDS", font=("Poppins", 13, "bold"),bg="#F5EFE6",fg="#44232D"
).pack(pady=(0, 10))


#text display and scrollbar
output_frame = Frame(results_frame, bg="#F5EFE6")
output_frame.pack(fill=BOTH, expand=True)

scrollbar = Scrollbar(output_frame)
scrollbar.pack(side=RIGHT, fill=Y)

output = Text(output_frame,font=("Poppins", 10),bg="#FFFFFF",fg="#44232D",relief="flat",wrap=WORD,yscrollcommand=scrollbar.set,padx=10,pady=10
)
output.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=output.yview)


#load records 
load_students()
#runs the final app
root.mainloop()
#thanks for checking out the code!
