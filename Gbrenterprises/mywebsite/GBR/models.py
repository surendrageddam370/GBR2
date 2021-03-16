from django.db import models
import datetime
from django.contrib.auth.models import User


class ItemList(models.Model):
    item_name= models.CharField(max_length=20)
    item_quantity = models.CharField(max_length=5)
    item_gaze= models.CharField(max_length=20,null=True,blank=True)
    item_dimensions = models.CharField(max_length=5,null=True,blank=True)
    
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE,related_name="itemlist")
    Date = models.DateField(null=True)
    def __str__(self):
        return self.item_name

class AddItem(models.Model):
    itemlist= models.ForeignKey(ItemList,null=True, blank=True,on_delete=models.CASCADE)
    options_item = (("10mm షీట్(3x4)","10mm షీట్(3x4)"),("12mm షీట్(3x4)","12mm షీట్(3x4)"),("బాటం","బాటం"),("పట్టి","పట్టి"),("SPL","SPL"),("సపోర్ట్ L","సపోర్ట్ L"),("POP బ్యాగ్","POP బ్యాగ్"),("మేకులు","మేకులు"),("ఫ్యాన్ హుక్","ఫ్యాన్ హుక్"),("Star స్క్రూలు","Star స్క్రూలు"),("ఎంకర్ బోల్టులు","ఎంకర్ బోల్టులు"))
    item_name= models.CharField(max_length=20,choices=options_item,default="10mm షీట్(3x4)")
    options= (("0.40","0.40"),("0.45","0.45"),('0.50',"0.50"),("0.55","0.55"),("0.60","0.60"))
    item_dimensions = models.CharField(max_length=5,choices=options,null=True,blank=True)
    item_quantity = models.IntegerField(max_length=5,default='0')
    status=(("హెవీ","హెవీ"),("లైట్","లైట్"),("అల్ట్రా","అల్ట్రా"))
    item_gaze=models.CharField(max_length=20,choices=status,null=True,blank=True)
    Date = models.DateField(default=datetime.date.today)
    

    def __str__(self):
        return self.item_name
