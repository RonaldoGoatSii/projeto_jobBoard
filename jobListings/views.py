from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Choice, JobListing


class IndexView(generic.ListView):
    template_name = "jobListings/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published Jobs."""
        return JobListing.objects.order_by("-pub_date")[:5]



def listing(request, job):
    return 