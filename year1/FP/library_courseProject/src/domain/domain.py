class Book:

    def __init__(self,id,title,author):
        self.__book_id = id
        self.__book_title = title
        self.__book_author = author
       
    
    @property
    def id(self):
        return self.__book_id
      
    @property
    def title(self):
        return self.__book_title  
    
    @property
    def author(self):
        return self.__book_author

   

    def set_title(self,title):
        self.__book_title = title

    def set_author(self,author):
        self.__book_author = author
    
   
   

    # def to_string(self):
    #     return "Book id: " + str(self.__book_id) + "|  Book title: " + self.__book_title + "|  Book author : " + self.__book_author  + "\n"

    def make_list(self):
        book = [self.__book_id,  self.__book_title, self.__book_author]
        return book









################################################################################################################################



class Client:

    def __init__(self, id, name):
        self.__client_id = id
        self.__client_name = name
       

    @property
    def id(self):
        return self.__client_id

    @property
    def name(self):
        return self.__client_name

     
    def set_name(self,name):
        self.__client_name = name
        

    # def to_string(self):
    #     return "Client id: " + str(self.__client_id) + "  Client name: " + self.__client_name + "\n"
    
    def make_list(self):

        client = [ self.__client_id, self.__client_name ]
        return client



################################################################################################################################



class Rental:

    def __init__(self, RentId, BookId, ClientId, rent_date, return_date):

        self.__rental_id = RentId
        self.__rental_book_id = BookId
        self.__rental_client_id = ClientId
        self.__rented_date = rent_date
        self.__returned_date = return_date

    @property
    def rental_id(self):
        return self.__rental_id

    @property
    def rental_book_id(self):
        return self.__rental_book_id

    @property
    def rental_client_id(self):
        return self.__rental_client_id

    @property
    def rented_date(self):
        return self.__rented_date

    @property
    def returned_date(self):
        return self.__returned_date
        


    def set_returned_date(self,date):
        self.__returned_date = date

    # def to_string(self):
    #     return "Rental id: " + str(self.rental_id) + "  Book id: " + str(self.rental_book_id) + "  Client id: " + str(self.rental_client_id) + \
    #         "  Rented date: " + str(self.rented_date) + "  Returned date: " + str(self.returned_date) + "\n" 

    def make_list(self):

        rental = [ self.__rental_id,self.__rental_book_id, self.__rental_client_id, self.__rented_date, self.__returned_date]
        return rental





