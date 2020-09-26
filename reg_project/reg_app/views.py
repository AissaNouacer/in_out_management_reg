from django.shortcuts import render
from .models import Entry, Sent
from django.views.generic import ListView, DetailView


def index(request):
    return render(request, "reg_app/index.html")


def EnteryListView(request):
    """[Entry view]

    Args:
        request ([type]): [description]

    Returns:
        [request, tamplate_name, context]: [It return list of entry for specific user]
    """
    # get_current_user from request
    cr_usr = request.user
    entries = Entry.objects.filter(user=cr_usr.id)
    #context_object_name = 'entries'
    #model = Entry
    #template_name = "reg_app/entry.html"

    return render(request, "reg_app/entry.html", {"entries": entries})
