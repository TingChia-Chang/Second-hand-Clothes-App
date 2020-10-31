from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class ClothesList(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='image/')
    price = models.IntegerField(default=0)
    seller = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=200)
    comment = ArrayField(models.TextField(blank=True), blank=True)

# class ClothesList():
#     def __init__(self, id, name, url, picture, price, seller, amount, description, size):
#         self.id = id
#         self.name = name
#         self.url = url
#         self.picture = picture
#         self.price = price
#         self.seller = seller
#         self.amount = amount
#         self.description = description
#         self.size = size

# clothes1 = ClothesList(
#     1,
#     "Hokies Logo Hoodie",
#     "second_hand_clothes_app:clothes_detail",
#     "pictures/item4.png",
#     "20",
#     "Iris Chang",
#     "10",
#     "This hoodie is very comfortable. It was bought 3 months ago, so it is new.",
#     "S"
# )

# clothes2 = ClothesList(
#     2,
#     "Champion Sweater",
#     "second_hand_clothes_app:clothes_detail",
#     "pictures/item5.png",
#     "20",
#     "Jessica",
#     "20",
#     "This hoodie is very comfortable. It was bought 3 months ago, so it is new.",
#     "S"
# )

# clothes3 = ClothesList(
#     3,
#     "VT Logo Hoodie",
#     "second_hand_clothes_app:clothes_detail",
#     "pictures/item1.png",
#     "20",
#     "Sharon",
#     "20",
#     "This hoodie is very comfortable. It was bought 3 months ago, so it is new.",
#     "S"
# )

# clothes4 = ClothesList(
#     4,
#     "VT Logo Hoodie Red",
#     "second_hand_clothes_app:clothes_detail",
#     "pictures/item2.png",
#     "20",
#     "Tina",
#     "30",
#     "This hoodie is very comfortable. It was bought 3 months ago, so it is new.",
#     "S"
# )



# clothes = []
# clothes.append(clothes1)
# clothes.append(clothes2)
# clothes.append(clothes3)
# clothes.append(clothes4)

regular_user = {"username": "regular", "password": "regular"}
admin_user = {"username": "admin", "password": "admin"}

        
    