from rest_framework import serializers
from .models import Customer, Book, PublishingHouse,Author
from .models import Customer, Book, PublishingHouse,Author,  BookWithAuthors
import datetime

from django.shortcuts import render, get_object_or_404



#---------------------------------------BOOK WITH AUTHORS SERIALIZERS----------------------------------------------------





class BookWithAuthorsSerializer ( serializers.ModelSerializer):
    
    class Meta:
        model =  BookWithAuthors
        fields = ('__all__')

#---------------------------------------BOOK SERIALIZERS+ PublishingHouseSerializer_list ----------------------------------------------------

class PublishingHouseSerializer_list( serializers.ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = ('__all__')

    
    def validate_headquarters(self, value): 
          
        if not value.isalpha():
            raise serializers.ValidationError('This field must contain only letters!')
        return value
        


class BookSerializer_list(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('__all__')

    def validate_releasing_year(self, value):  
    
        today = datetime.datetime.now()
        year = today.year
        if value <= int(year):
            return value
        raise serializers.ValidationError('The provided year is not valid.')
    


class BooksSerializer_justTitle(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']


class BookSerializer(serializers.ModelSerializer):
    publishing_house = PublishingHouseSerializer_list(read_only=True,)
    authors = BookWithAuthorsSerializer(read_only=True ,many = True)
    
    class Meta:
        model = Book
        fields = ['id','title','description','releasing_year','publishing_house','authors']
    

#---------------------------------------PUBLISHING HOUSE SERIALIZERS + FILTER ----------------------------------------------------



class PublishingHouseSerializer( serializers.ModelSerializer):
    books = BookSerializer_list(read_only=True, many=True)
    class Meta:
        model = PublishingHouse
        fields = ['name','headquarters','founding_year','books']

    def validate_headquarters(self, value): 
          
        if not value:
            raise serializers.ValidationError('This field can not be left empty!')
        return value


# DON T TOUCH IT
class PublishingHouseFilterSerializer(serializers.ModelSerializer):
    avg_year = serializers.FloatField(read_only= True)

    #  for all info in the book object
    # books = BookSerializer_list( read_only = True,many = True)

    #for only the title
    books = BooksSerializer_justTitle( read_only = True,many = True)
    class Meta:
        model = PublishingHouse
        fields = ['id','name','headquarters','founding_year','avg_year','books']


#---------------------------------------AUTHOR SERIALIZERS + FILTERS ----------------------------------------------------


class AuthorSerializer_list( serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')

    def validate_first_name(self, value): 
          
        if not value[0].isupper():
            raise serializers.ValidationError('The name must start with an uppercase letter!')
        
        if not all(x.isalpha() or x.isspace() for x in value):
            raise serializers.ValidationError('This field must contain only letters!')
        
        return value
    
    def validate_last_name(self, value): 
          
        if not value[0].isupper():
            raise serializers.ValidationError('The name must start with an uppercase letter!')
        
        if not all(x.isalpha() or x.isspace() for x in value):
            raise serializers.ValidationError('This field must contain only letters!')        
        
        if ' ' in value:
            raise serializers.ValidationError('You must enter just the last name of the author!')
        return value
    

class AuthorFilterSerializer(serializers.ModelSerializer):
    avg_releasing_year = serializers.FloatField(read_only = True)
    # bookwithauthors =  BookWithAuthorsSerializer( read_only = True,many = True)

    class Meta:
        model = Author
        fields = ['id','first_name','last_name','nationality','date_of_birth','preponderent_genre','avg_releasing_year']

class AuthorSerializer(serializers.ModelSerializer):
   
    books = BookWithAuthorsSerializer(read_only=True ,many = True)
    # bookwithauthors =  BookWithAuthorsSerializer( read_only = True,many = True)
    
    class Meta:
        model = Author
        fields = ['id','first_name','last_name','nationality','date_of_birth','preponderent_genre','books']

       
#---------------------------------------CUSTOMER SERIALIZERS + FILTERS ----------------------------------------------------


class CustomerSerializer_list (serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')



class BooksForPublishingHouseSerializer (serializers.ModelSerializer):
    id= serializers.IntegerField()


    def create(self,validated_data):
        book_id = validated_data['id']
        book = get_object_or_404(Book, pk = book_id)
        book.publishing_house = validated_data['publishing_house']
        db = validated_data.get('using',None)
        book.save(using = db)
        return book
    
    class Meta:
        model = Book
        fields = ['id']




