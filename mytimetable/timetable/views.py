from django.shortcuts import render

def timetable(request):
    return render (request,"timetable/table.html")

def web(request):
    return render(request,"timetable/web.html")

def responsive(request):
    return render(request,"timetable/responsive.html")