from django.shortcuts import render
import copy
import json
import os
from shutil import copyfile

# Create your views here.
names = {"explorers":[],"challengers":[],"voyagers":[],"pioneers":[],"prefect":[]}
align = 0
lock = 0
electorate = open("allnames.csv","r").readlines()
voters={"explorers": {}, "pioneers":{}, "voyagers":{}, "challengers":{}, "prefect":{}}

G_CompletedVoters = set()	# <- Nikhil Idiculla's noble contribution: a single line.


for i in range(1,len(electorate)):
	a = electorate[i].split(",")
	if a[2] == "":
		voters["explorers"][a[1]] = 0
		voters["pioneers"][a[1]] = 0
		voters["voyagers"][a[1]] = 0
		voters["challengers"][a[1]] = 0
	elif a[2] == "C":
		voters["challengers"][a[1]] = 0
	elif a[2] == "E":
		voters["explorers"][a[1]] = 0
	elif a[2] == "V":
		voters["voyagers"][a[1]] = 0
	elif a[2] == "P":
		voters["pioneers"][a[1]] = 0

path = os.path.dirname(os.path.abspath(__file__)) + "/static/image/"
savepath = os.path.dirname(os.path.abspath(__file__)) + "/../save.txt"

def index(request):
    return render(request, 'vote/main.html', {})

def loadsave(request):
    global names
    names = json.load(open(savepath))
    print(names)
    return render(request, 'vote/main.html', {})

def choose(request):
    house = request.GET.get("house")
    copy_house = copy.deepcopy(voters[house])
    sorted_names = sorted(copy_house)
    
    return render(request, 'vote/choose.html', {'voters': sorted_names, 'house': house, 'completed_voters': G_CompletedVoters})

def voter(request):
    person = request.GET.get("voter")
    house = request.GET.get("house")

    G_CompletedVoters.add(person)
    del voters[house][person]
	
    global lock
    lock += 1
    return render(request, 'vote/voter.html', {'house': house, 'person': person})

def votepage(request):
    house = request.GET.get("house")
    return render(request, 'vote/vote.html', {'names': names[house], 'align': align})

def count(request):
    global lock

    house = request.GET.get("house")
    name = request.GET.get("name")

    if lock == 0:
        return render(request, 'vote/fail.html', {'house': house})

    for i in names[house]:
        if i["name"] == name:
            i["count"] += 1
            json.dump(names, open("save.txt",'w'))
    lock -= 1
    return render(request, 'vote/refresh.html', {'house': house})

def results(request):
    house = request.GET.get("house")
    return render(request, 'vote/results.html', {'names': names[house]})

# Saves the files with their names in files.
def settings(request):
    if request.method == "POST":
        print(request.POST)
        house = ""
        number = ""
        if "explorers" in request.POST:
            house = "explorers"
        elif "challengers" in request.POST:
            house = "challengers"
        elif "voyagers" in request.POST:
            house = "voyagers"
        elif "pioneers" in request.POST:
            house = "pioneers"
        else:
            house = "prefect"

        if "2s" in request.POST:
            number = "2"
        else:
            number = "3"

        global align
        if number == "3":
            align = 2
        else:
            align = 10

        for i in range(1,int(number)+1):
            info = {}

            name = request.POST.get("name"+str(i))
            imagepath = request.POST.get("image" + str(i))
            newpath = path + house + "image" + str(i)
            copyfile(imagepath, newpath)
            count = 0
            info["name"] = name
            info["image"] = "image/" + house + "image" + str(i)
            info["count"] = count
            info["house"] = house
            names[house].append(info)

            
    return render(request, 'vote/settings.html', {})
