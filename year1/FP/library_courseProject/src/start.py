

from services.services import BookServices, ClientServices
from services.services import RentalServices
from ui.ui import Ui
from repository.repository import RepositoryBook, RepositoryClient, RepositoryRental, BookBinFileRepository,BookTextFileRepository, ClientBinFileRepository,ClientTextFileRepository, RentalBinFileRepository,RentalTextFileRepository
from domain.domain import Book, Client, Rental
import traceback
import os.path


file = open("settings.properties" , "r")
row = 1

for line in file.readlines():
    if row == 1:
        entity,type = line.split(maxsplit=1, sep='=')          
    if row == 2:
        entity, book_file = line.split(maxsplit = 1,sep ='=')
        if book_file == '"bookbin.txt"\n':
            book_file = "bookbin.txt"
        else:
            book_file = "book.txt"


            
        basepath_book = os.path.basename(book_file)
    if row == 3:
        entity, client_file = line.split(maxsplit = 1,sep ='=')
        if client_file == '"clientbin.txt"\n':
            client_file = "clientbin.txt"
        else:
            client_file = "client.txt"


        basepath_client = os.path.basename(client_file)
    if row == 4:
        entity, rental_file = line.split(maxsplit = 1,sep ='=')
        if rental_file == '"rentalbin.txt"':
            rental_file = "rentalbin.txt"
        else:
            rental_file = "rental.txt"

        basepath_rental = os.path.basename(rental_file)

    row = row + 1

file.close()


if type == '"textfile"\n':
    
    book_repository = BookTextFileRepository(basepath_book)
    client_repository = ClientTextFileRepository(basepath_client)
    rental_repository = RentalTextFileRepository(basepath_rental)

if type == '"binaryfile"\n':

    book_repository = BookBinFileRepository(basepath_book)   
    client_repository = ClientBinFileRepository(basepath_client)
    rental_repository = RentalBinFileRepository(basepath_rental)

elif type == '"inmemory"\n':
    book_repository = RepositoryBook()
    client_repository = RepositoryClient()
    rental_repository = RepositoryRental()


rental_service = RentalServices(rental_repository)
book_service = BookServices(book_repository)
client_service = ClientServices(client_repository)



# book_repository.add(Book(10,"it","stephen king"))
# book_repository.add(Book(11,"dune","paul atreides"))
# book_repository.add(Book(12,"Ion","rebreanu"))
# book_repository.add(Book(13,"the dog","samantha moore"))
# book_repository.add(Book(14,"lIfe book","noel"))
# book_repository.add(Book(15,"the tree cottage","boris moose"))
# book_repository.add(Book(16,"7 pounds","lena collar"))
# book_repository.add(Book(17,"life of nemo","remi "))
# book_repository.add(Book(18,"Korra","dori mane"))
# book_repository.add(Book(19,"the dynasty","sofia "))
# book_repository.add(Book(20,"a simple novel","lolla"))

# client_repository.add(Client( 10,"andrei"))
# client_repository.add(Client( 11,"ana"))
# client_repository.add(Client( 12,"maria"))
# client_repository.add(Client( 13,"samantha"))
# client_repository.add(Client( 14,"sofia"))
# client_repository.add(Client( 15,"sorana"))
# client_repository.add(Client( 16,"mircea"))
# client_repository.add(Client( 17,"tudor"))
# client_repository.add(Client( 18,"maia"))
# client_repository.add(Client( 19,"carmen"))
# client_repository.add(Client( 20,"ovidiu"))



# rental_service.add_new_rental("rebreanu",1,12,12,1,1,2020,0)
# rental_service.add_new_rental("samantha moore",2,13,13,1,2,2020,0)
# rental_service.add_new_rental("noel",3,14,13,1,2,2020,0)
# rental_service.add_new_rental("boris moose",4,15,14,1,4,2020,0) 


ui = Ui(book_service, client_service, rental_service)

ui.console()

