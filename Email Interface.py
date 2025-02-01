# #mail interface
# send abstract
# email
# sms
# whatsapp
from abc import ABC, abstractmethod

class Mail(ABC):
    @abstractmethod

    def disp(self):
        pass

class Email(Mail):
    def disp(self):
        print("Message is sent through Email")

class SMS(Mail):
    def disp(self):
        print("Message is sent through SMS")

class Whatsapp(Mail):
    def disp(self):
        print("Message is sent through Whatsapp")

a=Email()
a.disp()

b=SMS()
b.disp()

c=Whatsapp()
c.disp()