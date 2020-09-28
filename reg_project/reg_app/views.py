from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry, Sent
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse, Http404
from reg_app.forms import EntryForm

# def Login(request):
#   username = request.POST.get("username")
#  password = request.POST.get("password")
# user = authenticate(request, username=username, password=password)
# if user is not None:
#   login(request, user)
#  return HttpResponse("/entry")
# else:
#   print("User Not identified ")
#  return render(request, 'reg_app/login.html', {"user": user})


@login_required
def index(request):
    return render(request, "reg_app/index.html")


@login_required
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
    # context_object_name = 'entries'
    # model = Entry
    # template_name = "reg_app/entry.html"

    return render(request, "reg_app/entry.html", {"entries": entries})


@login_required
def Entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    return render(request, "reg_app/entry_detail.html", {"entry": entry})


@login_required
def Sent(request):
    cr_usr = request.user
    sented = Entry.objects.filter(user=cr_usr.id)
    return render(request, "reg_app/sent.html", {"sented": sented})


def add_entry(request):
    cr_usr = request.user
    if request.POST:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('/entry')
            except:
                pass
        else:
            print(form.errors)
    else:
        form = EntryForm()
    return render(request, 'reg_app/add_entry.html', {'form': form, 'cr_usr': cr_usr})


def edit_entry(request, entry_id):
    entry_to_edit = get_object_or_404(Entry, id=entry_id)
    return render(request, 'reg_app/edit_entry.html', {'entry_to_edit': entry_to_edit})


def update_entry(request, entry_id):
    entry_to_update = get_object_or_404(Entry, id=entry_id)
    form = EntryForm(request.POST, instance=entry_to_update)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'reg_app/edit_entry.html', {'entry_to_update': entry_to_update})


def delete_entry(request, entry_id):
    entry_to_delete = get_object_or_404(Entry, id=entry_id)
    entry_to_delete.delete()
    return redirect('/')
