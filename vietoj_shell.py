import django
import os
#ištriniau decouple,pasiliko python-decouple
#.env ir setings.py pakaitimai minimalūs

os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')
django.setup()

from library.models import *

b=Book.objects.all()
print(b)

authors=Author.objects.all()
books=Book.objects.all()

some_list=[]
for author in authors:
    new_dict={}
    for book in books:
        if book.author.first_name not in new_dict.keys():
            new_dict['author_first_name']=book.author.first_name
        else:
            continue
    some_list.append(new_dict)
print(some_list)

book=Book.objects.filter(book_id=1).values()
print(book)
print(book[0])