from django.db import models

#Customer Model
class Customer(models.Model):
    #Customer's email and name
    name = models.CharField(max_length=100) # Name of the customer
    email = models.EmailField(max_length=100,unique=True) # Email of the customer

    def __str__(self):
        return self.name #Output for customer's name
    
#Order Model
class Order(models.Model):
    #Order for one customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders') # Foreign key referencing the customer model
    order_date = models.DateField(auto_now_add=True) # Date the order was made
    total_amount = models.DecimalField(max_digits=10, decimal_places=2) # Total cost of the order

    def __str__(self):
     return f"Order by {self.customer.name} on {self.order_date} - ${self.total_amount}"

