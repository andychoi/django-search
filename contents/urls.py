from django.urls import path

from .views import ContentList, SearchResultsList, HeadlineSearchResultsList

urlpatterns = [
    path("", ContentList.as_view(), name="all_contents"),
    # path("search/", SearchResultsList.as_view(), name="search_results"),
    path("search-headline/", HeadlineSearchResultsList.as_view(), name="headline_search_results"),
]
