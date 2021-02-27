from django.shortcuts import render,redirect
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from .form import Option
from .saved_contacts import send_to_saved
from .unsaved_contacts import whatsapp_login,send_to_unsaved,quits
import csv
from .models import Whatsapp_Numbers
# Create your views here.

def home_view(request):
    if request.method=="POST":
        choice=request.POST.get("option")
        text=request.POST.get("text")
        loc=request.POST.get("file_name")
        # location=f"media\{loc}.csv"
        #lst=[918962191644,918889210328]
        #lst1=[917980121239,917620330659,919898111783,918469199444,919913651467,919909967688,916359013131,917980121239,917620330659,919898111783,918469199444,919913651467,919909967688,916359013131,917980121239,917620330659,919898111783,918469199444,919913651467,919909967688,916359013131]
        #print(choice, text)
        # lst=read_file(location)
        lst=Whatsapp_Numbers.objects.all()
        # print(lst)
        if choice == "1":
            send_to_saved(lst,text)
            sleep(5)
            return redirect("Home")
        elif choice == "2":
            whatsapp_login()
            for number in lst:
                send_to_unsaved(number,text,1)
                sleep(2)
            quits()
            return redirect("Home")

    else:
        send=Option
        return render(request,"send\home.html",{"form":send})

def read_file(way):
    with open(way) as file:
        number=csv.reader(file)
        next(number)
        lst=[]
        for line in number:
            lst.append(line[0])
    return lst