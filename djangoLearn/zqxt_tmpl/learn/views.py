from django.shortcuts import render

# Create your views here.


def home(request):
    string = u"我在自强学堂学习Django，用它来建网站"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    return render(request, 'home.html', {'string': string, 'TutorialList': TutorialList})