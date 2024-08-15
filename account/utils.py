import random

def create_new_ref_number():
      return str(random.randint(1000000000, 9999999999))


def create_new_ref_pin():
      return str(random.randint(1000, 9999))