from django.shortcuts import render
from django.views import generic
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, User

from .models import Book, Author, BookInstance, Boutique

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            reverse_lazy('books')
    else:
        f = UserCreationForm()

    return render(request, 'catalog/register.html', {'form': f})

def user(request):
    return render(
        request,
        'catalog/user_detail.html',
    )

def index(request):
    # Generate counts of some of the main objects
    num_books=Book.objects.all().count()
    num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    num_authors=Author.objects.count()  # The 'all()' is implied by default.
    num_shops=Boutique.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_books':num_books,
                 'num_instances':num_instances,
                 'num_instances_available':num_instances_available,
                 'num_authors':num_authors, 
                 'num_visits':num_visits, 
                 'num_shops':num_shops,
                 'boutique':Boutique.objects.all(),
                 'book': Book.objects.all(),
                 'author': Author.objects.all(),
                }
    )
    
    
class BookListView(generic.ListView):
    model = Book    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        page = self.request.GET.get('page')
        if query :
            return Book.objects.filter(title__icontains=query)
        elif page:
            return Book.objects.filter(title__startswith=page)
        else:
            return Book.objects.all()
    
class BookDetailView(generic.DetailView):
    model = Book
    
def book_detail_view(request,pk):    
    try:
        book_id=Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
        
    return render(
        request,
        'catalog/book_detail.html',
        context={'book':book_id,}
    )
    
class BoutiqueListView(generic.ListView):
    model = Boutique
    def get_context_data(self, **kwargs):
        context = super(BoutiqueListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')        
        page = self.request.GET.get('page')
        if query :
            return Boutique.objects.filter(name__icontains=query)
        elif page:
            return Boutique.objects.filter(name__startswith=page)
        else:
            return Boutique.objects.all()
        
class BoutiqueDetailView(generic.DetailView):
    model = Boutique
    
def boutique_detail_view(request,pk):    
    try:
        boutique_id=Boutique.objects.get(pk=pk)
    except Boutique.DoesNotExist:
        raise Http404("Book does not exist")
        
    return render(
        request,
        'catalog/boutique_detail.html',
        context={'boutique':boutique_id,}
    )

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')
    
class AuthorListView(generic.ListView):
    model = Author
    def get_context_data(self, **kwargs):
        context = super(AuthorListView, self).get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        page = self.request.GET.get('page')
        if query :
            return Author.objects.filter(first_name__icontains=query)
        elif page:
            return Author.objects.filter(first_name__startswith=page)
        else:
            return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author
    
def author_detail_view(request,pk):
    try:
        author_id=Author.objects.get(pk=pk)
        book = Book.objects.all()
    except Author.DoesNotExist:
        raise Http404("Author does not exist")
    
    return render(
        request,
        'catalog/author_detail.html',
        context={'author':author_id,
                 'book': book}
    )
    
########Creating view to manage User informations#########
class UserUpdate(UpdateView):
    model = User
    fields =['username', 'first_name','last_name', 'email']
    template_name = 'catalog/user_form.html'
    success_url = reverse_lazy('user')
    
    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user

########Creating view to manage Authors#########
class AuthorCreate(CreateView) :
    model = Author
    fields = '__all__'
    initial = {'date_of_death':'12/10/2016', 'date_of_birth':'12/10/2016'} #dateformat = mm/dd/yyyy
    
class AuthorUpdate(UpdateView) :
    model = Author
    fields = ['first_name','last_name','date_of_birth','date_of_death']
    
class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('authors')

########Creating view to manage Books#########
class BookCreate(CreateView) :
    model = Book
    fields = '__all__'
    
class BookUpdate(UpdateView) :
    model = Book
    fields = ['Title','Author','Summary','ISBN','Genre']
    
class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books')
    
########Creating view to manage Books#########
class BoutiqueCreate(CreateView) :
    model = Boutique
    fields = '__all__'
    
class BoutiqueUpdate(UpdateView) :
    model = Boutique
    
class BoutiqueDelete(DeleteView):
    model = Boutique
    success_url = reverse_lazy('boutiques')

def search(request):
    return render(request, 'catalog/search.html', context = {
                    'book' : Book.objects.filter(title__icontains=request.GET.get('q')), 
                    'author' : Author.objects.filter(first_name__icontains=request.GET.get('q')),
                    'boutique' : Boutique.objects.filter(name__icontains=request.GET.get('q'))
                    })
