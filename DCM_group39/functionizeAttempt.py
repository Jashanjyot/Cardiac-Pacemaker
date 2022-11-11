#import modules

from math import ceil
from tkinter import *
import os
import time
import tkinter
import InputScreen
from combineFuncs import combine_funcs
from combineFuncs import roundToNearest
#global constants

#registration
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register aaaaaa")
    register_screen.geometry("300x300")
 
    global username
    global password
    global confirm
    global username_entry
    global password_entry
    global confirm_entry
    
    username = tkinter.StringVar(register_screen)
    password = StringVar()
    confirm = StringVar()
 
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show= '*')
    password_entry.pack()
    
    confirm_lable = Label(register_screen, text="Verify Password * ")
    confirm_lable.pack()
    confirm_entry = Entry(register_screen, textvariable=confirm, show= '*')
    confirm_entry.pack()
    
    list_of_files = os.listdir()  
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="light green", command = register_user).pack()
# login 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# click register
def register_user():
    global username_info
    username_info = StringVar()
    username_info = username.get()
    password_info = password.get()
    confirm_info = confirm.get()
    tally = 0
    files = os.listdir()
    
    for i in files:
        tally = tally + 1
    if tally <= 11:
 
        if password_info != confirm_info:
            password_not_matched()
        else:
            global file
            file = open(username_info, "w")
            file.write(username_info + "\n")
            file.write(password_info + "\n")
            #file.close()
 
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            confirm_entry.delete(0, END)
 
            Label(register_screen, text="Success", fg="green", font=("calibri", 11)).pack()
            delete_register_screen()
            delete_main_screen()
            select_mode_register()
    else:
        max_users()           
# allow new user to pick mode
def select_mode_register():
    global i
    i = 1
    global mode_screen
    mode_screen = Tk()
    mode_screen.geometry("600x600")
    mode_screen.title("Pacing Mode select")
    #embedded function to get selection
    def get_mode():
        selection = tkinter.StringVar(mode_screen)
        selection = mode_sel.get()
        label = Label(mode_screen, bg="green", text="Selection of " + selection + " is Successful")
        label.pack()
        button = Button(mode_screen, text = "Confirm", command = add2file).pack()
    #embedded function to add to file and move to parameter selection, still needs the actual file adding, currently only transports you to the next step
    def add2file():
        mode = tkinter.StringVar(mode_screen)
        mode = mode_sel.get()
        username_info = username.get()
        if mode == "AOO":
            #file = open(username_info, "w")
            file.write(mode + "\n")
            file.close()
            AOO_selections()
            delete_mode_screen()
        elif mode == "VOO":
            file.write(mode + "\n")
            file.close()
            VOO_selections()
            delete_mode_screen()
        elif mode == "AAI":
            file.write(mode + "\n")
            file.close()
            AAI_selections()
            delete_mode_screen()
        elif mode == "VVI":
            file.write(mode + "\n")
            file.close()
            VVI_selections()
            delete_mode_screen()
        
 
    Label(mode_screen, text="Before Starting, please select a pacing mode", bg="#C70039", width="300", height="2", font=("Calibri", 13)).pack()
    mode_sel= tkinter.StringVar(mode_screen)
    mode_sel.set("AOO")
    ModeOptions = ["AOO","VOO","AAI","VVI"]
    drop= tkinter.OptionMenu(mode_screen, mode_sel, *ModeOptions) #andrew this is the type of line youre gonna wanna edit,
    drop.pack()
    button = Button(mode_screen, text = "Select", command = get_mode).pack()
def select_mode_edit():
    global i
    i = 0
    global mode_screen
    mode_screen = Tk()
    mode_screen.geometry("600x600")
    mode_screen.title("Pacing Mode select")
    button = Button(mode_screen, text = "Back to Dashboard", command = combine_funcs(dashboard, delete_mode_screen)).pack()
    file = open(name, 'a')
    #embedded function to get selection
    def get_mode():
        selection = tkinter.StringVar(mode_screen)
        selection = mode_sel.get()
        label = Label(mode_screen, bg="green", text="Selection of " + selection + " is Successful")
        label.pack()
        button = Button(mode_screen, text = "Confirm", command = add2file).pack()
    #embedded function to add to file and move to parameter selection, still needs the actual file adding, currently only transports you to the next step
    def add2file():
        mode = tkinter.StringVar(mode_screen)
        mode = mode_sel.get()
        if mode == "AOO":
            file.write(mode + "\n")
            file.close()
            AOO_selections()
            delete_mode_screen()
        elif mode == "VOO":
            file.write(mode + "\n")
            #file.close()
            VOO_selections()
            delete_mode_screen()
        elif mode == "AAI":
            file.write(mode + "\n")
            #file.close()
            AAI_selections()
            delete_mode_screen()
        elif mode == "VVI":
            file.write(mode + "\n")
            #file.close()
            VVI_selections()
            delete_mode_screen()
        
 
    Label(mode_screen, text="Before Starting, please select a pacing mode", bg="#C70039", width="300", height="2", font=("Calibri", 13)).pack()
    mode_sel= tkinter.StringVar(mode_screen)
    mode_sel.set("AOO")
    ModeOptions = ["AOO","VOO","AAI","VVI"]
    drop= tkinter.OptionMenu(mode_screen, mode_sel, *ModeOptions) #andrew this is the type of line youre gonna wanna edit,
    drop.pack()
    button = Button(mode_screen, text = "Select", command = get_mode).pack()
