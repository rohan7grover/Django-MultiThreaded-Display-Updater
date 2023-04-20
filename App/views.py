from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import time
import random as r
import threading

displays = {
    "D1" : 0,
    "D2" : 0,
    "D3" : 0,
    "D4" : 0,
    "D5" : 0,
    "D6" : 0
}

def display_data(request):
    return JsonResponse(displays)

def task(lb, ub, refreshTime, displayLocation):
    while (1):
        num = r.randint(lb, ub)
        displays[displayLocation] = num
        time.sleep(refreshTime)
    return

def index(request):

    t1 = threading.Thread(target=task, args=(10, 20, 10, "D1"))
    t2 = threading.Thread(target=task, args=(-10, 10, 20, "D2"))
    t3 = threading.Thread(target=task, args=(-100, 0, 8, "D3"))
    t4 = threading.Thread(target=task, args=(0, 20, 12, "D4"))
    t5 = threading.Thread(target=task, args=(-40, 40, 16, "D5"))
    t6 = threading.Thread(target=task, args=(100, 200, 14, "D6"))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    return render(request, "App/index.html", context=displays)
