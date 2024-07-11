import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize  # Import the Recognize module
import utils  # Import the utils module
import datetime

# creating the title bar function
def title_bar():
    os.system('cls' if os.name == 'nt' else 'clear')  # for windows and Unix-based systems
    # title of the program
    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********By FINIXIA DEDECONS************")

# creating the user main menu function
def mainMenu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Auto Mail")
    print("[6] Clear Student Data")  # Existing option
    print("[7] Clear Attendance Logs by Date")  # New menu option
    print("[8] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))

            if choice == 1:
                checkCamera()
                break
            elif choice == 2:
                CaptureFaces()
                break
            elif choice == 3:
                Trainimages()
                break
            elif choice == 4:
                RecognizeFaces()
                break
            elif choice == 5:
                os.system("py automail.py" if os.name == 'nt' else "python3 automail.py")
                break
            elif choice == 6:
                clearStudentData()
                break
            elif choice == 7:
                clearAttendanceByDate()
                break
            elif choice == 8:
                print("Thank You")
                break
            else:
                print("Invalid Choice. Enter 1-8")
                mainMenu()
        except ValueError:
            print("Invalid Choice. Enter 1-8\n Try Again")
    exit

# calling the camera test function from check_camera.py file
def checkCamera():
    check_camera.camer()
    key = input("Enter any key to return main menu")
    mainMenu()

# calling the take image function form capture image.py file
def CaptureFaces():
    Capture_Image.takeImages()
    key = input("Enter any key to return main menu")
    mainMenu()

# calling the train images from train_images.py file
def Trainimages():
    Train_Image.TrainImages()
    key = input("Enter any key to return main menu")
    mainMenu()

# calling the recognize_attendance from Recognize.py file
def RecognizeFaces():
    Recognize.recognize_attendance()
    key = input("Enter any key to return main menu")
    mainMenu()

# New function to clear student data
def clearStudentData():
    utils.clear_student_data("StudentDetails/StudentDetails.csv")
    key = input("Enter any key to return main menu")
    mainMenu()

# New function to clear attendance logs by date
def clearAttendanceByDate():
    try:
        date_str = input("Enter the date (YYYY-MM-DD) for which to clear attendance logs: ")
        datetime.datetime.strptime(date_str, '%Y-%m-%d')  # Validate date format
        Recognize.clear_attendance_by_date(date_str)
    except ValueError:
        print("Invalid date format. Please enter date in YYYY-MM-DD format.")
    
    input("Enter any key to return to the main menu")
    mainMenu()

# ---------------main driver ------------------
mainMenu()
