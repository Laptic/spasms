import os
import sys

sys.path.append(os.path.abspath(os.path.join("..", "src")))

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .forms import InputModelForm,ExerciseForm,TweetRunForm
from spasmsMain import spasms_main, create_twitter_users
from django.contrib import messages


def spasms_index(request):
    return render(request, "spasms_index.html")


def index(request):
    return HttpResponse("Hello, world. You're at the polls index")


def thanks(request):
    return render(request, "thanks.html", {"messages":["Thank you for your submission!"]})

def get_exercise_form(request):
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            today = str(datetime.now()).split()[0]
            create_twitter_users(
                data['name'],
                data['num_users'],
                data['percent_female'],
                today,
                today
            )
            form.save()
            #redirect to new URL
            return HttpResponseRedirect("/thanks")
            # if a GET (or any other method) we'll create a blank form
    else:
        form = ExerciseForm()
    return render(request, "exercise_form.html", {"form": form})

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = InputModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = form.cleaned_data
            start_date = str(data["start_date"])
            end_date = str(data["end_date"])
            nameOfJsonFile = data["json_output"]
            outputFileLoc = os.path.join("../../output", nameOfJsonFile)
            absOutputFileLoc = os.path.abspath(outputFileLoc)
            messages.success(request, absOutputFileLoc)
            # print(data)
            spasms_main(
                data["group_name"],
                data["topic_name"],
                data["num_users"],
                data["percent_female"],
                data["twitter_or_facebook"],
                data["num_posts"],
                data["sentiment"],
                data["topic_noun"],
                start_date,
                end_date,
                data["json_output"],
            )
            # redirect to new url
            return HttpResponseRedirect("/thanks/")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputModelForm()
    return render(request, "form_template.html", {"form": form})
