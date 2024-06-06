from dotenv import load_dotenv
from driver import Driver
import time

load_dotenv()


driver = Driver()
driver.login()
time.sleep(5)
accounts = driver.get_accounts()
[print(a) for a in accounts]
time.sleep(5)
# driver.quit()