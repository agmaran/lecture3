from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

# Create your views here.


def index(request):
    if "tasks" not in request.session:  # Is it already a list of tasks in this session
        # If there is not a list of tasks, I create it as an empty list
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })


def add(request):
    if request.method == "POST":  # Checks if the request method is POST
        # We take all the data submitted and save it in the form variable
        form = NewTaskForm(request.POST)
        if form.is_valid():  # We check if the data submitted is valid
            task = form.cleaned_data["task"]  # We get the task from the form
            # We add the task to the list of tasks
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:  # If the form is not valid
            return render(request, "tasks/add.html", {  # We render the add.html file
                "form": form  # We pass in the form they submitted so they can see the error in the data submitted
            })
    return render(request, "tasks/add.html", {  # If the request method is not POST we just render an empty form
        "form": NewTaskForm()
    })
