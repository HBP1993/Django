
from django.shortcuts import render, redirect

from .forms import TopicForm, EntryForm

from .models import Topic, Entry

from django.contrib.auth.decorators import login_required

from django.http import Http404
# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html') #process the request and rendering a page in your browser 

@login_required

def topics(request):
    #topics = Topic.objects.order_by("date_added")
    topics = Topic.objects.filter(owner = request.user).order_by("date_added")
    context = {'topics': topics} #key you have to refer in html and value you need to define (above line)
    
    return render(request, 'MainApp/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id= topic_id)
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.all()
    
    context = {'topic': topic, 'entries': entries}
    
    return render(request, 'MainApp/topic.html', context)

'''topic will bring us individual topic page e.g. chess or mountain climbing but topics will bring to 
page for the all the topic; Topic (capital topic) here is the obejct or model'''
'''context - context is dictionary and passes infomration from view to template '''
'''topic and entries are object passes to web page '''
'''types of request: get receive information and post is click submit '''

@login_required
def new_topic(request):
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data = request.POST)
        
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            
            return redirect('MainApp:topics')
        
    context = {'form': form}
    return render(request, 'MainApp/new_topic.html', context)

@login_required
def new_entry(request, topic_id): #this is just an integer 
    topic = Topic.objects.get(id=topic_id)  #this is a topic object
    
    if topic.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = EntryForm()
        
    else:
        form = EntryForm (data = request.POST)
        
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('MainApp:topic', topic_id = topic_id)
        
    context = {'form': form, 'topic': topic}
    return render(request, 'MainApp/new_entry.html', context)
 
@login_required
def edit_entry(request, entry_id):
    entry =Entry.objects.get(id = entry_id)
    topic = entry.topic
    
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance = entry)
         
    else:
        form = EntryForm(instance = entry, data = request.POST)
         
        if form.is_valid():
            form.save()
            return redirect ('MainApp:topic', topic_id = topic.id)
        
    context = {'form': form, 'topic': topic, 'entry': entry}
    return render(request, 'MainApp/edit_entry.html', context)  

     