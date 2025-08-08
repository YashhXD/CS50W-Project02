from django.shortcuts import render
from django import forms

from . import util

class NewTopicForm(forms.Form):
    TopicName = forms.CharField(label="Enter New Page")
    TopicBody = forms.CharField(label="Enter about the topic")

def index(request):
    if "entries" not in request.session:
        request.session["entries"] = []
    return render(request, "encyclopedia/index.html", {
        "entries": request.session["entries"]
    })

def add(request):
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            TopicName = form.cleaned_data["TopicName"]
            entries.append(TopicName)
        else:
            return render(request, "entries/add.html",{
                "form":form
            })
    return render(request, "encyclopedia/add.html", {
        "form" : NewTopicForm()
    })

