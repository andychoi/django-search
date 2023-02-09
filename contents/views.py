from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.decorators.cache import cache_page

from .models import Content


@method_decorator(cache_page(60 * 5), name="dispatch")
class ContentList(ListView):
    model = Content
    context_object_name = "contents"
    template_name = "content.html"


# class SearchResultsList(ListView):
#     model = Content
#     context_object_name = "contents"
#     template_name = "search.html"


# Q objects
# class SearchResultsList(ListView):
#     model = Content
#     context_object_name = "contents"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Content.objects.filter(
#             Q(name__icontains=query) | Q(content__icontains=query)
#         )


# Single Field Search
# class SearchResultsList(ListView):
#     model = Content
#     context_object_name = "contents"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Content.objects.filter(content__search=query)


# Multi Field Search
# class SearchResultsList(ListView):
#     model = Content
#     context_object_name = "contents"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Content.objects.annotate(search=SearchVector("title", "content")).filter(
#             search=query
#         )


# Stemming and Ranking
# class SearchResultsList(ListView):
#     model = Content
#     context_object_name = "contents"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         search_vector = SearchVector("title", "content")
#         search_query = SearchQuery(query)
#         return (
#             Content.objects.annotate(
#                 search=search_vector, rank=SearchRank(search_vector, search_query)
#             )
#             .filter(search=search_query)
#             .order_by("-rank")
#         )


# Weights
# class SearchResultsList(ListView):
#     model = Content
#     context_object_name = "contents"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         search_vector = SearchVector("title", weight="B") + SearchVector(
#             "content", weight="A"
#         )
#         search_query = SearchQuery(query)
#         return (
#             Content.objects.annotate(rank=SearchRank(search_vector, search_query))
#             .filter(rank__gte=0.3)
#             .order_by("-rank")
#         )


# Preview
class HeadlineSearchResultsList(ListView):
    model = Content
    context_object_name = "contents"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        search_vector = SearchVector("title", "content")
        search_query = SearchQuery(query)
        search_headline = SearchHeadline("content", search_query, start_sel='<mark>', stop_sel='</mark>')

        # return Content.objects.annotate(search_headline)
                
        return Content.objects.annotate(
            search=search_vector,
            rank=SearchRank(search_vector, search_query)
        ).annotate(headline=search_headline).filter(search=search_query).order_by("-rank")


# SearchVectorField
class SearchResultsList(ListView):
    model = Content
    context_object_name = "contents"
    template_name = "search.html"

    def get_queryset(self):
        
        Content.objects.update(search_vector=SearchVector('content'))

        query = self.request.GET.get("q")
        return Content.objects.filter(search_vector=query)
