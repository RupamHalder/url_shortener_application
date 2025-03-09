from symbol import return_stmt

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from django.urls import reverse_lazy

from app_url_shortener.forms import UrlModelForm
from app_url_shortener.models import Url


class ShortenUrlCreateView(generic.CreateView):
    template_name = 'url/shorten-url.html'
    form_class = UrlModelForm
    success_url = reverse_lazy('shortened-url-list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ShortenUrlUpdateView(generic.UpdateView):
    template_name = 'url/shorten-url-edit.html'
    form_class = UrlModelForm
    success_url = reverse_lazy('shortened-url-list')

    def get_queryset(self):
        return Url.objects.all()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ShortenUrlListView(generic.ListView):
    model = Url
    template_name = "url/shorten-url-list.html"
    context_object_name = "shorten_url_list" # by default it takes "object_list"
    paginate_by = 10

    def get_queryset(self):
        return Url.objects.order_by("-created_at")


class ShortenUrlDetailView(generic.DetailView):
    model = Url
    template_name = 'url/shorten-url-detail.html'
    context_object_name = "shorten_url_detail"


class OpenUrlView(generic.RedirectView):
    permanent = True

    def get_redirect_url(self, *args, **kwargs):
        shorten_url = kwargs.get('shorten_url')
        original_url_data = get_object_or_404(Url, short_url=shorten_url)
        original_url = original_url_data.original_url
        return original_url
