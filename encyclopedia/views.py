from django.shortcuts import render
from django import forms

from . import util
encyclopedia = []

class NewTopicForm(forms.Form):
    pedia = forms.CharField(label="Enter New Page name")

def index(request):
    if "entries" not in request.session:
        request.session["entries"] = []
    return render(request, "encyclopedia/index.html", {
        "encyclopedia": encyclopedia
    })

def add(request):
    if request.method == "POST":
        form = NewTopicForm(request.POST)
        if form.is_valid():
            pedia = form.cleaned_data["pedia"]
            encyclopedia.append(pedia)
        else:
            return render(request, "encyclopedia/add.html",{
                "form":form
            })
    return render(request, "encyclopedia/add.html", {
        "form" : NewTopicForm()
    })

