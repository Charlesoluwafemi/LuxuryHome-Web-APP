from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import BlogPost
from django.shortcuts import render
from django.utils import timezone
 # Corrected the import statement
from .forms import ContactForm, BlogPostModelForm # Added the import statement for BlogPostForm
from django.utils import timezone

def homepage(request):
    my_title = 'Hello there....'
    qs= BlogPost.objects.all()[:5]
    context = {'title': 'Welcome to LuxuryHome', 'blog_list':qs}
    return render(request, 'homepage.html', context)

# Other views remain the same

def about_page(request):
    return render(request, 'about.html', {'title': 'About'})

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data (send email, save to database, etc.)
            print(form.cleaned_data)
            # Optionally redirect to a success page
        else:
            # Form is not valid, render the page with errors
            return render(request, 'form.html', {'title': 'Contact us', 'form': form})
    else:
        form = ContactForm()

    context = {'title': 'Contact us', 'form': form}
    return render(request, 'form.html', context)

def blog_post_detail_page(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    template_name = 'blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    if request.user.is_authenticated:
       my_qs = BlogPost.objects.filter(user=request.user)
       qs = (qs | my_qs).distinct()
    context = {'object_list': qs}
    template_name = 'blog_post_list.html'
    return render(request, template_name, context)

from django.shortcuts import render, redirect

@staff_member_required
def blog_post_create_view(request):
    form = BlogPost(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('blog_post_create')  # Redirect to the same view to clear the form
    template_name = 'form.html'
    context = {'title': 'Create a Blog Post', 'form': form}
    return render(request, template_name, context)


def blog_post_update_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    
    if request.method == 'POST':
        form = BlogPostModelForm(request.POST or None, instance=obj)  # Use BlogPostModelForm here
        if form.is_valid():
            form.save()
    else:
        form = BlogPostModelForm(instance=obj)  # Use BlogPostModelForm here

    template_name = 'form.html'
    context = {'form': form, 'title': f'Update {obj.title}'}
    return render(request, template_name, context)


def blog_post_delete_view(request, post_id):
    obj = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        obj.delete()
    template_name = 'blog_post_delete.html'
    context = {'object': obj}
    return render(request, template_name, context)
