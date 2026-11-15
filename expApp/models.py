from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE

class Expense(models.Model):


    CATEGORY_CHOICES=(
        ("food","food"),
        ("bill","bill"),
        ("fuel","fuel")
    )

    PAYMENT_CHOICES=(
        ("upi","UPI"),
        ("card","CARD")
    )

    title=models.CharField(max_length=100)
    amount=models.DecimalField(max_digits=8,decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(User,on_delete=CASCADE)
    payment=models.CharField(max_length=20,choices=PAYMENT_CHOICES,default="UPI")
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES,default="food")

    def __str__(self):
        return f"{self.title}-{self.amount}"
