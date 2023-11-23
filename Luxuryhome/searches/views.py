from django.shortcuts import render
from .models import SearchQuery
from base.models import BlogPost

def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user

    # Make sure to handle the case where query is None (optional)
    context = {'query': query}

    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        blog_list = BlogPost.objects.search(query=query)

        # Corrected the assignment of 'blog_list' to the context dictionary
        context['blog_list'] = blog_list

    return render(request, 'view.html', context)
