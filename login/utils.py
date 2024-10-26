import random

def send_sms_verification_code(phone_number):
    verification_code = random.randint(1000, 9999)
    print(f"Simulated SMS to {phone_number}: Your verification code is {verification_code}")
    return verification_code
