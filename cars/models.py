from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200) # Modelo do veiculo
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # Marca do veiculo
    factory_year = models.IntegerField(blank=True, null=True) # Ano de fabricacao do veiculo
    model_year = models.IntegerField(blank=True, null=True) # Ano do veiculo
    plate = models.CharField(max_length=10, blank=True, null=True) # Placa do veiculo
    value = models.FloatField(blank=True, null=True) # Valor do veiculo
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    
    def __str__(self):
        return self.model