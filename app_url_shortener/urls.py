from django.urls import path

from app_url_shortener.views import ShortenUrlListView, \
    OpenUrlView, ShortenUrlDetailView, ShortenUrlCreateView, ShortenUrlUpdateView

urlpatterns = [
    # path('', ShortenUrlView.as_view()),
    path('', ShortenUrlCreateView.as_view(), name='shorten-url'),
    path('list/', ShortenUrlListView.as_view(), name='shortened-url-list'),
    path('detail/<int:pk>/', ShortenUrlDetailView.as_view(), name='shorten-url-detail'),
    path('edit/<int:pk>', ShortenUrlUpdateView.as_view(), name='edit-shorten-url'),
    path('<path:shorten_url>/', OpenUrlView.as_view(), name='open-shorten-url')
]
