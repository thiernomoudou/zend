from django.db import models

# Create your models here.

#refer to the Getswift api documentation for fields descrition
#https://app.getswift.co/ApiDocs/ResourceModel?modelName=DeliveryBookingItemModel
class DeliveryBookingItemModel(models.Model):
    quantity = models.IntegerField()
    sku = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)

#for more info
#https://app.getswift.co/ApiDocs/ResourceModel?modelName=ExtraAddressDetails
class ExtraAddressDetails(models.Model):
    stateProvince = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    suburbLocality = models.CharField(max_length=35, null=True, blank=True)
    postcode = models.CharField(max_length=11, null=True, blank=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)

# for more informatio see
#https://app.getswift.co/ApiDocs/ResourceModel?modelName=DeliveryBookingLocationModel
class DeliveryBookingLocationModel(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=256, null=True, blank=True)
    address = models.CharField(max_length=250)
    additionnalAdressDetail = models.ForeignKey(ExtraAddressDetails, on_delete=models.CASCADE, null=True, blank=True)

# for information about fields refer to
#https://app.getswift.co/ApiDocs/ResourceModel?modelName=TimeFrameModel
class TimeFrameModel(models.Model):
    easliestTime = models.DateField(null=True, blank=True)
    latestTime = models.DateField(null=True, blank=True)

# for more informatio see
#https://app.getswift.co/ApiDocs/ResourceModel?modelName=DeliveryEventWebhookModel
class DeliveryEventWebhookModel(models.Model):
    eventName = models.CharField(max_length=200)
    url = models.CharField(max_length=300)

#refer to the Getswift api documentation for fields descrition
# https://app.getswift.co/ApiDocs/ResourceModel?modelName=DeliveryBookingModel
class DeliveryBookingModel(models.Model):
    reference = models.CharField(max_length=50, null=True, blank=True)
    deliveryInstruction = models.CharField(max_length=2000, blank=True, null=True)
    itemsRequirePurchase = models.BooleanField(default=False)
    items = models.ForeignKey(DeliveryBookingItemModel, on_delete=models.CASCADE, null=True, blank=True)
    pickupTime = models.DateField(null=True, blank=True);
    pickupDetail = models.ForeignKey(DeliveryBookingLocationModel, on_delete=models.CASCADE, related_name='pickup_detail')
    dropoffWindow = models.ForeignKey(TimeFrameModel, on_delete=models.CASCADE)
    dropoffDetail = models.ForeignKey(DeliveryBookingLocationModel, on_delete=models.CASCADE, related_name='dropoff_detail')
    customerFee = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    customerReference = models.CharField(max_length=50, null=True, blank=True)
    tax = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    taxInclusivePrice = models.NullBooleanField()
    tip = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    driverFeePercentage = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    driverMatchCode = models.CharField(max_length=200)
    deliverySequence = models.IntegerField()
    webhooks = models.ForeignKey(DeliveryEventWebhookModel, on_delete=models.CASCADE, null=True, blank=True)
    template = models.CharField(max_length=4000)