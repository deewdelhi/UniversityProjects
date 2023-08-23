import unittest
from domain.domain import Book, Client, Rental
from repository.repository import RepositoryBook
from repository.repository import RepositoryClient
from repository.repository import RepositoryRental
from services.services import BookServices
from services.services import ClientServices
from services.services import RentalServices



class TestBookService(unittest.TestCase):
    def setUp(self) -> None:        
        self.book_services = BookServices(RepositoryBook())
        self.book_services.add_new_book(2,"ion", "rebreanu")
        return super().setUp()

    def test__add_new_book__list_one_element__list_two_elements(self):
        self.book_services.add_new_book(1,"mara", "slavici")
        self.assertEqual(len(self.book_services.book_repo.book_list), 2)

    def test__remove_book__list_one_element__list_zero_elemts(self):
        self.book_services.remove_book(2)
        self.assertEqual(len(self.book_services.book_repo.book_list), 0)

    def test__update_book_by_id__item_with_id__item_updated(self):
        self.book_services.update_book_by_id(2,"it","king")
        self.assertEqual(self.book_services.book_repo.__getitem__(2).title, "it" )
        self.assertEqual(self.book_services.book_repo.__getitem__(2).author, "king" )



class TestCLientService(unittest.TestCase):
    def setUp(self) -> None:
        self.client_services = ClientServices(RepositoryClient())
        self.client_services.add_new_client(1,"mirel")
        return super().setUp()

    def test__add_new_client__list_one_element__list_two_elements(self):
        self.client_services.add_new_client(2,"ionel")
        self.assertEqual(len(self.client_services.client_repo.list_clients), 2)

    def test__remove_client__list_one_element__list_zero_elemts(self):
        self.client_services.remove_client(1)
        self.assertEqual(len(self.client_services.client_repo.list_clients), 0)

    def test__update_client_by_id__item_with_id__item_updated(self):
        self.client_services.update_client_by_id(1, "mara")
        self.assertEqual( self.client_services.client_repo.__getitem__(1).name, "mara")




class TestRentalService(unittest.TestCase):
    def setUp(self) -> None:
        self.rental_service = RentalServices(RepositoryRental())
        self.rental_service.add_new_rental("frodo", 2,2,2,2,2,2000,[0,0,0])
        return super().setUp()


    def test__add_new_rental__list_one_element__list_two_elements(self):
        self.rental_service.add_new_rental("arthur", 1,1,1,1,1,2000,[0,0,0])
        self.assertEqual( len(self.rental_service.rental_repo.rental_list), 2)


    def test__update_rental_by_id__item_with_id__item_updated(self):
        self.rental_service.update_rental_by_id(2,4,4,4444)
        self.assertEqual(self.rental_service.rental_repo.__getitem__(2).returned_date,  [4,4,4444]) 
        
    

if __name__ == '__main__':
    unittest.main()