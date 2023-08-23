import unittest
from repository.repository import RepositoryBook, RepositoryClient,RepositoryRental
from domain.domain import Book, Client, Rental




class TestRepositoryBook(unittest.TestCase):


    def setUp(self) -> None:
        self.book_list = RepositoryBook()
        self.book_list.add(Book(1,"mara", "slavici"))
        return super().setUp()

    def test__add__list_one_element__list_two_elements(self):
        self.book_list.add(Book(2,"mara", "slavici"))
        self.assertEqual(len(self.book_list.book_list), 2)

    def test__delete__list_one_element__list_zero_elements(self):
        self.book_list.delete(1)
        self.assertEqual(len(self.book_list.book_list), 0)

    def test__update__item_with_id__list_updated(self):
        self.book_list.update(1, "the book","arthur" )
        self.assertEqual(self.book_list.__getitem__(1).title , "the book")
        self.assertEqual(self.book_list.__getitem__(1).author , "arthur")


class TestRepositoryClient(unittest.TestCase):
    def setUp(self) -> None:
        self.clients_list = RepositoryClient()
        self.clients_list.add(Client(1,"angelo"))
        return super().setUp()

    def test__add__list_one_element__list_two_elements(self):
        self.clients_list.add(Client(2, "mara"))
        self.assertEqual(len(self.clients_list.list_clients), 2)

    def test__delete__list_one_element__list_zero_elements(self):
        self.clients_list.delete(1)
        self.assertEqual(len(self.clients_list.list_clients), 0)

    def test__update__item_with_id__list_updated(self):
        self.clients_list.update(1,"ionel")
        self.assertEqual(self.clients_list.__getitem__(1).name, "ionel")


class TestRepositoryRental(unittest.TestCase):
    def setUp(self) -> None:
        self.rentals = RepositoryRental()
        self.rentals.add(Rental(2,2,2,[1,2,2000],[0,0,0]),1,"miron")
        
        return super().setUp()

    def test__add__list_one_element__list_two_elements(self):
        self.rentals.add(Rental(1,1,1,[1,2,2000],[0,0,0]),1,"miron")
        self.assertEqual(len(self.rentals.rental_list),2)

    # def test_update(self):
    #     self.rentals.update(2,[12,12,2000])
    #     self.assertEqual(self.rentals.__getitem__(2).returned_date, [12,12,2000] )

  








if __name__ == '__main__':
    unittest.main()
