import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText

class TestSite:
    def __init__(self, date, zip, sender, recipient, pw):
        # for web request
        self.url = f'https://aru-test-center-search.collegeboard.org/prod/test-centers?date={date}&zip={zip}&country=US'
        self.test_sites = []
        # for sending email
        self.zip = zip
        self.sender = sender
        self.recipient = recipient
        self.pw = pw
    
    def _extract_test_sites(self):
        with requests.Session() as s:
            # query test sites
            response= s.get(self.url)
            sites = BeautifulSoup(response.text, 'html.parser')
            sites_json = json.loads(sites.text)
            # extract sites with available seats
            for site in sites_json:
                if site['seatAvailability'] and not site in self.test_sites:
                    self._notify(site['name'], site['address1'], site['city'], site['state'])
                    self.test_sites.append(site)
                elif not site['seatAvailability'] and site in self.test_sites:
                    self.test_sites.remove(site)
        return self.test_sites
    
    def _notify(self, name, street, city, state):
        # construct a message
        body = f"""
        Good news! New test site is available near {self.zip}. \n
        Test site: {name}
        Address: {street}, {city}, {state}
        Go to college board to reschedule your test appointment. 
        """
        msg = MIMEText(body)
        msg['Subject'] = 'New Test Site Is Available'
        msg['From'] = self.sender
        msg['To'] = self.recipient
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # log into gmail with email & password
        s.starttls()
        s.login(self.sender, self.pw)
        # send mail to recipient
        s.sendmail(self.sender, self.recipient, msg.as_string())
        s.quit()