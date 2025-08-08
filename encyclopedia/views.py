from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse

from . import util
encyclopedia = []

class NewTopicForm(forms.Form):
    pedia = forms.CharField(label="Enter New Page name")

def index(request):
    return render(request, "encyclopedia/index.html", {
        "encyclopedia": encyclopedia
    })

def add(request):
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            pedia = form.cleaned_data["pedia"]
            encyclopedia.append(pedia)
            return HttpResponseRedirect(reverse("encyclopedia:index")) 
        else:
            return render(request, "encyclopedia/add.html",{
                "form":form
            })
    return render(request, "encyclopedia/add.html", {
        "form" : NewTopicForm()
    })

