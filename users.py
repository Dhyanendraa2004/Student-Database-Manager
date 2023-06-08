#oops project by dhyanendra_tripathi
import customtkinter,json,os
from PIL import ImageTk,Image
from utils import *
import matplotlib, numpy
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
#filedialog to create file selection windows
from tkinter import filedialog

os.chdir("assets/")
with open("users.json","r+") as file:
    data = json.load(file)
    
customtkinter.set_default_color_theme("blue")
class Users:
    def check_login(self,frame):
        username = frame.uentry.get().strip()
        password = frame.pentry.get().strip()
        if username not in data["users"].keys():
            print(f"No user named {username} found")
        else:
            real_password = data["users"][username]["password"]
            if password == real_password:
                if data["users"][username]["isadmin"] == True:
                    frame.destroy()
                    user=Admin(self.window,username)
                    user.manage_user()
                else:
                    frame.destroy()
                    self.username = username
                    self.home_page(i=0)
            else:
                print("Incorrect login please check password or username")

    def login_page(self):
        self.window = customtkinter.CTk()
        frame = customtkinter.CTkToplevel(self.window)
        frame.geometry("600x440")
        frame.title("Login")
        bg_image = ImageTk.PhotoImage(Image.open("pattern.png"))
        bg = customtkinter.CTkLabel(master=frame,image=bg_image,text="")
        bg.pack()
        frame.l_frame = customtkinter.CTkFrame(master=bg,height=360,width=360,corner_radius=15)
        frame.l_frame.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
        frame.label_1 = customtkinter.CTkLabel(master=frame.l_frame,text="Student Database Manager \nOOPs Project",font=("Century Gothic",20))
        frame.label_1.place(x=60,y=10)
        frame.uentry = customtkinter.CTkEntry(master=frame.l_frame,placeholder_text="Username",width=220)
        frame.uentry.place(relx=0.2,y=125)
        frame.pentry = customtkinter.CTkEntry(master=frame.l_frame,placeholder_text="Password",width=220)
        frame.pentry.place(relx=0.2,y=180)
        frame.l_button = customtkinter.CTkButton(master=frame.l_frame,width=220,text="Login",corner_radius=6,command=lambda : self.check_login(frame))
        frame.l_button.place(relx=0.2,y=250)
        frame.mainloop()

    def print(self):
        ...

    def home_page(self,i=0):
        #Define window of the page
        self.window.title("Student DataBase- By DoTes")
        self.window.iconbitmap("deshpremikiryu-modified.ico")
        self.text_font = customtkinter.CTkFont("Proxima Nova Rg",18)
        self.text_font_bold = customtkinter.CTkFont("Proxima Nova Rg",20,"bold")
        self.font = customtkinter.CTkFont("Proxima Nova Rg",12,'bold')
        self.window.geometry("900x600")

        #Define grid inside the window
        self.window.grid_columnconfigure(1,weight=1)
        self.window.grid_rowconfigure(0,weight=1)

        #Add left frame inside the row 0 col 0 cell
        self.l_frame = customtkinter.CTkFrame(master=self.window)
        self.l_frame.grid(row=0,column=0,rowspan=4,padx=20,pady=20,sticky="nsew")

        #Added MANAGE label
        self.window.manage_ = customtkinter.CTkLabel(master=self.l_frame,text="MANAGE",font=self.font)
        self.window.manage_.place(y=30,relx=0.1)

        #Added ATTENDANCE button
        self.window.but_attend = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Attendance",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("calendar-solid.png")),command=self.attendace)
        self.window.but_attend.place(y=60)

        #Added Projects button
        self.window.but_attend = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Projects",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("calendar-solid.png")),command=self.attendace)
        self.window.but_attend.place(y=330)

        #Added Student button 
        self.window.but_emp = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Change Password",corner_radius=0,image=customtkinter.CTkImage(Image.open("a.png"),size=(20,20)),fg_color="#333333",hover_color="#2e2e2e",
                              command= self.change_password
                                )
        self.window.but_emp.place(y=100)

        #Added DEDUCTION button
        self.window.but_deduction = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Grades",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("documents-solid.png")),command=self.gradess)
        self.window.but_deduction.place(y=140)

        #Added Printables label
        self.window.printables = customtkinter.CTkLabel(master=self.l_frame,text="PRINTABLES",font=self.font)
        self.window.printables.place(y=185,relx=0.1)

        #Added sheet button
        self.window.but_sheet = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Attendence Sheet   ",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",image=customtkinter.CTkImage(Image.open("coins-solid.png")),command=self.print)
        self.window.but_sheet.place(y=215)

        #Added Home page button
        if i==0:
            self.window.home_page = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Home Page",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=self.home_page)
            self.window.home_page.place(y=295)
        else:
            self.window.home_page = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Home Page",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=lambda : self.home_page(1))
            self.window.home_page.place(y=295)

        #Added right frame 
        self.r_frame = customtkinter.CTkFrame(master=self.window)
        self.r_frame.grid(row=0,column=1,rowspan=4,padx=20,pady=20,sticky="nsew")

        if i==1:
            manage = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Other Students",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=self.manage_user)
            manage.place(y=400)

        #Added dashboard label inside right frame
        self.dashboard = customtkinter.CTkLabel(master=self.r_frame,text="Dashboard")
        self.dashboard.configure(padx=20,font=self.text_font_bold)

        #Grid inside right frame with 3 coloumns and 3 rows
        self.r_frame.grid_columnconfigure((0,1,2,3),weight=1)
        self.r_frame.grid_rowconfigure((1,2,3),weight=1)

        #Place dashboard label to the (0,0) of right frame
        self.dashboard.grid(row=0,column=0,padx=7.5,pady=20,sticky="nw")

        #Add total_working_employee frame
        total_student = customtkinter.CTkFrame(master=self.r_frame,fg_color="#6c7f91",corner_radius=0)
        total_student.grid(row=1,column=0,sticky="new",padx=20)

        #Details
        total_student_ = customtkinter.CTkLabel(master=total_student,text="Total Students",font=self.text_font)
        total_student_.place(relx=0.1,rely=0.25)
        users = len(data["users"])
        total_student_label = customtkinter.CTkLabel(master=total_student,text=f"{users}",font=self.text_font_bold)
        total_student_label.place(relx=0.1,rely=0.1)

        #Add attendance percentage frame 
        percentage = customtkinter.CTkFrame(master=self.r_frame,fg_color="#019258",corner_radius=0)
        percentage.grid(row=1,column=1,sticky="new")

        #Details
        percentage_label = customtkinter.CTkLabel(master=percentage,text=f"{total_attendace(data,self.username)}",font=self.text_font_bold)
        percentage_label.place(relx=0.1,rely=0.1)
        percentage_label_ = customtkinter.CTkLabel(master=percentage,text="Attendance %",font=self.text_font)
        percentage_label_.place(relx=0.1,rely=0.25)

        #Add current time frame
        time = customtkinter.CTkFrame(master=self.r_frame,fg_color="#fd9c0a",corner_radius=0)
        time.grid(row=1,column=2,sticky="new",padx=20)

        #Details
        time_label = customtkinter.CTkLabel(master=time,text="",font=self.text_font_bold)
        time_label.place(relx=0.1,rely=0.1)
        update_time(time_label)
        current_time_label = customtkinter.CTkLabel(master=time,text="Current Time",font=self.text_font)
        current_time_label.place(relx=0.1,rely=0.25)

        basic = int(data["users"][self.username]["basic"])
        #Late Frame Right most
        cgpa_f = customtkinter.CTkFrame(master=self.r_frame,fg_color="#e85832",corner_radius=0)
        cgpa_f.grid(row=1,column=3,sticky="new")

        net_pay=9.29
        cgpa = customtkinter.CTkLabel(master=cgpa_f,text=f"{net_pay}",font=self.text_font_bold)
        cgpa.place(relx=0.1,rely=0.1)
        cgpa_ = customtkinter.CTkLabel(master=cgpa_f,text="NET_CGPA",font=self.text_font)
        cgpa_.place(relx=0.1,rely=0.25)

        details = customtkinter.CTkFrame(master=self.r_frame)
        details.grid(row=2,column=0,sticky="nsew",rowspan=4,columnspan=4)

        name_account = customtkinter.CTkLabel(details,width=2000,bg_color="#474545",text="Name: {}     Roll Number:{}".format(data["users"][self.username]["name"],data["users"][self.username]["acc"]),anchor="w",font=self.text_font)
        name_account.place(x=0,y=40)
        name_account.configure(padx=40)
        
        if i==0:
            self.window.mainloop()





    def gradess(self):
        ...


    def attendace(self):
        self.r_frame.destroy()
        #Create a new window with the same name
        
        self.r_frame = customtkinter.CTkFrame(master=self.window)
        self.r_frame.grid(row=0,column=1,rowspan=4,padx=20,pady=20,sticky="nsew")

        self.r_frame.grid_columnconfigure((0,1,2,3),weight=1)
        self.r_frame.grid_rowconfigure(1,weight=1)

        attendance = customtkinter.CTkLabel(master=self.r_frame,text="Attendance")
        attendance.configure(padx=20,font=self.text_font_bold)
        attendance.grid(row=0,column=0,padx=7.5,pady=20,sticky="nw")

        attendance_graph = customtkinter.CTkFrame(master=self.r_frame)
        
        attendance_graph.grid(row=1,column=0,padx=7.5,pady=20,sticky="nsew",columnspan=4) 

        f = Figure(figsize=(10,20), dpi=100,facecolor="#2a2b2a")
        ax = f.add_subplot(111)
        ax.set_facecolor("lightblue")
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.xaxis.label.set_color('black')
        ax.tick_params(axis='x', colors='white')
        ax.yaxis.label.set_color('white')
        ax.tick_params(axis='y', colors='white')
        data_ = tuple(data["users"][self.username]["attendance"])
        ind = numpy.arange(len(data_))  # the x locations for the groups
        width = .75
        ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11],["LAMA", "Optimisation tech", 'OOPs', "IoT", "Calculus", 'C Programming', "Python", "Probability", "DLD", "Singal and system", 'CDS' , "Human Values"])
        ax.set_xticklabels(["LAMA", "Optimisation tech", 'OOPs', "IoT", "Calculus", 'C Programming', "Python", "Probability", "DLD", "Singal and system", 'CDS' , "Human Values"],rotation=30)
        rects1 = ax.bar(ind, data_, width)

        canvas = FigureCanvasTkAgg(f, master=attendance_graph)
        canvas.draw()
        
        canvas.get_tk_widget().pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1)

    def change_password(self):
        #UI Element Top level to create additional windows
        self.top_level = customtkinter.CTkToplevel()
        self.top_level.title("Change Password")
        image = ImageTk.PhotoImage(Image.open("alo.png"))
        bg = customtkinter.CTkLabel(master=self.top_level,image=image,text="")
        bg.pack()
        self.top_level.geometry("600x440") 

        self.top_l_frame = customtkinter.CTkFrame(master=self.top_level,height=360,width=360,corner_radius=15)
        self.top_l_frame .place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)

        label_1 = customtkinter.CTkLabel(master=self.top_l_frame ,text="Change Password",font=("Century Gothic",20))
        label_1.place(x=80,y=10)

        current_password_label = customtkinter.CTkLabel(master=self.top_l_frame ,text="Current Password")
        current_password_label.place(relx=0.2,y=70)

        uentry = customtkinter.CTkEntry(master=self.top_l_frame ,placeholder_text="",width=220)
        uentry.place(relx=0.2,y=105)

        new_password_label = customtkinter.CTkLabel(master=self.top_l_frame ,text="New Password")
        new_password_label.place(relx=0.2,y=145)

        new_password = customtkinter.CTkEntry(master=self.top_l_frame ,placeholder_text="",width=220)
        new_password.place(relx=0.2,y=180)   
        
        confirm_password_label = customtkinter.CTkLabel(master=self.top_l_frame ,text="Confirm Password")
        confirm_password_label.place(relx=0.2,y=220)

        confirm_password = customtkinter.CTkEntry(master=self.top_l_frame ,placeholder_text="",width=220)
        confirm_password.place(relx=0.2,y=255) 

        l_button = customtkinter.CTkButton(master=self.top_l_frame ,width=220,text="Change Password",corner_radius=6,command=lambda : self.check_entered_pass(uentry,new_password,confirm_password))
        l_button.place(relx=0.2,y=300)
        
        
        #Check if current password is right
    def check_entered_pass(self,uentry,uentry2,uentry3):
        pass1 = uentry2.get()
        pass2 = uentry3.get()
        if (data["users"][self.username]["password"] == uentry.get().strip())and (pass1==pass2):
            self.top_l_frame.destroy()
            self.top_l_frame2 = customtkinter.CTkFrame(master=self.top_level,height=360,width=360,corner_radius=15)
            self.top_l_frame2.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
            valid_pass = customtkinter.CTkLabel(master=self.top_l_frame2,text="Password changed",text_color="Green",font=("Century Gothic",20))
            password_changed_image = customtkinter.CTkImage(Image.open("checkmark.png"),size=(60,60))
            image_frame = customtkinter.CTkLabel(master=self.top_l_frame2,image=password_changed_image,text="")
            image_frame.place(relx=0.4,rely=0.5)
            valid_pass.place(relx=0.25,rely=0.3)
            
            data["users"][self.username]["password"] = pass1
            with open("users.json","w") as file:
                    json.dump(data,file,indent=4)
        else:
            invalid_pass = customtkinter.CTkLabel(master=self.top_l_frame,text="Invalid Password Try again",text_color="Red",font=("Century Gothic",20))
            invalid_pass.place(relx=0.15,rely=0.1)

