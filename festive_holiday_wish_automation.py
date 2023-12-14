# Import necessary libraries
import smtplib
from datetime import datetime
import time
import random

# Function to generate a random holiday wish from a list of messages
def generate_holiday_wish():
    holiday_messages = [
        "Wishing you a joyous holiday season and a happy New Year!",
        "May your days be merry and bright this holiday season!",
        # ... (more holiday messages)
    ]
    return random.choice(holiday_messages)

# Function to send an email with a specified subject, body, and recipient email addresses
def send_email(subject, body, to_emails):
    sender_email = "youremailaddress@gmail.com"  # Your Gmail address
    password = "your generated app password"  # Paste the generated App Password here

    # Create the email message
    message = f"Subject: {subject}\n\n{body}"

    # Try to connect to the SMTP server and send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)

            # Send the email to each recipient
            for to_email in to_emails:
                server.sendmail(sender_email, to_email, message)
                print(f"Email sent to {to_email} successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main program
if __name__ == "__main__":
    # Initialize holiday_wish
    holiday_wish = None

    # Main loop to generate and display holiday messages until the user is satisfied
    while True:
        if not holiday_wish:
            holiday_wish = generate_holiday_wish()

        print("\nGenerated Holiday Message:\n")
        print(holiday_wish)

        regenerate = input("\nDo you want to regenerate the message? (yes/no): ").lower()
        if regenerate != 'yes':
            break
        else:
            holiday_wish = None

    # Get recipient email addresses from the user
    to_emails = input("\nEnter the recipient's email address(es) separated by commas: ").split(',')

    # Get scheduled date and time for the email
    scheduled_date = input("Enter the scheduled date for the email (YYYY-MM-DD format): ")
    scheduled_time = input("Enter the scheduled time for the email (HH:MM format): ")
    scheduled_datetime = f"{scheduled_date} {scheduled_time}"

    # Check if the scheduled time is in the future
    if datetime.now() < datetime.strptime(scheduled_datetime, "%Y-%m-%d %H:%M"):
        time_difference = (datetime.strptime(scheduled_datetime, "%Y-%m-%d %H:%M") - datetime.now()).total_seconds()

        # Sleep until the scheduled time
        print(f"\nEmail will be sent on {scheduled_datetime}. Sleeping until then...")
        time.sleep(time_difference)

        # Send the email
        subject = "Holiday Greetings"
        send_email(subject, holiday_wish, to_emails)
    else:
        print("Scheduled time is in the past. Please choose a future time.")