#when completed, these four functions will add the parameters to the txt file created upon register. I have not done that yet but probably will soon
#def roundToNearest(input, toNearest=5):
#    return toNearest * round(input/toNearest)
def success_param():
    global success_screen
    success_screen = Tk()
    success_screen.geometry("300x300")
    success_screen.title("parameter save success")
    def to_login():
        delete_success_screen()
        main_account_screen()
        
    Label(success_screen, text = 'Your parameters have been saved!', font=("Calibri", 13), bg = "#20E714", width="300", height="2").pack()
    Button(success_screen, text = "Back to main screen", command = to_login).pack()
    
def AOO_selections():
    #where I am saving 
    file = open(username_info,'a')
    #create class object 
    AOO_screen = InputScreen.InputScreenClass("AOO",file)
    
    #ranges for inputs, increments for those ranges, label, default value, whether or not "Off" is a valid input for 0 = FALSE
    AOO_screen.addInputBox([30,50,90,175],[5,1,5],"LRL (ppm) ",60) 
    AOO_screen.addInputBox([50,175],[5],"URL (ppm) ",120)
    AOO_screen.addInputBox([0.5,3.2,3.5,7],[0.1,0.5,0.5],"A Pulse Amplitude (V) ",3.5,TRUE)
    AOO_screen.addInputBox([0.05,0.1,1.9],[0.05,0.1],"A Pulse Width (ms) ",0.4)
    #AOO_screen.addInputBox([150,500],[10],"A Refractory Period (ms) ",320) #just for testing
    AOO_screen.open()
    #file.close()
def VOO_selections(): ##literally the same as AOO except with some varible names swapped
    VOO_screen = InputScreen.InputScreenClass("AOO")
    #ranges for inputs, increments for those ranges, label, default value, whether or not "Off" is a valid input for 0 = FALSE
    VOO_screen.addInputBox([30,50,90,175],[5,1,5],"LRL (ppm) ",60) 
    VOO_screen.addInputBox([50,175],[5],"URL (ppm) ",120)
    VOO_screen.addInputBox([0.5,3.2,3.5,7],[0.1,0.5,0.5],"V Pulse Amplitude (V) ",3.5,TRUE)
    VOO_screen.addInputBox([0.05,0.1,1.9],[0.05,0.1],"V Pulse Width (ms) ",0.4)
    VOO_screen.open()
                        
def AAI_selections():
    AAI_screen = InputScreen.InputScreenClass("AAI")
    #ranges for inputs, increments for those ranges, label, default value, whether or not "Off" is a valid input for 0 = FALSE
    AAI_screen.addInputBox([30,50,90,175],[5,1,5],"LRL (ppm) ",60) 
    AAI_screen.addInputBox([50,175],[5],"URL (ppm) ",120)
    AAI_screen.addInputBox([0.5,3.2,3.5,7],[0.1,0.5,0.5],"A Pulse Amplitude (V) ",3.5,TRUE)
    AAI_screen.addInputBox([0.05,0.1,1.9],[0.05,0.1],"A Pulse Width (ms) ",0.4)
    AAI_screen.addInputBox([0.25,1,10],[0.25,0.5],"A Sensitivity (ms) ",0.75) #swap for VVI
    AAI_screen.addInputBox([150,500],[10],"A Refractory Period (ms) ",250) #swap for VVI
    AAI_screen.addInputBox([30,50,90,175],[5,1,5],"Hysteresis Rate Limit (ms) ",60,TRUE) #same as LRL
    AAI_screen.addInputBox([3,21,25],[3,5],"Rate Smoothing (%)",60,TRUE) #edgecase needs testing 
    AAI_screen.addInputBox([150,500],[10],"PVARP (ms)",250,TRUE) #edgecase needs testing 
    AAI_screen.open()

