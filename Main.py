import random  # Importing random module for generating OTP
import smtplib  # Importing smtplib for sending emails
import re  # Importing re module for validating email format

# Function to generate a 6-digit OTP
def Get_OTP():
    allDigits = "0123456789"  # String containing all possible digits
    _otp = ""  # Initialize OTP as an empty string
    for i in range(6):  # Loop to generate a 6-digit OTP
        _otp += allDigits[random.randint(0, 9)]  # Select random digit from allDigits and append it to OTP
    return _otp  # Return the generated OTP

# Generate and store the current OTP
Current_OTP = Get_OTP()

# Function to get a valid email address from the user
def GetEmail():
    _id = input("Enter Your Email Address:\n")  # Prompt user for email input
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'  # Regular expression for email validation
    
    if re.fullmatch(regex, _id):  # Check if entered email matches regex pattern
        return _id  # Return valid email
    else:
        print("You entered an invalid email. Example format: abc43@xyz.com")  # Inform user of invalid email
        return GetEmail()  # Recursively prompt for a valid email

# Counter for OTP verification attempts
attempts = 0

# Function to check if the entered OTP matches the generated OTP
def Check_OTP():
    global attempts  # Access global attempts variable
    attempts += 1  # Increment the attempt counter
    _receivedOtp = input("Enter Your OTP >>:\n")  # Prompt user to enter OTP
    
    if _receivedOtp == Current_OTP:  # If entered OTP matches the generated OTP
        print("Verified!!!")  # Print success message
    else:
        if attempts < 3:  # Allow up to 3 attempts
            print("Incorrect OTP. Please try again.")  # Inform user of incorrect OTP
            Check_OTP()  # Recursively call function for another attempt
        else:
            print("Verification Failed.")  # Print failure message after 3 attempts

# SMTP setup to send OTP via email
_server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to Gmail SMTP server on port 587
_server.starttls()  # Upgrade the connection to a secure TLS/SSL mode

_senderEmail = "Enter sender Email"  # Replace with sender's email
_server.login(_senderEmail, "sender app password")  # Login with sender's credentials

# Get recipient's email from user
emailid = GetEmail()

# Construct email message with OTP
msg_context = f'From: {_senderEmail}\r\nTo: {emailid}\r\nSubject: OTP Verification.\r\n\r\nYour One Time Password is: {Current_OTP}'

# Send OTP email
_server.sendmail(_senderEmail, emailid, msg_context)

# Call function to check OTP
Check_OTP()
