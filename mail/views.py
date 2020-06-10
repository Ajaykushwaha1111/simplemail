

from django.shortcuts import HttpResponse,render
from django.core.mail import EmailMessage
import random
def mailSend(request):
    res =dict()
    if request.method=='POST':
        email =request.POST.get('email')
        mess =request.POST.get('mess')
        otp =random.randrange(1111,9999)
        header=f"Your otp is {otp}"
        try:
            email = EmailMessage(header, mess, to=[email])
            email.send()
            res['status']="Mail Send Succesful !"
        except:
            res['status'] = "Your Email Not No valid !"



    return render(request,'mail.html',res)