def VVI_selections():
    AAI_screen = InputScreen.InputScreenClass("AAI")
    #ranges for inputs, increments for those ranges, label, default value, whether or not "Off" is a valid input for 0 = FALSE
    AAI_screen.addInputBox([30,50,90,175],[5,1,5],"LRL (ppm) ",60) 
    AAI_screen.addInputBox([50,175],[5],"URL (ppm) ",120)
    AAI_screen.addInputBox([0.5,3.2,3.5,7],[0.1,0.5,0.5],"V Pulse Amplitude (V) ",3.5,TRUE)
    AAI_screen.addInputBox([0.05,0.1,1.9],[0.05,0.1],"V Pulse Width (ms) ",0.4)
    AAI_screen.addInputBox([0.25,1,10],[0.25,0.5],"V Sensitivity (ms) ",2.5) #swap for VVI
    AAI_screen.addInputBox([150,500],[10],"V Refractory Period (ms) ",320) #swap for VVI
    AAI_screen.addInputBox([30,50,90,175],[5,1,5],"Hysteresis Rate Limit (ms) ",60,TRUE) #same as LRL
    AAI_screen.addInputBox([3,21,25],[3,5],"Rate Smoothing (%)",60,TRUE) #edgecase needs testing 
    AAI_screen.open()
def login_verify():
    username1 = username_verify.get()
    global name
    name = StringVar()
    name = username1
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# login sucess procedure 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()

    delete_login_screen()
    delete_main_screen()
    dashboard()
# Designing popup for too many users
 
def max_users():
    global max_users_screen
    max_users_screen = Toplevel(register_screen)
    max_users_screen.title("error")
    max_users_screen.geometry("150x100")
    Label(max_users_screen, text="max # of users reached").pack()
    Button(max_users_screen, text="OK", command=delete_max_users_screen).pack()
    
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
    
# popup for unmatching passwords
def password_not_matched():
    global password_not_matched_screen
    password_not_matched_screen = Toplevel(register_screen)
    password_not_matched_screen.title("error")
    password_not_matched_screen.geometry("150x100")
    Label(password_not_matched_screen, text="Passwords do not match ").pack()
    Button(password_not_matched_screen, text="OK", command=delete_password_not_matched).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
# combining functions for buttons 

# Deleting stuff
 
def delete_login_success():
    login_success_screen.destroy()
    
def delete_password_not_matched():
    password_not_matched_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def delete_max_users_screen():
    max_users_screen.destroy()

def delete_login_screen():
    login_screen.destroy()

def delete_register_screen():
    register_screen.destroy()

def delete_main_screen():
    main_screen.destroy()

def delete_mode_screen():
    mode_screen.destroy()

def delete_dashboard():
    dash_screen.destroy()
    
def delete_AOO_screen():
    AOO_screen.destroy()

def delete_VOO_screen():
    VOO_screen.destroy()

def delete_AAI_screen():
    AAI_screen.destroy()

def delete_VVI_screen():
    VVI_screen.destroy()
    
def delete_success_screen():
    success_screen.destroy()
 
