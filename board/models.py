from tarfile import PAX_NUMBER_FIELDS
from django.db import models



#
# ������� ��������, ��������� � ������
#

class usersByType(models.Model):                            #��������� ������ � ������ ��� ������������� �������
    class Meta():
        db_table = 'users'
    user = models.CharField(max_length=70, blank=True)
    group = models.TextField(null=False)
    schoolClass = models.CharField(max_length=4,blank=True)   #������������ ��� ��� ����������� ������ ������, ��� � ��� ����������� �����.���.

class subjectsByClass(models.Model):                #������� ������ ������������� �������� �������
    class Meta():
        db_table = 'subjects'
    schoolClass = models.CharField(max_length=5)
    physicalEducation = models.BooleanField(default = False)
    biology = models.BooleanField(default = False)
    math = models.BooleanField(default = False)
    ruLanguage = models.BooleanField(default = False)
    enLanguage = models.BooleanField(default = False)

class homeworkByClass(models.Model):    #�������� ������ �� ����� ��� ���������� �������� ��� ����������� ������
    class Meta():
        db_table = 'homeworks'
    classId = models.IntegerField()
    subjectId = models.IntegerField()
    data = models.CharField(max_length=10)
    homework = models.TextField()


class marksByUsers(models.Model):                   #������ ������, ������������� ��� id user, �� ���� � ��������
    class Meta():
        db_table = 'marks'
    userId = models.IntegerField()
    subjectId = models.IntegerField()
    data = models.CharField(max_length=30)
    mark = models.CharField(max_length=5)

class salesPeople(models.Model):
    class Meta():
        db_table = 'SalespeopleOne'
    SNAME = models.CharField(max_length=10)
    CITY = models.CharField(max_length=10)
    COMM = models.IntegerField()

class customers(models.Model):
    CNAME = models.CharField(max_length=10)
    CITY = models.CharField(max_length=10)
    RATING = models.IntegerField()

class product(models.Model):
    class Meta():
        db_table = 'product'
    PNAME = models.CharField(max_length=20)
    PRICE = models.IntegerField()

class orderdetails(models.Model):
    class Meta():
        db_table = 'order_details'
    PNUM = models.ForeignKey(product, on_delete=models.CASCADE)
    QUANTITY = models.IntegerField()

class orders(models.Model):
    class Meta():
        db_table = 'orders'
    AMT = models.IntegerField()
    ODATE = models.DateField()
    CNUM = models.ForeignKey(customers,on_delete=models.CASCADE)
    SNUM = models.ForeignKey(salesPeople,on_delete=models.CASCADE)
    ORDERDETAILS = models.ForeignKey(orderdetails, on_delete=models.CASCADE, blank=True)
