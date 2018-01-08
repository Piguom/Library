from django.conf.urls import url

from . import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^books/$', views.BookListView.as_view(), name='books'),
        url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
        url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
        url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]

urlpatterns += [   
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [   
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete$', views.AuthorDelete.as_view(), name='author_delete'),
]

urlpatterns += [   
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete$', views.BookDelete.as_view(), name='book_delete'),
]

urlpatterns += [   
    url(r'^boutiques/$', views.BoutiqueListView.as_view(), name='boutiques'),
    url(r'^boutique/(?P<pk>\d+)$', views.BoutiqueDetailView.as_view(), name='boutique-detail'),
    url(r'^boutique/create/$', views.BoutiqueCreate.as_view(), name='boutique_create'),
    url(r'^boutique/(?P<pk>\d+)/update$', views.BoutiqueUpdate.as_view(), name='boutique_update'),
    url(r'^boutique/(?P<pk>\d+)/delete$', views.BoutiqueDelete.as_view(), name='boutique_delete'),
]


urlpatterns += [
    url(r'^register/$', views.register, name='register'),
    url(r'user/$', views.user, name='user'),
    url(r'^user/(?P<pk>\d+)/update$', views.UserUpdate.as_view(), name='user_update'),
    url(r'search/$', views.search, name='search'),
]

urlpatterns += [
        url(r'^cart/$', views.CartView.as_view(), name='cart'),
        url(r'^comparaison/$', views.comparaison, name='comparaison'),
]