# Designing login/register (first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="#C70039", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
#creating dashboard after login (this is where all selections will go)
def dashboard():
    global dash_screen
    dash_screen = Tk()   
    dash_screen.geometry("600x600")
    dash_screen.title("Dashboard")
    Label(text="Welcome to the Dashboard", bg="#C70039", width="300", height="2", font=("Calibri", 15)).pack() #adding which user it is would be nice
    button = Button(dash_screen, text = "Back to Login", command = combine_funcs(delete_dashboard, main_account_screen)).place(x=0,y=2)
    Label(text="FOR TESTING PURPOSES ONLY",bg = "orange",font=("calibri", 14)).place(x=0, y=500)
    #need to find a way to port username to dashboard, likley need to redo the way things save in register
    #username_info = username.get()
    #Label(text="Welcome, signed in as" + username_info ,font=("calibri", 16)).pack()
    
    def change_status_c2d():
        status_label = Label(text="Status: connected", bg = 'green', width="30").place(x=60, y=600)
        Button(dash_screen, text = "change status", command = change_status_d2c).place(x=0, y=600)         

    def change_status_d2c():  
        status_label = Label(text="Status: disconnected", bg = 'red', width="30").place(x=60, y=600)
        Button(dash_screen, text = "change status", command = change_status_c2d).place(x=0, y=600)

    def change_pacemaker_1st():
            Label(dash_screen, text = ' ', width = 100, height = 2).place(x=0,y=550)
            status_label = Label(text="Pacemaker 1 Connected", bg = "cyan",width="30").place(x=80, y=550)
            Button(dash_screen, text = "change pacemaker", command = change_pacemaker_2nd).place(x=0, y=550)
            
            
    def change_pacemaker_2nd():
            status_label = Label(text="Pacemaker 2 Connected", bg = "cyan", width="30").place(x=80, y=550)
            Button(dash_screen, text = "change pacemaker", command = change_pacemaker_3rd).place(x=0, y=550)
            
    def change_pacemaker_3rd():
        status_label = Label(text="Pacemaker 3 Connected",bg = "cyan", width="30").place(x=80, y=550)
        Button(dash_screen, text = "change pacemaker", command = change_pacemaker_1st).place(x=0, y=550)
        
    Button(dash_screen, text="show status", command = change_status_c2d).place(x=0, y=600)
    Button(dash_screen, text="show connected pacemaker", command = change_pacemaker_1st).place(x=0, y=550)
    Label(dash_screen, text = "Hello " + name +"!", bg = "yellow", font=("Calibri", 13)).pack()
    userfile = open(name, 'r')
    filelines = userfile.readlines()
    user_name = filelines[0]
    user_pass = filelines[1]
    user_mode = filelines[2]
    Label(dash_screen, text = "Your Current Settings", bg = "#C70039", font = ("Calibri", 12)).place(x=0,y=120)
    Label(dash_screen, text = "mode = " + user_mode).place(x=0,y=150)

    def edit_selections():
        file = open(name, 'w')
        file.write(user_name)
        file.write(user_pass)
        file.close()
        select_mode_edit()
        delete_dashboard()
        
    if user_mode == "AOO"+ '\n':
        user_lrl = filelines[3]
        user_url = filelines[4]
        user_aa = filelines[5]
        user_apw = filelines[6]
        Label(dash_screen, text = "LRL = " + user_lrl).place(x=0,y=165)
        Label(dash_screen, text = "URL = " + user_url).place(x=0,y=180)
        Label(dash_screen, text = "AA = " + user_aa).place(x=0,y=195)
        Label(dash_screen, text = "APW = " + user_apw).place(x=0,y=210)
        Button(dash_screen, text = 'edit selections', command = edit_selections).place(x=0,y=225)
    elif user_mode == "VOO"+ '\n':
        user_lrl = filelines[3]
        user_url = filelines[4]
        user_va = filelines[5]
        user_vpw = filelines[6]
        Label(dash_screen, text = "LRL = " + user_lrl).place(x=0,y=165)
        Label(dash_screen, text = "URL = " + user_url).place(x=0,y=180)
        Label(dash_screen, text = "VA = " + user_va).place(x=0,y=195)
        Label(dash_screen, text = "VPW = " + user_vpw).place(x=0,y=210)
        Button(dash_screen, text = 'edit selections', command = edit_selections).place(x=0,y=225)
        
    elif user_mode == "AAI"+ '\n':
        user_lrl = filelines[3]
        user_url = filelines[4]
        user_aa = filelines[5]
        user_apw = filelines[6]
        user_as = filelines[7]
        user_arp = filelines[8]
        user_pvarp = filelines[9]
        user_hyster = filelines[10]
        user_smooth = filelines[11]
        Label(dash_screen, text = "LRL = " + user_lrl).place(x=0,y=165)
        Label(dash_screen, text = "URL = " + user_url).place(x=0,y=180)
        Label(dash_screen, text = "AA = " + user_aa).place(x=0,y=195)
        Label(dash_screen, text = "APW = " + user_apw).place(x=0,y=210)
        Label(dash_screen, text = "AS = " + user_as).place(x=0,y=225)
        Label(dash_screen, text = "ARP = " + user_arp).place(x=0,y=240)
        Label(dash_screen, text = "PVARP = " + user_pvarp).place(x=0,y=255)
        Label(dash_screen, text = "HYSTER= " + user_hyster).place(x=0,y=270)
        Label(dash_screen, text = "SMOOTH = " + user_smooth).place(x=0,y=285)
        Button(dash_screen, text = 'edit selections', command = edit_selections).place(x=0,y=300)
        
    elif user_mode == "VVI"+ '\n':
        user_lrl = filelines[3]
        user_url = filelines[4]
        user_va = filelines[5]
        user_vpw = filelines[6]
        user_vs = filelines[7]
        user_vrp = filelines[8]
        user_hyster = filelines[9]
        user_smooth = filelines[10]
        Label(dash_screen, text = "LRL = " + user_lrl).place(x=0,y=165)
        Label(dash_screen, text = "URL = " + user_url).place(x=0,y=180)
        Label(dash_screen, text = "VA = " + user_va).place(x=0,y=195)
        Label(dash_screen, text = "VPW = " + user_vpw).place(x=0,y=210)
        Label(dash_screen, text = "VS = " + user_vs).place(x=0,y=225)
        Label(dash_screen, text = "VRP = " + user_vrp).place(x=0,y=240)
        Label(dash_screen, text = "HYSTER= " + user_hyster).place(x=0,y=270)
        Label(dash_screen, text = "SMOOTH = " + user_smooth).place(x=0,y=285)
        Button(dash_screen, text = 'edit selections', command = edit_selections).place(x=0,y=300)
        
        
    


##TO DO: 2-make parameters save to file (probably same code for both), 3-add confirm button to parameters to update files 4- (andrew) make all parameters within guidelines and bound by eachother 5- read files to dashboard and allow edits from there
    
#run start
main_account_screen()
