from domain.domain import Book, Client, Rental
from repository.repository import RepositoryBook
from repository.repository import RepositoryClient
from repository.repository import RepositoryRental
from repository.repository import RepositoryBookException
from repository.repository import RepositoryClientException
from repository.repository import RepositoryRentalException



class BookServices:

    def __init__(self, book_repository:RepositoryBook):

        self.__book_repository = book_repository

    @property
    def book_repo(self):
        return self.__book_repository

    def get_all_books(self):
        list_books = []
        all_id = self.__book_repository.__getlist__()
        for id in all_id:
            list_books.append(self.__book_repository.__getitem__(id))

        return list_books

    def add_new_book(self,id, title, author):
        """
        function creates a new objeect in the class Book that will be added in the repository by the "add" function defined in the repository class
        :param id: integer, books id
        :param title: tring, books name
        :param author: string, authors name
        """        

        list_books = self.__book_repository.book_list
        try:
            if id in list_books:
                raise RepositoryBookException
        except:
            print("Book with Id " + str(id) + " already in repository")

        else:
            book = Book(id, title, author)
            self.__book_repository.add(book)

    def remove_book(self, id):
        """
        the function checks for the id of the book to be removed and that book is gooing to be deleted by de function "delete" defined in the book repository
        :param id: integer, the books id
        """        
        
        keys = list(self.__book_repository.__getlist__())  
        found_id = False
    

        for i in keys:

            if int(i) == int(id):

                self.__book_repository.delete(int(id))
                found_id = True
                break
        if found_id == False:

            print("The book with this id doesn't exist")

    def update_book_by_id(self,id,title , author):
        """
        the function checks for the id of the book you want to update and transmits the id and the new dates to the "update" function defined in the book repository that will do the actual update
        :param id:integer, the books id
        :param title: string, the books title
        :param author: string, the books author
        
        """        

        keys = list(self.__book_repository.__getlist__()) 
        found_id = False

        for i in keys:

            if int(i) == int(id):

                self.__book_repository.update(int(id),title, author)
                found_id = True
                break
        if found_id == False:
            print("The book with this id doesn't exist")

    # def to_string(self):           
    #     final_list = ""
    #     for id in self.__book_repository.__getlist__():
    #         final_list = final_list + self.__book_repository.__getitem__(id).to_string()
    #     return final_list

    def to_list(self):
        books_list = []
        for id in self.__book_repository.__getlist__():
            books_list.append(self.__book_repository.__getitem__(id).make_list())
        return books_list

    def check_valid_id_book(self,id):
        """
        checks if the id of the book was already introduced 
        :param id: integer, the id to look for
        :return: True if the id was found and False otherwise
        """        

        keys = list(self.__book_repository.__getlist__())  # a list with id s
        found_id = False
        for i in keys:

            if int(i) == int(id):

                
                found_id = True
                break
        
        return found_id
    def get_author(self,id):
        return self.__book_repository.__getauthor__(id)

    def get_book(self,id):
       
        book = self.__book_repository.__getitem__(id).make_list()
        return book



###########################################################################################################################
   


class ClientServices:    

    def __init__(self, client_repository:RepositoryClient):
        self.__client_repository = client_repository


    @property
    def client_repo(self):
        return self.__client_repository

    def add_new_client(self, id,name):
        """
        function creates a new objeect in the class Client that will be added in the repository by the "add" function defined in the repository 
        :param id: integer, clients id
        :param name: tring, clients name
        
        """    
        clients_list = self.__client_repository.list_clients
        try:
            if id in clients_list:
                raise RepositoryClientException
        except:       
            print("Client with Id " + str(id) + " already in repository")
        else:                   
            client = Client( id,name)
            self.__client_repository.add(client)

    def remove_client(self, id):
        """
        the function checks for the id of the client to be removed and that client is going to be deleted by de function "delete" defined in the client repository
        :param id: integer, the clients id
        """       
        
        keys = list(self.__client_repository.__getlist__())  # a list with id s
        found_id = False
    
        for i in keys:

            if int(i) == int(id):

                self.__client_repository.delete(int(id))
                found_id = True
                break
        if found_id == False:

            print("The client with this id doesn't exist")

    def update_client_by_id(self,id, name):
        """
        the function checks for the id of the client you want to update and transmits the id and the new dates to the "update" function defined in the client repository that will do the actual update
        :param id:integer, the clients id
        :param name: string, the clients name
        
        """

        keys = list(self.__client_repository.__getlist__())  # a list with id s
        found_id = False

        for i in keys:

            if int(i) == int(id):

                self.__client_repository.update(int(id),name)
                found_id = True
                break

        if found_id == False:
            print("The client with this id doesn't exist")

 

    def check_valid_id_client(self,id):
        """
        checks if the id of the client was already introduced 
        :param id: integer, the id to look for
        :return: True if the id was found and False otherwise
        """  
        keys = list(self.__client_repository.__getlist__())  
        found_id = False
        for i in keys:

            if int(i) == int(id):

                
                found_id = True
                break
        
        return found_id


    def to_list(self):

        clients_list = []
        for id in self.__client_repository.__getlist__():
            clients_list.append(self.__client_repository.__getitem__(id).make_list())

        return clients_list

    def get_client(self,id):
       
        client = self.__client_repository.__getitem__(id).make_list()
        return client


