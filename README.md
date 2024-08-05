# SAT Test Center Notification System

As a high school student preparing for the SAT, you might have faced the challenge of finding a nearby test center with available seats. Implemented with Requests and BeautifulSoup, this Python script helps alleviate that stress by monitoring test centers within a 100-mile radius of your zip code. Whenever a new test center with available seats is detected, the script sends you an email notification.

Inspired by Resy's waitlist system, this solution uses a web scraper to query the College Board's API and gather real-time information about test center availability. This way, you can minimize travel time, get a good night's sleep, and perform your best on test day!

## How to use
1. Clone the repository 
   ```
   git clone 
   ```
2. Create an app password for sender's email
3. Configure ```examples.py``` file to match personal information (sender's/recipient's email, password, zip code, etc.)
4. Run ```examples.py``` on terminal
   ```
   python examples.py
   ```
5. Let it run until you find the test center you like!

## How it works

Initialization: \
The __init__ method initializes the class with details such as the test date, zip code, sender's and recipient's email addresses. It also constructs the URL for querying test centers and stores the email password securely from environment variables.

Extracting Test Sites: \
The _extract_test_sites method makes an HTTP GET request to the API endpoint, parses the response, and updates the list of available test centers. It triggers notifications for newly available test centers.

Notification: \
The _notify method constructs an email message with details about the newly available test center and sends it to the specified recipient using an SMTP server.
