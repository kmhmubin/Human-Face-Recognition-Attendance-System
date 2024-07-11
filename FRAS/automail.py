import yagmail
import os
import datetime

# Get today's date
date = datetime.date.today().strftime("%B %d, %Y")

# Change directory to 'Attendance' and get the newest file
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest

# Email subject
sub = "Attendance Report for " + str(date)

# Mail information (Replace with your email and app-specific password if needed)
yag = yagmail.SMTP("finixiaglobal@gmail.com", "Finixia@2005")

# Email body
body = "Please find the attached attendance report for " + str(date)

# Send the mail
try:
    yag.send(
        to="Bhaskarjyotisaikia078@gmail.com",  # Corrected here
        subject=sub,  # Email subject
        contents=body,  # Email body
        attachments=filename  # File attached
    )
    print("Email Sent!")
except Exception as e:
    print(f"Failed to send email: {e}")
