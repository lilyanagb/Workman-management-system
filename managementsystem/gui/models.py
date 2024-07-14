from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CATEGORY = (
    ('Electrical tasks','Electrical tasks'),
    ('Furniture assembling','Furniture assembling'),
    ('Interior stain and paint','Interior stain and paint'),
    ('Plumbing','Plumbing'),
    ('Home upgrades','Home upgrades'),
    ('Window cleaning','Window cleaning'),
    ('Smart appliance installation','Smart appliance installation'),
)

STATUS_CHOICE = (
        ('taken', 'Taken'),
        ('active', 'Active'),
        ('completed', 'Completed'),
)

class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=80, choices=CATEGORY, null=True)
    order = models.CharField(max_length=150, null=True)
    status = models.CharField(choices=STATUS_CHOICE, max_length=20, null=True)

    def __str__(self):
        return f'{self.owner}-{self.category}-{self.order}'
    
class Mail(models.Model):
    take_order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'{self.take_order}-{self.date_time}'