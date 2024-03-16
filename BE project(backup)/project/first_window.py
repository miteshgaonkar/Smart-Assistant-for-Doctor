import smtplib
import random
import string



def random_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


mail = smtplib.SMTP('smtp.gmail.com:587')
#x = '10'
#msg = x
#mail.starttls()
#mail.login('kushhingol123@gmail.com','kushhingol@1')
#receiver = "kushhingol.kh@gmail.com"
#sender = "kushhingol123@gmail.com"
#mail.sendmail(sender, receiver, msg)
#ail.close()
email = 'kushhingol.kh@gmail.com'
user = random_generator()
paswd = random_generator()

print(user)

x = user
y = paswd
msg = "usename %s & password %s"%(x,y)
mail.starttls()
mail.login('kushhingol123@gmail.com','kushhingol@1')
receiver = "kushhingol.kh@gmail.com"
sender = "kushhingol123@gmail.com"
mail.sendmail(sender, receiver, msg)
mail.close()

