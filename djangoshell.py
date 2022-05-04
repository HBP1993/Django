from html import entities
import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic

topics = Topic.objects.all()

for t in topics:
    print(t.id,' ', t) #id is an attribute of the topic 
    #because of the string method you do not need to do t.text, t is enough
  
t = Topic.objects.get(id=1) #t here is itself is an object 

print(t.text)
print(t.date_added) 

entries = t.entry_set.all() #entries.object.all will give you all the info


for e in entries:
    print(e) 
    
