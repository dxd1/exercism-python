from datetime import timedelta
from math import pow

def add_gigasecond(bday):
    return bday + timedelta(seconds = pow(10,9))
