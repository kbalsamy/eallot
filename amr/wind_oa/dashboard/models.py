from django.db import models


class Customer(models.Model):

    customer_name = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_name


# model for Edc mapping
class EDCModel(models.Model):

    code = models.CharField(max_length=3)
    place = models.CharField(max_length=25)

    def __str__(self):

        return self.code


# Model for customer mapping

class ServiceGroup(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    serviceNumber = models.CharField(max_length=12, unique=True)
    edc = models.ForeignKey(EDCModel, on_delete=models.CASCADE)

    def __str__(self):

        return self.serviceNumber


class Readings(models.Model):

    consumerID = models.CharField(max_length=12)
    statementMonth = models.CharField(max_length=2, blank=True)
    statementYear = models.CharField(max_length=4, blank=True)
    impUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC002 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC003 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC004 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC005 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC006 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC007 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC001 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)

    def __str__(self):

        return self.consumerID + '_' + self.statementMonth + self.statementYear
