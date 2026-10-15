# date and time module

from datetime import datetime

now=datetime.now()
print("current date:",now.date())
print("current time:",now.strftime("%H:%M:%S"))