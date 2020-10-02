from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry, Sent
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.http import HttpResponse, Http404
from .forms import EntryForm

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


def index(request):
    return render(request, "reg_app/index.html")


def entry(request):
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


def Entry_detail(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    return render(request, "reg_app/entry_detail.html", {"entry": entry})


def Sent(request):
    cr_usr = request.user
    sented = Entry.objects.filter(user=cr_usr.id)
    return render(request, "reg_app/sent.html", {"sented": sented})


# CRUD views

def Parent(request):
    """[Parent View]

    Description:
        Hole all add, create, delete views on it
    """
    return render(request, "reg_app/parent.html")


def create_entry(request):
    cr_usr = request.user
    cr_usr = cr_usr.id
    entry = Entry(user=request.user,
                  date_responded=request.POST["date_responded"],
                  subject=request.POST["subject"],
                  sender=request.POST["sender"],
                  files=request.POST.get("files"),
                  num_of_file=request.POST["num_of_file"],
                  date_of_file=request.POST["date_of_file"],
                  date_recived=request.POST["date_recived"]
                  )
    entry.save()
    return redirect("/entry")


def edit_entry(request, entry_id):
    entry_to_edit = get_object_or_404(Entry, id=entry_id)
    return render(request, 'reg_app/edit_entry.html', {'entry_to_edit': entry_to_edit})


def update_entry(request, entry_id):
    entry_to_update = get_object_or_404(Entry, id=entry_id)
    entry_to_update.user = request.user
    entry_to_update.date_responded = request.POST["date_responded"]
    entry_to_update.subject = request.POST["subject"]
    entry_to_update.sender = request.POST["sender"]
    entry_to_update.files = request.POST.get("files")
    entry_to_update.num_of_file = request.POST["num_of_file"]
    entry_to_update.date_of_file = request.POST["date_of_file"]
    entry_to_update.date_recived = request.POST["date_recived"]
    entry_to_update.save()
    return redirect("/entry")


def delete_entry(request, entry_id):
    entry_to_delete = get_object_or_404(Entry, id=entry_id)
    entry_to_delete.delete()
    return redirect('/')

# end CRUD...


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
