from twilio.rest import Client
import MQFinder

"""Stores the parameters required for the twilio api sms service
    will throw error if token/sid or any number is invalid. does
    check that the length of these are valid but nothing more"""
class User():
    def __init__(self, acc_sid: str, auth_tok: str, twilio_num: str):
        #assuming the tokens are the same length as mine
        if len(acc_sid + auth_tok + twilio_num) != 78:
            raise Exception("Invalid SID/Token or Number")
        self.__sid = acc_sid
        self.__tok = auth_tok
        self.__twilioNum = twilio_num
        self.__client = Client(acc_sid, auth_tok)
        self.__quotes = MQFinder.quotes()


    """the set and get property for twilioNUm and the accUpdate
    method at the moment are not particularly useful at runtime
    but they may be useful in later versions"""

    #allows for user to change their num
    @property
    def twilioNum(self):
        return self.__twilioNum
    @twilioNum.setter
    def twilioNum(self, new_num):
        self.__twilioNum = new_num

    #allows for credential update
    def accUpdate(self, new_sid: str, new_tok: str):
        if len(new_sid, new_tok) != 66:
            raise Exception("Invalid Token or SID")
        self.__sid = new_sid
        self.__tok = new_tok
        self.__client = Client(self.__sid, self.__tok)

    def sendSMS(self, targetNum: str):
        if len(targetNum) != 12:
            raise Exception("Invalid Client Number")
        msg = self.__quotes.get_quote()
        self.__deliverText(msg, targetNum)

    def __deliverText(self, msg: str, targetNum: str):
        unsent = ""
        if len(msg) > 1600:
            unsent = msg[1600:]
            msg = msg[:1600]

        message = self.__client.messages.create(
            body = msg,
            from_= self.twilioNum,
            to=targetNum
        )

        if unsent:
            self.sendSms(unsent, targetNum)