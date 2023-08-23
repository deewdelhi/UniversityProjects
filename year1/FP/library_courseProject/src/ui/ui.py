from services.services import BookServices
from services.services import ClientServices
from services.services import RentalServices

from undo_handlers import UndoHandler
from redo_handlers import RedoHandler
from undo import UndoManager
from redo import RedoManager

class Ui:

    def __init__(self, book_service:BookServices, client_service:ClientServices, rental_service:RentalServices):

        self.__ui_book_service = book_service
        self.__ui_client_service = client_service
        self.__ui_rental_service = rental_service
    

    def print_menu():
        
        print(
        """
        Options available:

        1  -> Add new book 

        2  -> Add new client

        3  -> Display books

        4  -> Display clients

        5  -> Remove book

        6  -> Remove client

        7  -> Update book

        8  -> Ubdate client

        9  -> Rent book

        10 -> Return book

        11 -> Display rentals

        12 -> Top books
        
        13 -> Top clients

        14 -> Top authors

        15 -> Search book by field

        16 -> Search client by field

        17 -> Display menu

        18 -> Exit

        23 -> Undo

        24 -> Redo


        """        )


    def add_new_book_ui(self):
       
        try:
            id = input( " Enter book id:  ")
            if not id.isdecimal():
                raise ValueError
            title = input( " Enter book title:  ")
            author = input( " Enter author name:  ")
            for character in author:
                if not character.isalpha():
                    if character != " ":
                        raise AssertionError

        except AssertionError:
            print(" the author name must not contain any letters")   
        except ValueError:
            print("the id must not contain any letters")

        else:
            self.__ui_book_service .add_new_book(int(id),title,author)
            
            UndoManager.register_operation(self.__ui_book_service, UndoHandler.ADD_BOOK, int(id),title,author)


    def add_new_client_ui(self):
       
        try:
            id = input( " Enter client id:  ")
            if not id.isdecimal():
                raise ValueError
        except ValueError:
            print("the id must not contain any letters")
        else:   
            
            try:

                name = input( " Enter client name:  ")

                for character in name:
                    if not character.isalpha():
                        if character != " ":
                            raise AssertionError

            except AssertionError:
                print(" The client name must contain only letters!")

            else:
                     
                self.__ui_client_service .add_new_client(int(id),name) 
                UndoManager.register_operation(self.__ui_client_service, UndoHandler.ADD_CLIENT,int(id),name)    

    def remove_book_ui(self):
        try:
            id = input( " Enter the id of the book you want to remove:  ")
            if not id.isdecimal():
                raise ValueError
        except ValueError:
            print("the id must not contain any letters")      ##### how get the name ??? same problem with client
        else: 
            book = self.__ui_book_service.get_book(int(id))  
            book_id = book[0]
            book_title = book[1]
            book_author = book [2]
            print(str(book))
            self.__ui_book_service.remove_book(int(id))
            
            UndoManager.register_operation(self.__ui_book_service, UndoHandler.REMOVE_BOOK, int(book_id), str(book_title), str(book_author))


    def remove_client_ui(self):

        try:
            id = input( " Enter the id of the client you want to remove:  ")
            if not id.isdecimal():
                raise ValueError
        except ValueError:                              
            print("the id must not contain any letters")
        else:   
            client = self.__ui_client_service.get_client(int(id)) 
            client_id =int( client[0])
            client_name= client[1]
            self.__ui_client_service.remove_client(int(id))
            UndoManager.register_operation(self.__ui_client_service, UndoHandler.REMOVE_CLIENT, client_id, client_name)

    def update_client_by_id_ui(self):
        try:
            id = input( " Enter client id:  ")
            if not id.isdecimal():
                raise ValueError
        except ValueError:
            print("the id must not contain any letters")
        else:   
            
            try:

                name = input( " Enter the new name for this id:  ")

                for character in name:
                    if not character.isalpha():
                        if character != " ":
                            raise AssertionError

            except AssertionError:
                print(" The client name must contain only letters!")

            else:
                client = self.__ui_client_service.get_client(int(id)) 
                client_id =int( client[0])
                client_name= client[1]    
                self.__ui_client_service .update_client_by_id(int(id), name)
                UndoManager.register_operation(self.__ui_client_service, UndoHandler.UPDATE_CLIENT_INFORMATION, client_id, name,client_name)

    def update_book_by_id_ui(self):
        try:
            id = input( " Enter book id:  ")
            if not id.isdecimal():
                raise ValueError
        except ValueError:
            print("the id must not contain any letters")
        else:   
            title = input( " Enter book title:  ")
            try:

                author = input( " Enter author name:  ")

                for character in author:
                    if not character.isalpha():
                        if character != " ":
                            raise AssertionError

            except AssertionError:
                print(" The author name must contain only letters!")

            else:
                book = self.__ui_book_service.get_book(int(id))  
                book_id = book[0]
                book_title = book[1]
                book_author = book [2]    
                self.__ui_book_service .update_book_by_id(int(id), title,author)
                UndoManager.register_operation(self.__ui_book_service, UndoHandler.UPDATE_BOOK_INFORMATION, book_id, title, book_title, author,book_author)

    def update_rental_by_id_ui(self):

        try:
            id = input( " Enter rental id:  ")
            if not id.isdecimal():
                raise ValueError
        except ValueError:
            print("the id must not contain any letters")
        else:  
            try:

               
                return_day = input(" enter the day  ")
                return_month = input(" enter the month  ")
                return_year = input(" enter the year  ")

                if not ( return_day.isdecimal() and return_month.isdecimal() and return_year.isdecimal()):
                    raise ValueError

            except ValueError:
                print(" the dates must contain only digits ")


            else:
                     
                self.__ui_rental_service .update_rental_by_id(int(id), int(return_day), int(return_month) , int(return_year)) 
                UndoManager.register_operation(self.__ui_rental_service, UndoHandler.RETURN_BOOK, int(id), int(return_day), int(return_month) , int(return_year))



    def list_books(self):
        final_list = self.__ui_book_service.to_list()
        for i in range (len(final_list)):
            print("Book id: " + str(final_list[i][0]) + "|  Book title: " + final_list[i][1] + "|  Book author : " + final_list[i][2]  + "\n")

    def list_clients(self):

                 
        final_list = self.__ui_client_service.to_list()
        for i in range (len(final_list)):
            print("Client id: " + str(final_list[i][0]) + "  Client name: " + final_list[i][1] + "\n")

    def list_rentals(self):

        final_list = self.__ui_rental_service.to_list()
        for i in range (len(final_list)):
            print( "Rental id: " + str(final_list[i][0]) + "  Book id: " + str(final_list[i][1]) + "  Client id: " + str(final_list[i][2]) + \
            "  Rented date: " + str(final_list[i][3]) + "  Returned date: " + str(final_list[i][4]) + "\n" )

    def rent_book_ui(self):

        try:
            rental_id = input( " Enter rental id:  ")
            book_rental_id = input(" Enter the id of the book you want to rent:  ")
            client_rental_id = input(" Enterthe id of the client that wants to rent a book:  ")

            if not (rental_id.isdecimal() and book_rental_id.isdecimal() and  client_rental_id.isdecimal() ):
                raise ValueError
        except ValueError:
            print("every id must not contain any letters")
        else:   
            
            try:

                
                rental_day = input(" enter the day  ")
                rental_month = input(" enter the month  ")
                rental_year = input(" enter the year  ")

                if not ( rental_day.isdecimal() and rental_month.isdecimal() and rental_year.isdecimal()):
                    raise ValueError

            except ValueError:
                print(" the dates must contain only digits ")



            else:
                if self.__ui_book_service.check_valid_id_book(book_rental_id) == True and self.__ui_client_service.check_valid_id_client(client_rental_id) == True:

                    author = self.__ui_book_service.get_author(book_rental_id)
                    self.__ui_rental_service.add_new_rental( author, int(rental_id),int( book_rental_id), int( client_rental_id), int(rental_day), int(rental_month),int(rental_year), return_date = int(0))
                    UndoManager.register_operation(self.__ui_rental_service, UndoHandler.RENT_BOOK, author, int(rental_id),int( book_rental_id), int( client_rental_id), int(rental_day), int(rental_month),int(rental_year))
                else:
                    print("Book and/or client not valid!")

    def print_top_books(self):
        books_sorted = self.__ui_rental_service.sort_contor_books()
        for key in books_sorted.keys():
            print(  " Book with id:  " + str(key) + ";  Number of rentals:  " + str(books_sorted[key]) + "\n")

    def print_top_clients(self):
        clients_sorted = self.__ui_rental_service.sort_contor_clients()
        for key in clients_sorted.keys():
            print(  " Client with id:  " + str(key) + ";  Number of days:  " + str(clients_sorted[key]) + "\n")

    def print_top_authors(self):
        authors_sorted = self.__ui_rental_service.sort_contor_authors()
        for key in authors_sorted.keys():
            print(  " author:  " + str(key) + ";  Number of rentals:  " + str(authors_sorted[key]) + "\n")

    def search_book(self):
        list_books = self.__ui_book_service.to_list()
      
        
        try:
            option = input("""
            choose the field:
            1 - id
            2 - title
            3 - author
            """ )
            if not option.isdecimal():
                raise ValueError
        except:
            print( " the pption must contain only digits")
        else:
            if int(option) == 1:

                try:
                    id = input(" enter id")
                    if not id.isdecimal():
                        raise ValueError
                except:
                    print( " the pption must contain only digits")

                else:


                    for index in range (0, len(list_books)):
                        if str(id) in str(list_books[index][0]):
                            print(list_books[index] )

            elif int(option) == 2:
                title = input(" enter title  ")
                for index in range (0, len(list_books)):
                        if str(title).lower() in str(list_books[index][1]).lower():
                            print(list_books[index] )

            elif int(option) == 3:
                try:
                    author = input(" enter author  ")
                    for character in author:
                        if not character.isalpha():
                            if character != " ":
                                raise AssertionError

                except AssertionError:
                    print(" the author name must not contain any letters")

                else:
                    for index in range (0, len(list_books)):
                        if str(author).lower() in str(list_books[index][2]).lower():
                            print(list_books[index] )


    def search_client(self):

        list_clients = self.__ui_client_service.to_list()

        try:
            option = input("""
            choose the field:
            1 - id
            2 - name
            
            """ )
            if not option.isdecimal():
                raise ValueError
        except:
            print( " the option must contain only digits")
        else:
            if int(option) == 1:

                try:
                    id = input(" enter id  ")
                    if not id.isdecimal():
                        raise ValueError
                except:
                    print( " the pption must contain only digits")

                else:


                    for index in range (0, len(list_clients)):
                        if str(id) in str(list_clients[index][0]):
                            print(list_clients[index] )

            elif int(option) == 2:
                try:
                    name = input(" enter name  ")
                    for character in name:
                        if not character.isalpha():
                            if character != " ":
                                raise AssertionError

                except AssertionError:
                    print(" the client name must not contain any letters")

                else:
                    for index in range (0, len(list_clients)):
                        if str(name).lower() in str(list_clients[index][1]).lower():
                            print(list_clients[index] )


    def author(self):
        id = input("enter id for author  ")
        print( self.__ui_book_service.get_auhor(id))




    def undo_menu(self, redo_handler):

        if redo_handler is RedoHandler.ADD_BOOK:
            book_id = RedoManager.get_first_argument()
            book_title = RedoManager.get_second_argument()
            book_author = RedoManager.get_third_argument()
            UndoManager.register_operation(self.__ui_book_service , UndoHandler.ADD_BOOK, book_id, book_title,  book_author)

        elif redo_handler is RedoHandler.ADD_CLIENT:
            client_id = RedoManager.get_first_argument()
            client_name = RedoManager.get_second_argument()
            UndoManager.register_operation(self.__ui_client_service, UndoHandler.ADD_CLIENT, client_id,
                                            client_name)
        
        elif redo_handler is RedoHandler.REMOVE_BOOK:
            book_id = RedoManager.get_first_argument()
            book_title = RedoManager.get_second_argument()
            book_author = RedoManager.get_third_argument()
            UndoManager.register_operation(self.__ui_book_service, UndoHandler.REMOVE_BOOK, book_id , book_title, book_author)

        elif redo_handler is RedoHandler.REMOVE_CLIENT:
            client_id = RedoManager.get_first_argument()
            client_name = RedoManager.get_second_argument()
            UndoManager.register_operation(self.__ui_client_service, UndoHandler.REMOVE_CLIENT, client_id,client_name)

        elif redo_handler is RedoHandler.UPDATE_BOOK_INFORMATION:
            book_id = RedoManager.get_first_argument()               ##### +++++  ADD RENTAL THINGS
            old_book_title = RedoManager.get_second_argument()     
            new_book_title = RedoManager.get_third_argument()
            old_author_name = RedoManager.get_fourth_argument()
            new_author_name = RedoManager.get_fifth_argument()
            UndoManager.register_operation(self.__ui_book_service, UndoHandler.UPDATE_BOOK_INFORMATION, book_id, old_book_title, new_book_title,old_author_name, new_author_name )


        elif redo_handler is RedoHandler.UPDATE_CLIENT_INFORMATION:
            client_id = RedoManager.get_first_argument()
            old_client_name = RedoManager.get_second_argument()
            new_client_name = RedoManager.get_third_argument()
            UndoManager.register_operation(self.__ui_client_service, UndoHandler.UPDATE_CLIENT_INFORMATION,
                                            client_id, old_client_name, new_client_name)

        elif redo_handler is RedoHandler.RENT_BOOK:
            author = RedoManager.get_first_argument()
            book_id = RedoManager.get_second_argument()
            client_id= RedoManager.get_third_argument()
            rental_day = RedoManager.get_fourth_argument()
            rental_month = RedoManager.get_fifth_argument()
            rental_year = RedoManager.get_sixth_argument()
            returned_day =RedoManager.get_seventh_argument()
            UndoManager.register_operation(self.__ui_rental_service, UndoHandler.RENT_BOOK,
                                            author,book_id,  client_id, rental_day, rental_month, rental_month, rental_year)

        elif redo_handler is RedoHandler.RETURN_BOOK:
            id = RedoManager.get_first_argument()
            rent_day = RedoManager.get_second_argument()
            rent_month= RedoManager.get_third_argument()
            rent_year = RedoManager.get_fourth_argument()
            
            UndoManager.register_operation(self.__ui_rental_service, UndoHandler.RENT_BOOK,
                                            id,rent_day, rent_month, rent_year)




    def redo_menu(self, undo_handler):

        if undo_handler is UndoHandler.ADD_BOOK:
            book_id = UndoManager.get_first_argument()
            book_name = UndoManager.get_second_argument()
            book_author = UndoManager.get_third_argument()
            RedoManager.register_operation(self.__ui_book_service, RedoHandler.ADD_BOOK, book_id, book_name, book_author)

        elif undo_handler is UndoHandler.ADD_CLIENT:
            client_id = UndoManager.get_first_argument()
            client_name = UndoManager.get_second_argument()
            RedoManager.register_operation(self.__ui_client_service, RedoHandler.ADD_CLIENT, client_id, client_name)

        # elif undo_handler is UndoHandler.ADD_GRADE:
        #     discipline_id = UndoManager.get_first_argument()
        #     student_id = UndoManager.get_second_argument()    ################ save for rental
        #     grade_value = UndoManager.get_third_argument()
        #     RedoManager.register_operation(self._grade_book_service, RedoHandler.ADD_GRADE, discipline_id, student_id,grade_value)


        elif undo_handler is UndoHandler.REMOVE_BOOK:
            book_id = UndoManager.get_first_argument()
            book_title = UndoManager.get_second_argument()
            book_author = UndoManager.get_third_argument()
            RedoManager.register_operation(self.__ui_book_service, RedoHandler.REMOVE_BOOK, book_id, book_title, book_author)

        elif undo_handler is UndoHandler.REMOVE_CLIENT:
            client_id = UndoManager.get_first_argument()
            client_name = UndoManager.get_second_argument()
            RedoManager.register_operation(self.__ui_client_service, RedoHandler.REMOVE_CLIENT, client_id, client_name)

        elif undo_handler is UndoHandler.UPDATE_BOOK_INFORMATION:
            book_id = UndoManager.get_first_argument()
            old_book_title = UndoManager.get_second_argument()       
            new_book_title = UndoManager.get_third_argument()
            old_author_name = UndoManager.get_fourth_argument()
            new_author_name = UndoManager.get_fifth_argument()
            RedoManager.register_operation(self.__ui_book_service, RedoHandler.UPDATE_BOOK_INFORMATION ,book_id, old_book_title,new_book_title,old_author_name, new_author_name )

        elif undo_handler is UndoHandler.UPDATE_CLIENT_INFORMATION:
            client_id = UndoManager.get_first_argument()
            old_client_name = UndoManager.get_second_argument()
            new_client_name = UndoManager.get_third_argument()
            RedoManager.register_operation(self.__ui_client_service, RedoHandler.UPDATE_CLIENT_INFORMATION,
                                           client_id, new_client_name, old_client_name)

        elif undo_handler is UndoHandler.RENT_BOOK:
            author = UndoManager.get_first_argument()
            book_id = UndoManager.get_second_argument()
            client_id= UndoManager.get_third_argument()
            rental_day = UndoManager.get_fourth_argument()
            rental_month = UndoManager.get_fifth_argument()
            rental_year = UndoManager.get_sixth_argument()
            returned_day =UndoManager.get_seventh_argument()
            RedoManager.register_operation(self.__ui_rental_service, RedoHandler.RENT_BOOK,
                                            author,book_id,  client_id, rental_day, rental_month, rental_month, rental_year)

        elif undo_handler is UndoHandler.RETURN_BOOK:
            id = UndoManager.get_first_argument()
            rent_day = UndoManager.get_second_argument()
            rent_month= UndoManager.get_third_argument()
            rent_year = UndoManager.get_fourth_argument()
            
            RedoManager.register_operation(self.__ui_rental_service, RedoHandler.RETURN_BOOK,
                                            id, rent_day, rent_month, rent_year)




    


    def console(self):

        Ui.print_menu()
       
        while True:

            try:
                user_option = input( " Enter your option:  " )
                assert int(user_option)
                
            except:
                print("The option must contain only digits!")  

            else:
                if int(user_option) == 1:
                    Ui.add_new_book_ui(self)

                elif int(user_option) == 2:
                    Ui.add_new_client_ui(self)
            
                elif int(user_option) == 3:
                    self.list_books()

                elif int(user_option) == 4:
                    self.list_clients()

                elif int(user_option) == 5:
                    self.remove_book_ui()
              
                elif int(user_option) == 6:
                    self.remove_client_ui() 

                elif int(user_option) == 7:
                    self.update_book_by_id_ui()

                elif int(user_option) == 8:
                    self.update_client_by_id_ui()

                elif int(user_option) == 9:
                    self.rent_book_ui()
                    
                elif int(user_option) == 11:
                    self.list_rentals()
                elif int(user_option) == 10:
                    self.update_rental_by_id_ui()
                elif int(user_option) == 17:
                    Ui.print_menu()
                elif int(user_option) == 18:
                    break

                elif int(user_option) == 19:
                    Ui.print_Con_books(self)

                elif int(user_option) == 12:
                    Ui.print_top_books(self)
                    
                elif int(user_option) == 15:
                    Ui.search_book(self)
                
                elif int(user_option) == 16:
                    Ui.search_client(self)

                elif int(user_option) == 13:
                    Ui.print_top_clients(self)

                elif int(user_option) == 20:
                    Ui.print_Con_clients(self)

                elif int(user_option) == 21:
                    Ui.author(self)

                elif int(user_option) == 14:
                    Ui.print_top_authors(self)

                elif int(user_option) == 22:
                    Ui.print_Con_authors(self)

                elif int(user_option) == 23:
                    undo_handler = UndoManager.get_handler()
                    self.redo_menu(undo_handler)
                    UndoManager.undo()
                
                elif int(user_option) == 24:
                    redo_handler = RedoManager.get_handler()
                    self.undo_menu(redo_handler)
                    RedoManager.redo()

                
