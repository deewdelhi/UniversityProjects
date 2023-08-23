from enum import Enum

def add_book_handler(book_service,book_id, book_title, book_author):
    book_service.add_new_book(book_id,book_title, book_author )

def add_client_handler(client_service, client_id, client_name):
    client_service.add_new_client(client_id, client_name)

def remove_book_handler(book_service, book_id,book_title,book_author):
    book_service.remove_book(book_id)

def remove_client_handler(client_service, client_id,cllient_name):
    client_service.remove_client(client_id)

def update_book_information_handler(book_service, book_id, old_book_title, new_book_title,old_book_author, new_book_author):
    book_service.update_book_by_id(book_id, old_book_title, old_book_author)


def update_client_information_handler(client_service, client_id, new_client_name, old_client_name):
    client_service.update_client_by_id(client_id, old_client_name)

def rent_book_handler( rental_service, author, rental_id,book_id, client_id, rental_day,rental_month,rental_year ):
    returned_date = int(0)
    rental_service.add_new_rental(author, rental_id,book_id, client_id, rental_day,rental_month,rental_year,returned_date )

def return_book_handler( rental_service, return_id, return_day,return_month, return_year):
    rental_service.update_rental_by_id(return_id, return_day,return_month, return_year)



class RedoHandler(Enum):
    ADD_BOOK = add_book_handler
    ADD_CLIENT = add_client_handler
    REMOVE_BOOK = remove_book_handler
    REMOVE_CLIENT = remove_client_handler
    UPDATE_BOOK_INFORMATION = update_book_information_handler
    UPDATE_CLIENT_INFORMATION = update_client_information_handler
    RENT_BOOK = rent_book_handler
    RETURN_BOOK = return_book_handler    
