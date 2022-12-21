from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"index.html")

def contact(request):
    if request.method == 'POST':
        print("hello")
    name = request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']

    data = {'name': name,
            'email': email,
            'subject': subject,
            'message': message}
    message = '''
    Portfolio Notification:{}
    From:{}
    '''.format(data['message'], data['email'])
    send_mail(data['subject'], message, '', ['dannywanyoike@gmail.com'])
    messages.success(
        request, 'Your message has been sent.I will get back to you shortly. Thank you!')
    return redirect('/')    