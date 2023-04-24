from django.db import models
import uuid

class Genre(models.Model):
    genre_id=models.AutoField(primary_key=True)
    name=models.CharField('Name',max_length=100,help_text='enter type ganre')

    def __str__(self):
        return self.name

class Author(models.Model):
    author_id=models.AutoField(primary_key=True)
    first_name=models.CharField('First name',max_length=100)
    last_name = models.CharField('Last name', max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} ({self.last_name})'

class Book(models.Model):
    book_id=models.AutoField(primary_key=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL, null=True)
    title=models.CharField('Title',max_length=200,help_text='entre boo title')
    genre=models.ManyToManyField(Genre,help_text='entre books genre')
    description=models.TextField('Dwscription',max_length=1000,help_text='enter description..')
    isbn=models.CharField(
        'ISBN',max_length=13,
        help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn">ISBN kodas</a>')

    def __str__(self):
        return self.title


class BookInstance(models.Model):
    """Modelis, aprašantis konkrečios knygos kopijos būseną"""
    instance_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unikalus ID knygos kopijai')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField('Bus prieinama', null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota'),
    )
    book_status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.book.title}'