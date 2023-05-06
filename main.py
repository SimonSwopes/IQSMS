import sms

def main():

    #Change these Strings
    hungryUser = sms.User('TWILIO_ACCOUNT_SID',
                     'TWILIO_AUTH_TOKEN',
                     'TWILIO_PHONE_NUMBER')

    #Replace with recieving number incude country code
    hungryUser.sendSMS('+1234567891')
if __name__ == "__main__":
    main()