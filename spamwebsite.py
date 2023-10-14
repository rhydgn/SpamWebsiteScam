import requests
import random

url = input("url : ")
spam = int(input("spam : "))

def makePayLoad(nomor, pin, otp):
    return {
        "number" : nomor,
        "pin" : pin,
        "otp" : otp
    }


with open('1900-2020.txt') as f:
    number = list(f)
with open('6-digits-000000-999999.txt') as f:
    pwd = list(f)
with open('4-digits-0000-9999.txt') as f:
    otp = list(f)
number = list(map((lambda s: s.replace('\n','').lower()), number))
pwd = list(map((lambda s: s.replace('\n','').lower()), pwd))
otp = list(map((lambda s: s.replace('\n','').lower()), otp))

def makeRandomPin ():
    pii = random.choice(pwd)
    m = 'pin: '
    return m + pii


def makeRandomNumber ():
    nmb = random.choice(number)
    m = '+62 857'
    return m + nmb


def makeRandomOtp ():
    pp = random.choice(otp)
    m = ' otp: '
    return m + pp


for i in range(0,spam):
    nomor = makeRandomNumber()
    pinn = makeRandomPin()
    otpp = makeRandomOtp()
    data = makePayLoad(nomor,pinn,otpp)
    response = requests.post(url, data=data).status_code
    i += 1
    if (response > 299):
        print("failed to send data due to error code " "%s - %s %s %s (%s)" % (i, nomor, pinn, otpp, response))
    elif (response > 199):
        print("successfully sent fake data " "%s - %s %s %s (%s)" % (i, nomor, pinn, otpp, response))
