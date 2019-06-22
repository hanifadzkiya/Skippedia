from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


# Student model
# Student model, in a sense, is a weak entity to user
# id_user is the foreign key. 
# Django's standard user model is extended in this manner
# Includes enumerated choices for 'jurusan' field

class Student(models.Model):  
    IF= 'IF'
    STI = 'STI'
    JURUSAN_CHOICES = [
        (IF , 'Teknik Informatika'),
        (STI , 'Sistem dan Teknologi Informasi')
    ]
    id = models.AutoField(primary_key=True)
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=8)
    jurusan = models.CharField(
        max_length = 3,
        choices = JURUSAN_CHOICES,
        default = IF
    )
    angkatan = models.PositiveIntegerField(
        default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
        
    photo = models.CharField(max_length=255,blank=True)
    class Meta:
	    ordering = ('nim',)

# Reputation model
# Have one-to-many relationship with User(as receiver) and many-to-one (as received)
# Includes integerRangeField and Comment

class Reputation(models.Model):
    id = models.AutoField(primary_key=True)
    id_sender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='sended_reputations')
    id_receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='received_reputations')
    rating = IntegerRangeField(min_value=1, max_value=10)
    comment = models.CharField(max_length=255)