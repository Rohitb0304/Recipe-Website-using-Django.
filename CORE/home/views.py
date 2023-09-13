from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    peoples = [
        {'name': 'Rohit Bansode', 'age': 19},
        {'name': 'Rohan Sharma', 'age': 29},
        {'name': 'Amit Thakur', 'age': 40}
    ]

    vegetables = ['Pumpkin','Tomato', 'Cucumber']

    for people in peoples:
        print(people)

    return render(request, "index.html", context={'page':'Django Learning Part 1','peoples': peoples, 'vegetables':vegetables})

def about(request):
    context = {'page': 'About'}
    return render(request, "about.html", context)

def contact(request):
    context = {'page': 'contact'}
    return render(request, "contact.html",context)

def success_page(request):
    return HttpResponse("<h2>Heyy, This is a Success Page</h2>")