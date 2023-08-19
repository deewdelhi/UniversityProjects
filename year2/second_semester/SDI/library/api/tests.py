from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from api.models import Book, PublishingHouse, Author,BookWithAuthors


class BookByYearTest(APITestCase):
    def setUp(self):

        self.pHouse = PublishingHouse.objects.create (id = 1,name = "fortest",headquarters = "fortest",founding_year = 2000)
        self.book1 = Book.objects.create(id = 1,title='Book 1',publishing_house = self.pHouse,description ="aaaaaa", releasing_year=2000)
        self.book2 = Book.objects.create(id = 2,title='Book 2', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2005)
        self.book3 = Book.objects.create(id = 3,title='Book 3', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2010)



    def test_book_by_year(self):
        response = self.client.get('/api/findbooks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_book_by_year_no_result(self):
        response = self.client.get('/api/findbooks/?value=3000')
        self.assertEqual(response.status_code,  status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)





class PublishingHousesByTheNumberOfBooksTheyHaveTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.pHouse1 = PublishingHouse.objects.create (id = 1,name = "fortest1",headquarters = "fortest",founding_year = 2000)
        self.pHouse2 = PublishingHouse.objects.create (id = 2,name = "fortest2",headquarters = "fortest",founding_year = 2000)
       

        self.book1 = Book.objects.create(id = 1,title='Book 1',publishing_house = self.pHouse1,description ="aaaaaa", releasing_year=2000)
        self.book2 = Book.objects.create(id = 2,title='Book 2', publishing_house = self.pHouse2,description ="aaaaaa",releasing_year=2005)
        self.book3 = Book.objects.create(id = 3,title='Book 3', publishing_house = self.pHouse2,description ="aaaaaa",releasing_year=2010)


    def test_PublishingHousesByTheNumberOfBooksTheyHave(self):
        response = self.client.get('/api/publishing-houses/count-smth/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'fortest1')
        # self.assertEqual(response.data[0]['books'].len(), 1)

        self.assertEqual(response.data[1]['name'], 'fortest2')
        # self.assertEqual(response.data[0]['books'].len(), 2)



# class AuthorsByAvgReleasingYearOfTheirBooksTets(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#         self.author1 = Author.objects.create(
#             id=1, first_name='liviu',last_name = "rebreanu" ,nationality ="romanian", date_of_birth= 1885,preponderent_genre = "novels")
            
        
#         self.author2 = Author.objects.create(
#             id=2, first_name='george',last_name = "calinescu" ,nationality ="romanian", date_of_birth= 1900,preponderent_genre = "novels")
        

#         self.pHouse = PublishingHouse.objects.create (id = 1,name = "fortest",headquarters = "fortest",founding_year = 2000)
#         self.book1 = Book.objects.create(id = 1,title='Book 1',publishing_house = self.pHouse,description ="aaaaaa", releasing_year=2000)
#         self.book2 = Book.objects.create(id = 2,title='Book 2', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2005)
#         self.book3 = Book.objects.create(id = 3,title='Book 3', publishing_house = self.pHouse,description ="aaaaaa",releasing_year=2010)


#         self.relation1 = BookWithAuthors.objects.create(id = 1,book = self.book1, author = self.author1,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )
#         self.relation2 = BookWithAuthors.objects.create(id = 2,book = self.book1,author = self.author2,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )

#         self.relation3 = BookWithAuthors.objects.create(id = 3,book = self.book2,author = self.author1,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )
#         self.relation4 = BookWithAuthors.objects.create(id = 4,book = self.book3,author = self.author2,book_contribution = "sasasasa", author_additions = "sdkjhgfjsd" )

#     def test_AuthorsByAvgReleasingYearOfTheirBooks(self):
#         response = self.client.get('/api/authors-by-avg-releasing-year/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)
#         self.assertEqual(response.data[0]['first_name'], 'liviu')
#         self.assertEqual(response.data[0]['avg_releasing_year'], 2002.5)

#         self.assertEqual(response.data[1]['first_name'], 'george')
#         self.assertEqual(response.data[1]['avg_releasing_year'], 2005)




       
