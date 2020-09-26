from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    """[entry model]

    Args:
        models ([enter]): [table of reciving files from other services & all it's attribute]

    Returns:
        [None]: [used just for regestring infos + file correspand ]
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_responded = models.DateField(auto_now=True)
    subject = models.CharField(max_length=150)
    sender = models.CharField(max_length=150)
    files = models.FileField(upload_to=None, max_length=100)
    num_of_file = models.IntegerField()
    date_of_file = models.DateField(auto_now=False, auto_now_add=False)
    date_recived = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        reterse("entry_detail", kwargs={"pk": self.pk})


class Sent(models.Model):
    """[sent model]

    Args:
        models ([sent]): [Table used for recored what office sent files and others]

    Returns:
        [None]: [return nothing it's just for manipulation ]
    """
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    files = models.FileField(upload_to=None, max_length=100)
    subject = models.CharField(max_length=150)
    sent_to = models.CharField(max_length=150)
    refrence = models.ForeignKey(
        Entry, on_delete=models.CASCADE)
    notes = models.CharField(max_length=350)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("sent_detail", kwargs={"pk": self.pk})
