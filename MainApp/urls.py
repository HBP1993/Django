from django.urls import path


from . import views 

app_name = 'MainApp'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.topic, name = 'topic'),
    path('new_topic/', views.new_topic, name = 'new_topic'),
    path("new_entry/<int:topic_id>/", views.new_entry, name ='new_entry'),
    path("edit_entry/<int:entry_id>/", views.edit_entry, name ='edit_entry')
]


#project url file is the parent file controls what app included, we  can list all url files 
#in master URL file you would like to use include 
#url py files seperates the file 

