from django.shortcuts import render

def timetable(request):
    return render (request,"timetable/table.html")