from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    # register a new user
    if request.method != 'POST':
        form = UserCreationForm() # display blank registration form
    else:
        form = UserCreationForm(data=request.POST) # process completed form
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('MainApp:index')
   
    context = {'form': form}
    return render(request, 'registration/register.html', context)