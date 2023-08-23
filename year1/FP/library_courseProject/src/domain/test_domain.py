import unittest
from domain import Book, Client, Rental



class TestBook(unittest.TestCase):
  

    def setUp(self):
        self.book_1 = Book(1, "the shining", "stephen king")
        self.book_2 = Book(2, "Six of Crows", "Leigh Bardugo")
        
    def test_make_list(self):
        self.assertEqual(self.book_1.make_list(),  [1, "the shining", "stephen king"] )

    def test__id__valid_value__expected_id(self):
        self.assertEqual(self.book_1.id , 1)

    def test__title__valid_value__expected_title(self):
        self.assertEqual(self.book_1.title ,  "the shining")

    def test__author__valid_value__expected_author(self):
        self.assertEqual(self.book_1.author , "stephen king")

    def test__to_string__valid_value__turn_into_string(self):
        self.assertEqual(self.book_1.to_string(), "Book id: " + str(1) + "|  Book title: " + "the shining" + "|  Book author : " + "stephen king"  + "\n" )
    



class TestClient(unittest.TestCase):


    def setUp(self) -> None:
        self.client = Client(12, "Robert")
        return super().setUp()

    def test_make_list(self):
        self.assertEqual(self.client.make_list(),  [12, "Robert"] )

    def test__id__valid_value__expected_id(self):
        self.assertEqual(self.client.id , 12)

    def test__name__valid_value__expected_name(self):
        self.assertEqual(self.client.name ,  "Robert")

    def test__to_string__valid_value__turn_into_string(self):
        self.assertEqual(self.client.to_string(),"Client id: " + str(12) + "  Client name: " + "Robert" + "\n")
    
    



class TestRental(unittest.TestCase):


    def setUp(self) -> None:
        self.rental = Rental(1,1,1,[1,2,2000], [10,2,2000])
        return super().setUp()

    def test__rental_id__valid_value__expected_id(self):
        self.assertEqual(self.rental.rental_id, 1)

    def test__rental_book_id__valid_value__expected_id(self):
        self.assertEqual(self.rental.rental_book_id, 1)

    def test__rental_client_id__valid_value__expected_id(self):
        self.assertEqual(self.rental.rental_client_id, 1)

    def test__rented_date__valid_value__expected_rent_date(self):
        self.assertEqual( self.rental.rented_date, [1,2,2000])

    def test__returned_date__valid_value__expected_return_date(self):
        self.assertEqual(self.rental.returned_date, [10,2,2000])

    def test__set_returned_date__valid_item__updated_return_date(self):
        self.rental.set_returned_date([22,12,2001])
        self.assertEqual(self.rental.returned_date, [22,12,2001])

    def test__to_string__valid_value__turn_into_string(self):
        self.assertEqual( self.rental.to_string(),"Rental id: " + str(1) + "  Book id: " + str(1) + "  Client id: " + str(1) + \
            "  Rented date: " + str([1,2,2000]) + "  Returned date: " + str([10,2,2000]) + "\n" )




if __name__ == '__main__':
    unittest.main()
