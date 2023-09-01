import schedule
import time
from datetime import datetime

# Function to say hello
def say_hello():
    print(f"Hello Sarue, it currently is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Schedule 'say_hello' function to run every day at 09:00 am
schedule.every().day.at("00:53").do(say_hello)

while True:
    schedule.run_pending()
    now = datetime.now()
    print(now)
    time.sleep(1)