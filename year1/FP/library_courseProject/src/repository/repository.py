


from domain.domain import Client
from domain.domain import Rental
from datetime import date
import pickle
import os.path

from domain.domain import Book


class RepositoryBookException(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass


class RepositoryClientException(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass


class RepositoryRentalException(Exception):
    """
    Writing (Exception) tells Python that RepoExc... is an Exception
    """
    pass

################################################################################################################################





class RepositoryBook:

    def __init__(self):
        self.__book_list = dict()
        

    def add(self,book):
        
        self.__book_list[book.id] = book
        
        
    @property
    def book_list(self):
        return self.__book_list

    

    def delete(self,id):
        """
        functions removes a book
        :param id: integer, the id of the book you want to remove

        """        
        self.__book_list.pop(id)

    def update(self,id,title,author):

        """
        function updates the book by changing the author ant the name of the book keeping th eid intact
        :param id:integer, the id of the book you want to update
        :param title: string, the ne title of the book
        :param author: string, the new author of the book
        """           
        self.__getitem__(id).set_title(title)
        self.__getitem__(id).set_author(author)
        

    def __getitem__(self, id):        
        return self.__book_list[id] 

    def __getlist__(self):
        return self.__book_list.keys()   

    def __getauthor__(self,id):
        authors = self.__getitem__(int(id)).author
        return authors

    def __setall__(self, data={}):
        self.__book_list = data
    
    def __getall__(self):
        return self.__book_list


class BookBinFileRepository(RepositoryBook):
    def __init__(self, filename):
        RepositoryBook.__init__(self)
        self._file_name = filename
        self._load_file()

    def _load_file(self):
        if os.path.getsize(self._file_name) > 0:
            file = open(self._file_name, "rb")  
            self.__setall__(pickle.load(file))
            file.close()

    def _save_file(self):

        file = open(self._file_name, "wb")
        pickle.dump(self.__getall__(), file)
        file.close()

    def add(self, entity):
       
        super(BookBinFileRepository, self).add(entity)
        self._save_file()
    
    def delete(self,id):
        super(BookBinFileRepository, self).delete(id)
        self._save_file()

    def update(self,id,title,author):
        super(BookBinFileRepository, self).update(id,title,author)
        self._save_file()

class BookTextFileRepository(RepositoryBook):
   

    def __init__(self, filename):
        RepositoryBook.__init__(self)
        self._file_name = filename
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in file.readlines():
            if line.find(',')> 0:
                _id, title, author = line.split(maxsplit=2, sep=',')
                super(BookTextFileRepository, self).add(Book(int(_id), title, author)) 
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt") 
        for b in self.__getlist__():
            book = self.__getitem__(b)
            file.write(str(book.id) + ',' + str(book.title) + ',' +str(book.author) + "\n")
        file.close()

    def add(self, entity):
      
        super(BookTextFileRepository, self).add(entity)
        self._save_file()

    def delete(self,id):
        super(BookTextFileRepository, self).delete(id)
        self._save_file()

    def update(self,id,title,author):
        super(BookTextFileRepository, self).update(id,title,author)
        self._save_file()


################################################################################################################################

class RepositoryClient:

    def __init__(self):
        self.__client_list = dict()
       

    def add(self,client):
        """
        function adds elements to the list of all clients
        :param client: the object of Client class to be added
        """        
        self.__client_list[client.id] = client

    @property
    def list_clients(self):
        return self.__client_list

    def delete(self,id):
        """
        function removes a client
        :param id: the id of the client to be removed
        """        
        self.__client_list.pop(id)

    def update(self,id,name):
        """
        function updates the client by changing the name keeping the id intact
        :param id: integer, theid of the client
        :param name: string, the new name
        """        
        
        self.__getitem__(id).set_name(name)

    def __getitem__(self, id):       
        return self.__client_list[id] 

    def __getlist__(self):         
        return self.__client_list.keys()   

    def __setall__(self, data={}):
        self.__client_list = data
    
    def __getall__(self):
        return self.__client_list



class ClientBinFileRepository(RepositoryClient):
    def __init__(self, filename):
        RepositoryClient.__init__(self)
        #self._data = dict()
        self._file_name = filename
        self._load_file()

    def _load_file(self):
        if os.path.getsize(self._file_name) > 0:
            file = open(self._file_name, "rb")  
            self.__setall__(pickle.load(file))
            file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")  
        pickle.dump(self.__getall__(), file)
        file.close()

    def add(self, entity):
       
        super(ClientBinFileRepository, self).add(entity)
        self._save_file()


    def delete(self,id):
       super(ClientBinFileRepository,self).delete(id)        
       self._save_file()

    def update(self,id,name):
             
        super(ClientBinFileRepository,self).update(id,name) 
        self._save_file()


class ClientTextFileRepository(RepositoryClient):
   

    def __init__(self, filename):
        RepositoryClient.__init__(self) 
        self._file_name = filename
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in file.readlines():
            if line.find(',') > 0:

                _id, name = line.split(maxsplit=1, sep=',')
            # super().add(Client(int(_id), str(name))) ##ccred ca trebe super().add....
                super(ClientTextFileRepository,self).add(Client(int(_id), name))
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt") 

        for c in self.__getlist__():
            client = self.__getitem__(c)     
            file.write(str(client.id) + ',' + str(client.name) + "\n")
        file.close()

    def add(self, entity):       
        super(ClientTextFileRepository, self).add(entity)
        self._save_file()

    def delete(self,id):
        super(ClientTextFileRepository,self).delete(id)     
        self._save_file()

    def update(self,id,name):       
        super(ClientTextFileRepository,self).update(id,name)
        self._save_file()



################################################################################################################################


class RepositoryRental:

    def __init__(self):
        self.__rental_list = dict()
        self.__rented_books_id = []
        self.__rented_books_id_counter= dict()  # contor cu fiecare carte de cate ori a fost inchiriata are ca si key id ul cartilor
        self.__clients_counter = dict()
        self.__authors_counter = dict()
        

    @property
    def rental_list(self):
        return self.__rental_list

    @property
    def rented_books(self):
        return self.__rented_books_id


    def __set_rented_book_id__(self,data = []):
        self.__rented_books_id = data

    def __get_rented_book_id__(self):
        return self.__rented_books_id



    def __set_rented_books_id_counter__(self, data = {}):
        self.__rented_books_id_counter = data

    def __get_rented_books_id_counter__(self):
        return self.__rented_books_id_counter


    def __set_clients_counter__(self, data = {}):
        self.__clients_counter == data

    def __get_clients_counter__(self):
        return self.__clients_counter

    def __set_authors_counter__(self, data ={}):
        self.__authors_counter = data

    def __get_authors_counter__(self):
        return self.__authors_counter


    def __setall__(self, data={}):
        self.__rental_list = data
    
    def __getall__(self):
        return self.__rental_list




    def add(self, rental:Rental, book_rental_id,author):
        """
        the function adds a new element to the list of all rentals
        :param rental: object of Rental class to be added
        :param book_rental_id: integer, the  id of the book that is going to be rented
        """        
        self.__rental_list[rental.rental_id] = rental
        self.__rented_books_id.append(book_rental_id)

    def add_to_authors(self,author):
        if author in self.__authors_counter.keys():
                    self.__authors_counter[author] =self.__authors_counter[author]  + 1
        else:
            self.__authors_counter[author] = int(1)

    def add_to_books(self,book_rental_id):
        if book_rental_id in self.__rented_books_id_counter.keys():
                    self.__rented_books_id_counter[book_rental_id] =  self.__rented_books_id_counter[book_rental_id] + 1
        else:                
            self.__rented_books_id_counter[book_rental_id] = int(1)
            
    def update(self,id,returned_date):
        """
        teh function updates the returning date from '0'
        :param id: integer, the id of the rental
        :param returned_date: string, the  new returned date
        """        
        
        self.__getitem__(id).set_returned_date(returned_date)

        book_id = self.__getitem__(id).rental_book_id
        client_id = self.__getitem__(id).rental_client_id
        rental_date = self.__getitem__(id).rented_date

        rental_day = rental_date[0]
        rental_month = rental_date[1]
        rental_year = rental_date[2]
        return_day = returned_date[0]
        return_month = returned_date[1]
        return_year = returned_date[2]

        date_rental = date(rental_year,rental_month,rental_day)
        date_return = date(return_year,return_month,return_day)
        delta = date_return - date_rental

        self.__rented_books_id.remove(book_id)

        if client_id in self.__clients_counter.keys():
            
            self.__clients_counter[client_id] =  self.__clients_counter[client_id] + delta.days
        else:                
            self.__clients_counter[client_id] = delta.days

    def undo_return(self,id):

        return_date = [0,0,0]
        returned_date =  self.__getitem__(id).returned_date

        book_id = self.__getitem__(id).rental_book_id
        client_id = self.__getitem__(id).rental_client_id
        rental_date = self.__getitem__(id).rented_date

        rental_day = rental_date[0]
        rental_month = rental_date[1]
        rental_year = rental_date[2]
        return_day = returned_date[0]
        return_month = returned_date[1]
        return_year = returned_date[2]

        date_rental = date(rental_year,rental_month,rental_day)
        date_return = date(return_year,return_month,return_day)
        delta = date_return - date_rental

        self.__rented_books_id.append(book_id)
        self.__clients_counter[client_id] =  self.__clients_counter[client_id] - delta.days
        self.__getitem__(id).set_returned_date(return_date)
       


                  
              
    def contorbooks(self):
        return self.__rented_books_id_counter


    def __getitem__(self, id):        
        return self.__rental_list[id] 

    def __getlist__(self):          
        return self.__rental_list.keys()   

    
       
    @property
    def books_counter(self):
        return self.__rented_books_id_counter

    @property
    def clients_counter(self):
        return self.__clients_counter

    @property
    def authors_counter(self):
        return self.__authors_counter

    def undo_rental(self,author,book_rental_id):
        self.__rented_books_id_counter[book_rental_id] =  self.__rented_books_id_counter[book_rental_id] - 1
        self.__rental_list.popitem()
        self.__rented_books_id.pop()
        self.__authors_counter[author] = self.__authors_counter[author] - 1


    





class RentalBinFileRepository(RepositoryRental):
    def __init__(self, filename):
        RepositoryRental.__init__(self)       
        self._file_name = filename
        self._load_file()

    def _load_file(self):
        if os.path.getsize(self._file_name) > 0:
            file = open(self._file_name, "rb")  
            self.__setall__(pickle.load(file))
            file.close()

    def _save_file(self):
        file = open(self._file_name, "wb")  
        pickle.dump(self.__getall__(), file)
        file.close()

    def add(self, entity,book_rental_id,author):
        super(RentalBinFileRepository, self).add(entity,book_rental_id,author)  # cum fac sa adauge la lista de carti eliberate deja
       
        
        self._save_file()  


    def update(self,id,returned_date):
       super(RentalBinFileRepository, self).update(id,returned_date)      
       self._save_file()
       

    
    def undo_return(self,id):

        super(RentalBinFileRepository, self).undo_return(id)
        self._save_file()

    def undo_rental(self,author,book_rental_id):
        super(RentalBinFileRepository, self).undo_rental(author,book_rental_id)
        self._save_file()

        
        

        


class RentalTextFileRepository(RepositoryRental):
   

    def __init__(self, filename):
        
        RepositoryRental.__init__(self) 
        self._file_name = filename
        self._load_file()

    def _load_file(self):
        file = open(self._file_name, "rt")  # rt -> read, text-mode
        for line in file.readlines():
            if line.find(',') > 0:
                _id, book_id, client_id, rent_date, return_date = line.split(maxsplit=4, sep=',')
                super().add(Rental(int(_id), int(book_id), int(client_id),rent_date, return_date))            
                super(RentalTextFileRepository,self).add(Rental(int(_id), int(book_id), int(client_id),rent_date, return_date)) ##ccred ca trebe super().add....
        file.close()

    def _save_file(self):
        file = open(self._file_name, "wt") 

        for rentals in  self.__getlist__():
            rental = self.__getitem__(rentals)
            file.write(str(rental.rental_id) + ',' + str(rental.rental_book_id) + ',' + str(rental.rental_client_id) + ',' + str(rental.rented_date)+ ',' + str(rental.returned_date) + "\n")  # change the naming for the fil einput

        file.close()

    def add(self, entity,book_rental_id,author):
       
        super(RentalTextFileRepository, self).add(entity,book_rental_id,author)
        self._save_file()






    def update(self,id,returned_date):
       super(RentalTextFileRepository, self).update(id,returned_date)      
       self._save_file()
       

    
    def undo_return(self,id):

        super(RentalTextFileRepository, self).undo_return(id)
        self._save_file()

    def undo_rental(self,author,book_rental_id):
        super(RentalTextFileRepository, self).undo_rental(author,book_rental_id)
        self._save_file()
  

    
 