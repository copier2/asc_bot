from django.db import models


class Brand(models.Model):
    """Производитель (бренд)"""
    title = models.CharField(
        max_length=200
    )
    courier_delivery = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class ASC(models.Model):
    """АСЦ производителя"""
    name = models.CharField(
        max_length=200
    )
    phone_number_primary = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    address_primary = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )
    email = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class CommodityGroup(models.Model):
    """Товарная группа бренда, которая обслуживает АСЦ"""
    title = models.CharField(
        max_length=800
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title


class ASCList(models.Model):
    """Список производителя и АСЦ"""
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    asc = models.ForeignKey(
        ASC,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    commodity_group = models.ForeignKey(
        CommodityGroup,
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    def __str__(self):
        return f'{str(self.brand)}'
