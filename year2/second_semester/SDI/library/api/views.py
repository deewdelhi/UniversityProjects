from rest_framework import generics,views,status
from django.db.models import Avg, Count, OuterRef, Subquery, Q, Case, When, \
    IntegerField, Exists

from .models import Book,Customer,PublishingHouse,Author
from .models import Book,Customer,PublishingHouse,Author,BookWithAuthors
from .serializers import BookSerializer_list, CustomerSerializer_list,PublishingHouseSerializer_list
from .serializers import BookSerializer, PublishingHouseSerializer, AuthorSerializer_list,BooksForPublishingHouseSerializer
from .serializers import BookWithAuthorsSerializer,PublishingHouseFilterSerializer,AuthorFilterSerializer,AuthorSerializer


from django.http import Http404


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render, get_object_or_404


########### customer list + detail
class CustomerList(generics.ListCreateAPIView):
    serializer_class = CustomerSerializer_list
    def get_queryset(self):
        queryset = Customer.objects.all()
        return queryset
    
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer_list
    queryset = Customer.objects.all()




########### author  list + detail
class AuthorList(generics.ListCreateAPIView):
    serializer_class = AuthorSerializer_list
    def get_queryset(self):
        queryset = Author.objects.all()
        return queryset
    

    
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()  




########### book list + detail
class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer_list

    def get_queryset(self):
        queryset = Book.objects.all()
        return queryset
    
## for the details in the publishing hoiuse not just the id##

# class BookList(generics.ListCreateAPIView):
#     serializer_class = BookSerializer

#     def get_queryset(self):
#         queryset = Book.objects.all()
#         publishing_house = self.request.query_params.get('publishing_house')
#         if  publishing_house is not None:
#             queryset  =queryset.filter(publishing_house = publishing_house)

#         return queryset
    

class BookDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()



########### publishing house list + detail
class PublishingHouseList(generics.ListCreateAPIView):
    serializer_class = PublishingHouseSerializer_list


    def get_queryset(self):
        queryset = PublishingHouse.objects.all()
        return queryset
    

class PublishingHouseDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublishingHouseSerializer
    queryset = PublishingHouse.objects.all()

    #don t remember what is this for
    #queryset = PublishingHouse.objects.values_list('')




########### book with authors list + detail
class BooksWithAuthorsList(generics.ListCreateAPIView):
    serializer_class = BookWithAuthorsSerializer

    def get_queryset(self):
        queryset = BookWithAuthors.objects.all()
        return queryset  
    

class BooksWithAuthorsAsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookWithAuthorsSerializer

    queryset = BookWithAuthors.objects.all()


#-------------------------------------------------------------------------------------A2-------------------------------------------------------------------------------------------


#filters books by the releasing year
class BooksByReleasingYear(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        value = self.request.GET.get('value', 0)
        if value is not None:
            queryset = queryset.filter(releasing_year__gt=value)        
        return queryset


# #filters books by the releasing year - UPDATE TRYOUT
# class BooksByReleasingYear(APIView):

#     def get(self, request, ry):
#         releasing_year = Book.objects.filter(releasing_year__gt=ry)
#         serializer = BookSerializer(releasing_year, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    


#-------------------------------------------------------------------------------------A3-------------------------------------------------------------------------------------------


# all authors ordered by the releasing year of their books -WORKS DON T TOUCH IT!!!
class AuthorsByAvgReleasingYearOfTheirBooks(generics.ListCreateAPIView ):
    serializer_class = AuthorFilterSerializer 

    def get_queryset(self):
        query = Author.objects\
            .annotate(avg_releasing_year = Avg('bookwithauthors__books__releasing_year'))\
            .order_by('avg_releasing_year')
        print(query.query)

        return query



# publishing houses by the number of books they have -WORKS DON T TOUCH IT!!!
class PublishingHousesByTheNumberOfBooksTheyHave( generics.ListAPIView):
    serializer_class =PublishingHouseFilterSerializer


    def get_queryset(self):
        
        query = PublishingHouse.objects\
            .annotate(avg_number = Count('books__releasing_year'))\
            .order_by('avg_number')
        
        print(query.query)

        return query


class BooksForPublishingHouse(views.APIView):
    def post ( self,request,pk):
        serializer = BooksForPublishingHouseSerializer(data = request.data,many = True)
        publishing_house = get_object_or_404(PublishingHouse, id = pk)
        serializer.context['publishing_house'] = publishing_house
        if serializer.is_valid():
            serializer.save(publishing_house = publishing_house, using = '')
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response (serializer.errors,status = status.HTTP_204_NO_CONTENT)
    







