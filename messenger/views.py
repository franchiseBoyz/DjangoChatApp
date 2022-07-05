from django.shortcuts import render

# Creating our views
def home_screen_view(request):
    context = {}
    return render(request, "messenger/home.html", context)
