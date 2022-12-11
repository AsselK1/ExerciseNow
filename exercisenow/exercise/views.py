from django.shortcuts import render
from .models import Video
from .forms import VideoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from exercise import views
from counter import main
import random
def index(request):

    context = {

    }
    return render(request, 'index.html', context=context)

def profile(request):
    name = 'Your'
    calendar = []
    for i in range(35):
        calendar.append(0)
    for i in range(3, 15):
        calendar[i] = 1
    calendar[5] = 2
    calendar[8] = 2 #0 = grey, 1=green, 2=red
    calendar2 = []
    for i in range(5):
        temp = []
        for j in range(7):
            temp.append(calendar[i * 7 + j])
        calendar2.append(temp)

    reward = 3
    max_reward = 10
    context = {'name': name,
        'calendar': calendar2,
        'reward': reward,
        'max_reward': max_reward}

    return render(request, 'profile.html', context=context)
def inference():
    # returns dict: {pushup: reps, situp: reps, pull ups: reps, squat: reps}
    last_video = Video.objects.last()
    video_file= last_video.videofile
    reqs = last_video.reqs
    reqs = reqs.split()
    reqs = {'pushup': int(reqs[0]), 'situp': int(reqs[1]), 'pull ups': int(reqs[2]), 'squat': int(reqs[3])}
    return main(video_file, reqs)
def challenge(request):
    if request.method == 'POST':
        form= VideoForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            x = inference()
            return finish(request, x)
            # return render(request, '')
    exercises = [[["pushup", 10], ["situp", 10]], [["pull ups", 3], ["squat", 10]], [["squat", 15], ["pushup", 20]], [["situp", 15], ["pushup", 15]], [["situp", 5], ["squat", 5]]]
    exercises = exercises[random.randint(0, 4)]
    form= VideoForm(None, request.FILES or None)
    if form.is_valid():
        form.save()
    reqs = [0, 0, 0, 0]
    if(exercises[0][0] == "pushup"):
        reqs[0] = exercises[0][1]
    elif(exercises[0][0] == "situp"):
        reqs[1] = exercises[0][1]
    elif(exercises[0][0] == "pull ups"):
        reqs[2] = exercises[0][1]
    elif(exercises[0][0] == "squat"):
        reqs[3] = exercises[0][1]
    
    if(exercises[1][0] == "pushup"):
        reqs[0] = exercises[1][1]
    elif(exercises[1][0] == "situp"):
        reqs[1] = exercises[1][1]
    elif(exercises[1][0] == "pull ups"):
        reqs[2] = exercises[1][1]
    elif(exercises[1][0] == "squat"):
        reqs[3] = exercises[1][1]
    req = ""
    req += str(reqs[0]) + " "
    req += str(reqs[1]) + " "
    req += str(reqs[2]) + " "
    req += str(reqs[3])
    context= {  'exercises': exercises,
                'form': form,
                'challenge_num': 9,
                'reqs': req
              }
    
      
    return render(request, 'challenge.html', context=context)
    
def subscription(request):
        
    context= {

    }    
    return render(request, 'subscription.html', context=context)

def shop(request):
    items = [{"link":"heart.png", "cost":500, "name":"Skip Challenge"}, {"link":"dollar.png", "cost":5000, "name":"1 week subscription"}, {"link":"amazon.png", "cost":8000, "name":"Amazon 10$ gift card"}]
    context={
        'items': items
    }
    return render(request, 'shop.html', context=context)

def finish(request, result):
    success = result

    context={
        'success': success,
        'reps': result,
        'challenge_num': 9,
    }
    return render(request, 'finish.html', context=context)