from django.db import models

class Staff(models.Model):
    email = models.EmailField(max_length=30,blank=False)
    password = models.CharField('contraseña',max_length=25,blank=False)

    def __str__(self):
        return f'{self.email}'

class Users(models.Model):
    name = models.CharField("nombre", max_length=25,blank=False )
    lastname = models.CharField('apellido', max_length=25, blank=False)
    email = models.EmailField(max_length=30,blank=False)
    birthday = models.DateField(blank=False)
    phone = models.IntegerField(blank=False)
    address = models.CharField('direccion',max_length=25,blank=False)

    def __str__(self):
        return f'{self.name} - {self.lastname}'

class Orders(models.Model):
    client = models.ForeignKey(Users , on_delete=models.CASCADE,blank=False)
    travel = models.CharField(max_length=25,blank=False)
    price = models.IntegerField(blank=False)
    departure = models.DateField(blank=False)
    arrival = models.DateField(blank=False)

    def __str__(self):
        return f'{self.client} - {self.travel} - ${self.price}'

class Travel(models.Model):
    name = models.CharField(max_length=25,blank=False)
    image = models.CharField(max_length=300,blank=False)
    price = models.IntegerField(blank=False)
    time = models.CharField(max_length=25,blank=False)
    description = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return f'{self.name} - ${self.price}'

