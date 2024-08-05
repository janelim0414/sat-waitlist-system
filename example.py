from sat_scraper import TestSite
from apscheduler.schedulers.blocking import BlockingScheduler as scheduler

your_email = 'you@gmail.com'
your_pw = '1234 1234 1234 1234'
recipient = 'other@gmail.com'
zip_code = '12345'
test_date = 'yyyy-mm-dd'

scraper = TestSite(test_date, zip_code, your_email, recipient, your_pw)

sch = scheduler()
sch.add_job(scraper._extract_test_sites, 'interval', seconds=10)
sch.start()