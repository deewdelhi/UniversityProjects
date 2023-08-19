
from django.urls import path
from .views import BookList,BookDetail, CustomerList,CustomerDetail
from .views import AuthorList, AuthorDetail,BooksWithAuthorsAsDetail
from .views import PublishingHouseList, PublishingHouseDetail,BooksByReleasingYear,BooksForPublishingHouse
from .views import BooksWithAuthorsList,AuthorsByAvgReleasingYearOfTheirBooks,PublishingHousesByTheNumberOfBooksTheyHave
urlpatterns = [
   path('book/',BookList.as_view()),
   path('book/<int:pk>/',BookDetail.as_view()),

   path('customer/',CustomerList.as_view()),
   path('customer/<int:pk>/',CustomerDetail.as_view()),

   path('author/',AuthorList.as_view()),
   path('author/<int:pk>/',AuthorDetail.as_view()),

   path('publishing-house/',PublishingHouseList.as_view()),
   path('publishing-house/<int:pk>/',PublishingHouseDetail.as_view()),
   path('publishing-house/<int:pk>/add-books/',BooksForPublishingHouse.as_view()),

   path('findbooks/', BooksByReleasingYear.as_view()),

   path('books-with-authors/', BooksWithAuthorsList.as_view()),
   path('books-with-authors/<int:pk>/', BooksWithAuthorsAsDetail.as_view()),

   path('authors-by-avg-releasing-year/', AuthorsByAvgReleasingYearOfTheirBooks.as_view()),
   # path('authors/avg-smth/', AuthorsByAvgReleasingYearOfTheirBooks.as_view()),
   path('publishing-houses/count-smth/', PublishingHousesByTheNumberOfBooksTheyHave.as_view()),


]

