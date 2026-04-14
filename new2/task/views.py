from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

class NewTask(forms.Form):
    tasks = forms.CharField(label="new task")
    priority = forms.IntegerField(label="priority", min_value=0, max_value=10)

def task(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/task2.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTask(request.POST)
        if form.is_valid():
            task_item = form.cleaned_data["tasks"]
            request.session["tasks"] += [task_item]  # ✅ tasks → task_item
            return HttpResponseRedirect(reverse("task:task"))
        else:
            return render(request, "tasks/task.html", {
                "form": form
            })
    return render(request, "tasks/task.html", {
        "form": NewTask()
    })