class Admin(Users):
    def __init__(self,window,username):
        self.window = window
        self.username = username
        super().__init__()

    def manage_user(self):
        font = customtkinter.CTkFont("Proxima Nova Rg",18,'bold')
        text_font = customtkinter.CTkFont("Proxima Nova Rg",18)
        text_font_bold = customtkinter.CTkFont("Proxima Nova Rg",20,"bold")

        self.home_page(1)
        manage = customtkinter.CTkButton(master=self.l_frame,width=220,height=40,text="Other_Students",corner_radius=0,fg_color="#333333",hover_color="#2e2e2e",command=self.manage_user)
        manage.place(y=400)
        self.window.home_page.configure(text="Home Page", command = lambda: self.home_page(1))
        self.r_frame.destroy()
        self.r_frame = customtkinter.CTkFrame(master=self.window)
        self.r_frame.grid(row=0,column=1,rowspan=4,padx=20,pady=20,sticky="nsew")
        self.r_frame.grid_columnconfigure((0,1,2,3),weight=1)
        self.r_frame.grid_rowconfigure(1,weight=1)
        manage_users_frame = customtkinter.CTkFrame(master=self.r_frame)
        manage_users_frame.grid(row=1,column=0,padx=7.5,pady=10,sticky="nsew",columnspan=4)
        manage_user_label = customtkinter.CTkLabel(master=self.r_frame,text="Manage Users")
        manage_user_label.configure(padx=20,font=self.text_font_bold)
        manage_user_label.grid(row=0,column=0,padx=7.5,pady=10,sticky="nw")
        
        #SELECT USER 
        select_user = customtkinter.CTkLabel(master=manage_users_frame,text="Select Student:",font=text_font)
        select_user.place(x=30,y=20)


        #ACC NUMBER
        student_id = customtkinter.CTkLabel(master=manage_users_frame,text=f"Student Name: {0}    Roll Number: {0}"
                                            ,font=text_font,bg_color="#474545",anchor="w",width=2000,height=40)
        student_id.place(x=0,y=90)
        student_id.configure(padx=40)

        #CHANGE GRADE SCALE
        
        change_grade = customtkinter.CTkLabel(master=manage_users_frame,text="Change Grade Scale:",font=text_font)
        grade_list = []
        grade_list.place(x=30,y=170)
        change_grade.place(x=30,y=140)
        self.window.mainloop()
    
    def create_new_user(self):
        new_window = customtkinter.CTkToplevel()
        new_window.title("New User")
        new_window.geometry("600x400")
        new_window.resizable(width=False,height=False)
        frame = customtkinter.CTkFrame(master=new_window,width=580,height=380)
        frame.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
        uentry_label = customtkinter.CTkLabel(master=frame,text="New Username:",font=self.text_font)
        uentry_label.place(x=10,y=20)
        uentry = customtkinter.CTkEntry(master=frame,placeholder_text="New Username",width=180,font=self.text_font)
        uentry.place(x=10,y=50)
        pentry_label = customtkinter.CTkLabel(master=frame,text="New Password:",font=self.text_font)
        pentry_label.place(x=10,y=100)
        password = customtkinter.CTkEntry(master=frame,placeholder_text="New Password",width=180,font=self.text_font)
        password.place(x=10,y=130)
        month_of_joining = customtkinter.CTkOptionMenu(master=frame,values=["January", "February", 'March', "April", "May", 'June', "July", "August", "September", "October", 'November' , "December"],font=self.text_font)
        month_of_joining.place(x=360,y=130)
        month_of_joining_label = customtkinter.CTkLabel(master=frame,text="Month of Joining:",font=self.text_font)
        month_of_joining_label.place(x=360,y=100)

        salary_basic_label = customtkinter.CTkLabel(master=frame,text="Set Basic Pay: ",font=self.text_font)
        set_basic = customtkinter.CTkEntry(master=frame,placeholder_text="Set Basic Pay",font=self.text_font)
        salary_basic_label.place(x=10,y=180)
        set_basic.place(x=10,y=210)

        set_acc_label = customtkinter.CTkLabel(master=frame,text="Roll Number:",font=self.text_font)
        set_acc = customtkinter.CTkEntry(master=frame,placeholder_text="Set Roll Number",font=self.text_font,width=200)
        set_acc_label.place(x=360,y=180)
        set_acc.place(x=360,y=210)

        set_name_label = customtkinter.CTkLabel(master=frame,text="User's Name:",font=self.text_font)
        set_name = customtkinter.CTkEntry(master=frame,placeholder_text="Set User's name",width=200,font=self.text_font)
        set_name_label.place(x=360,y=20)
        set_name.place(x=360,y=50)

        acc_number = customtkinter.CTkEntry(master=frame,placeholder_text="New Password",width=220,font=self.text_font)
        acc_number.place(relx=20,y=180)
user = Users()
user.login_page()