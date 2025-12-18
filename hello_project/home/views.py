#from django.http import HttpResponse
from django.shortcuts import render
#import random

# Create your views here.
def home_view(request):
    messages = [
        "That's what's meant to happen!",
        "Oooh you pressed it again!😁",
        "Again!😏I think you want to invite me for a drink😅",
        "You sure?",  
        "Woww,Okey let's go coz you insisted!😜",
        "Okey now Sherehee ndo kuanza!!🎉"
    ]

    #get the messages by default to 0
    index = request.session.get('message_index',0)

    message = ""
    if request.method == "POST":
        message = messages[index] #pick current message
        index = (index + 1) % len(messages) #move to next
        request.session['message_index'] = index #save for the next click
    return render(request, 'home/index.html', {'message': message})
