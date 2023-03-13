from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Book


    
class BookListView(ListView):
    model = Book
    template_name = 'story/index.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class UploadBookView(CreateView):
    model = Book
    fields = ('site_name','site_url','site_con','site_cover')
    success_url = reverse_lazy('story:index')
    template_name = 'story/create.html'

def delete_book(req,pk):
    if req.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
        return redirect('story:index')
# Create your views here.
