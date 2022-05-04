from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):

    class Meta:
        model = Topic
        fields = ['text']
        labels = {'Text: ':''}
        
        
class EntryForm(forms.ModelForm):
    
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'Text: ':''}
        widgets = {'text':forms.Textarea(attrs ={'cols':80})} #altering the text form and makeing it 80 