################################################################################################################################



class RentalServices:

    def __init__(self, rental_repository:RepositoryRental):
        self.__rental_repository = rental_repository


    @property
    def rental_repo(self):
        return self.__rental_repository
        
    def add_new_rental(self, author, rental_id,book_rental_id,  client_rental_id, rental_day, rental_month,rental_year, return_date ) :
        """
        function creates a new objeect in the class Client that will be added in the repository by the "add" function defined in the repository
        :param rental_id: integer, the rentals id
        :param book_rental_id: integer, the id of the book you want to rent
        :param client_rental_id: integer, the id of the client that wants to rent a book
        :param rental_date: string, the date when the book was rented
        :param return_date: string, the date when the biik was returned( at start is '0')
        """        
    
        rental_date = [rental_day, rental_month,rental_year]
        return_date = [return_date,return_date,return_date]
        rental = Rental( rental_id,book_rental_id,  client_rental_id, rental_date, return_date )

        rental_list = self.__rental_repository.rental_list
        rented_books_list = self.__rental_repository.rented_books
        
        
        if rental_id in rental_list.keys():
            print("Rental with Id " + str(rental_id) + " already in repository")

        else:
            if book_rental_id in rented_books_list:
                print("Book with Id " + str(book_rental_id) + " is already rented!")

        self.__rental_repository.add(rental, book_rental_id, author)
        self.__rental_repository.add_to_books(book_rental_id)
        self.__rental_repository.add_to_authors(author)


    def update_rental_by_id ( self , id,  return_day, return_month , return_year):
        """
        the function updates the returned date
        :param id: integer, the rentals id
        :param returned_date:string, new return date
        """        

        keys = list(self.__rental_repository.__getlist__())  # a list with id s
        found_id = False

        for i in keys:

            if int(i) == int(id):
                returned_date = [ return_day, return_month , return_year]
                self.__rental_repository.update(int(id),returned_date)
                found_id = True
                break

        if found_id == False:
            print("The rental with this id doesn't exist")

    
    # def to_string(self):
            
    #     final_string = ""
    #     for id in self.__rental_repository.__getlist__():
    #         final_string = final_string + self.__rental_repository.__getitem__(id).to_string()
    #     return final_string
    
    # def print_c_books(self):
    #     self.__rental_repository.print_contor_books()

    # def print_c_authors(self):
    #     self.__rental_repository.print_contor_authors()

    # def print_c_clients(self):
    #     self.__rental_repository.print_contor_clients()

    def sort_contor_books(self):

        books_contor = self.__rental_repository.books_counter
        book_contor_sorted = dict(sorted(books_contor.items(), key = lambda id: id[1], reverse = True))
        return book_contor_sorted

    def sort_contor_clients(self):
        clients_contor = self.__rental_repository.clients_counter
        client_contor_sorted = dict(sorted(clients_contor.items(), key = lambda id: id[1], reverse = True))
        return client_contor_sorted


    def sort_contor_authors(self):
        authors_contor = self.__rental_repository.authors_counter
        author_contor_sorted = dict(sorted(authors_contor.items(), key = lambda id: id[1], reverse = True))
        return author_contor_sorted

    def to_list(self):

        rentals_list = []
        for id in self.__rental_repository.__getlist__():
            rentals_list.append(self.__rental_repository.__getitem__(id).make_list())

        return rentals_list

    # def remove_or_upadate_book_case(self,book_id,book_author):

    #     self.__rental_repository.remove_or_update_book_case_repository(book_id,book_author)


    def undo_rental(self,author,book_rental_id):
        self.__rental_repository.undo_rental(author,book_rental_id)
        
    def undo_return(self,id):
        self.__rental_repository.undo_return(id)
