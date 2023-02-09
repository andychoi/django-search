from django.urls import path

from .views import ContentList, SearchResultsList

urlpatterns = [
    path("", ContentList.as_view(), name="all_contents"),
    path("search/", SearchResultsList.as_view(), name="search_results"),
]
