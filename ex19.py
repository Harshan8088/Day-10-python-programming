# generate studnt registration ID

from datetime import datetime
import random

year=datetime.now().year
number=random.randint(1000,9999)

student_id=f"SC{year}{number}"
print("student ID:",student_id)