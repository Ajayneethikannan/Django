from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from polls.forms  import UserLoginForm
from polls.models import Question,Choice
from django.views.decorators.csrf import ensure_csrf_cookie
from django.urls import reverse

# Create your views here.



def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/home.html',context)


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()

    else:
        form = UserCreationForm()
    return render(request, 'polls/signup.html', {'form': form})


@ensure_csrf_cookie
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    else:
        return render(request, 'polls/login.html')

def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html',{'question':question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',{'question': question})
    

@login_required(login_url='/polls/login')
def vote(request, question_id):
    if request.method == 'POST':
       question = get_object_or_404(Question, pk=question_id)
       try:
           selected_choice = question.choice_set.get(pk=request.POST['choice'])
       except(KeyError,Choice.DoesNotExist):
          return render(request,'polls.detail.html',{'question':question,'error_message':"You did not select a choice"})
       else:
           selected_choice.votes+=1
           selected_choice.save()
           return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
 
