from django.contrib import admin

from .models import Book,Author,PublishingHouse,Customer

from .models import Book,Author,PublishingHouse,Customer,BookWithAuthors
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Customer)
admin.site.register(PublishingHouse)
admin.site.register(BookWithAuthors)