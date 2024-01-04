from django.shortcuts import render
from app.models import *

# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()

        QLTO=Topic.objects.all()
        d={'QLTO':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html')

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'checkbox.html',d)