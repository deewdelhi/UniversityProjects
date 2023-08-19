from django.db import models

class Customer ( models.Model):
    first_name = models.CharField(max_length = 100,default = "")
    last_name = models.CharField(max_length = 100,default = "")
    member_since = models.IntegerField(default = 0)
    address = models.CharField(max_length=100,default = "")
    email  = models.CharField(max_length=100,default = "")
    date_of_birth = models.IntegerField(default = 0)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email
    

class Author ( models.Model):
    first_name = models.CharField(max_length = 100,default = "")
    last_name = models.CharField(max_length = 100,default = "")
    nationality = models.CharField(max_length=100)
    date_of_birth = models.IntegerField(default = 0)
    preponderent_genre = models.CharField(max_length = 100,default = "")
   

    def __str__(self):
        return self.first_name + " " + self.last_name 

class PublishingHouse ( models.Model):
    name = models.CharField( max_length = 100)
    headquarters = models.CharField ( max_length = 100)
    founding_year = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.name

class Book( models.Model):
    title = models.CharField(max_length=100,default = "")
    #author = models.ManyToManyField(Author, through= 'BookWithAuthors')
    publishing_house = models.ForeignKey( PublishingHouse, related_name = "books", on_delete = models.CASCADE)
    description = models.TextField(default = "")
    releasing_year = models.IntegerField(default = 0)
    #authors = models.ManyToManyField(Book, through='CourseStudent')
    
    def __str__(self):
        return self.title 
    
class BookWithAuthors( models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete = models.CASCADE)
    book = models.ForeignKey(Book, related_name='authors', on_delete = models.CASCADE)
    book_contribution = models.CharField(max_length = 100)
    author_additions = models.CharField( max_length = 100)


    def __str__( self):
         return f"{self.book.title} - {self.author.first_name} {self.author.last_name}"
    




