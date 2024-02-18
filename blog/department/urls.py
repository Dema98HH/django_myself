
from django.urls import path
from . import views


urlpatterns = [
    path("", views.ArticleListView.as_view(), name="departments"),
    path('<uuid:pk>', views.singular_record, name='department'),
]
