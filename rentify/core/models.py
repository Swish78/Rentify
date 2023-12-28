from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.name


class ToolItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='tool_pics/', null=True, blank=False)

    def __str__(self):
        return self.title


class Booking(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings_made')
    tool_item = models.ForeignKey(ToolItem, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tool_item.title} - {self.start_date} to {self.end_date}"

    def calculate_total_cost(self):
        days = (self.end_date - self.start_date).days
        total_cost = days * self.tool_item.price
        return total_cost


@receiver(post_save, sender=Booking)
def update_item_availability(sender, instance, **kwargs):
    if instance.is_confirmed:
        instance.tool_item.is_available = False
        instance.tool_item.save()


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_given')
    reviewee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews_received')
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField()

    def __str__(self):
        return f"{self.reviewer.username} -> {self.reviewee.username}: {self.rating}"
