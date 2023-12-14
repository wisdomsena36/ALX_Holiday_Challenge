# Holiday Email Scheduler

This Python script allows users to generate random holiday messages that spread holiday cheer, customize them, and schedule emails to be sent to specified recipients or loved one at a later date and time. The script uses Gmail's SMTP server for email delivery.

## Features

- **Holiday Message Generation:** Choose from a list of pre-defined holiday messages or regenerate a new one until satisfied.
- **Email Customization:** Personalize the email subject, body, and recipient email addresses.
- **Scheduling:** Set a specific date and time for the email to be sent in the future.
- **Error Handling:** Provides feedback on successful email delivery and handles errors gracefully.

## Dependencies

- Python 3
- `smtplib` (Standard Library)
- `datetime` (Standard Library)
- `time` (Standard Library)
- `random` (Standard Library)

## Gmail App Password Setup

To use Gmail's SMTP server for sending emails, you need to generate an App Password. Follow these steps:

1. **Go to Google Account Security Settings:**
   - Navigate to [Google Account](https://myaccount.google.com/).
   - Click on "Security" in the left sidebar.

2. **App Passwords:**
   - Scroll down to the "Signing in to Google" section.
   - Click on "App passwords."

3. **Select App:**
   - In the "Select app" dropdown, choose "Mail."
   - In the "Select device" dropdown, choose "Other (Custom name)."

4. **Custom Name:**
   - Enter a custom name for the App Password (e.g., "HolidayEmailScheduler").
   - Click "Generate."

5. **Copy App Password:**
   - Copy the generated App Password.

## Integrating App Password into the Script

After obtaining the App Password, update the `password` variable in the script with the copied value. Open the `holiday_email_scheduler.py` file and locate the following lines:

```python
# Email configuration
sender_email = "youremailaddress@gmail.com"  # Your Gmail address
password = "your generated app password"  # Paste the generated App Password here
```

Replace `"youremailaddress@gmail.com"` with your Gmail address.

Replace `"your generated app password"` with the App Password you generated. Save the changes.

Now, the script is configured to use the generated App Password for authentication when connecting to Gmail's SMTP server.

Please note that you should keep your App Password secure and not share it publicly. If you have security concerns, consider using environment variables or a configuration file to store sensitive information.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/holiday-email-scheduler.git
   ```

2. Navigate to the project directory:

   ```bash
   cd festive_holiday_wish_automation
   ```

3. Run the script:

   ```bash
   python festive_holiday_wish_automation.py
   ```

4. Follow the prompts to generate a holiday messages that spread holiday cheer, customize the email, and schedule its delivery.


## Troubleshooting

### Holiday Messages Not Found in Primary Inbox

If you've tested the script, but you don't see your holiday messages in your primary inbox, consider checking your spam folder. Occasionally, email filters may categorize messages as spam. If the issue persists, please review your email settings and ensure they allow messages from the configured sender email address.


## Contributions

Contributions are welcome! If you encounter any issues, have suggestions, or want to improve the script, feel free to open an issue or submit a pull request.

## Authors

- **Author 1:**
  - Name: Wisdom Edem Sena
  - GitHub: [Wisdom Sena](https://github.com/wisdomsena36)

- **Author 2:**
  - Name: Mabel Ablah Zigah
  - GitHub: [Mabel Zigah](https://github.com/mabrite)
