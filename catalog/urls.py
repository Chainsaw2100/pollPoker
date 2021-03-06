from django.urls import path
from django.conf.urls import handler404
from . import views
handler404 = views.error404 
app_name = 'catalog'
urlpatterns = [
path('author/<int:pk>/vote/',views.vote,name='vote'),
path('votefailed/',views.votefail,name='votefailed'),
path('author/<int:pk>/updvote/',views.update_votes,name='update_votes'),
path('redir/',views.redir,name='redir'),
   path('author/<int:pk>/',
         views.AuthorDetailView.as_view(), name='author-detail'),
   
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),

 
]


urlpatterns += [
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge
]


# Add URLConf for librarian to renew a book.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]


# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('author/startgame/', views.StartGame.as_view(), name='start_game'),
]

# Add URLConf to create, update, and delete books
urlpatterns += [
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book_delete'),
]
