from django.db import models

# Create your models here.

class SalesReport(models.Model):
    """Daily/Weekly/Monthly sales reports"""
    PERIOD_CHOICES = [
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('yearly', 'Yearly'),
    ]
    
    report_id = models.CharField(max_length=100, unique=True, db_index=True)
    period_type = models.CharField(max_length=20, choices=PERIOD_CHOICES)
    period_start = models.DateField()
    period_end = models.DateField()
    total_sales = models.DecimalField(max_digits=12, decimal_places=2)
    total_orders = models.IntegerField()
    total_items_sold = models.IntegerField()
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-period_start']
    
    def __str__(self):
        return f"{self.period_type} Report: {self.period_start} to {self.period_end}"


class ProductAnalytics(models.Model):
    """Analytics for product performance"""
    product_id = models.CharField(max_length=100, db_index=True)
    product_name = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    add_to_cart_count = models.IntegerField(default=0)
    purchases = models.IntegerField(default=0)
    revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    report_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-report_date', '-revenue']
    
    def __str__(self):
        return f"{self.product_name} - {self.report_date}"


class CustomerInsight(models.Model):
    """Customer behavior insights"""
    customer_email = models.EmailField(db_index=True)
    total_orders = models.IntegerField(default=0)
    total_spent = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    last_order_date = models.DateField(null=True, blank=True)
    customer_segment = models.CharField(max_length=50, blank=True)
    lifetime_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-total_spent']
    
    def __str__(self):
        return f"{self.customer_email} - Segment: {self.customer_segment}"


class PerformanceMetric(models.Model):
    """Key performance indicators"""
    METRIC_TYPE_CHOICES = [
        ('revenue', 'Revenue'),
        ('orders', 'Orders'),
        ('customers', 'Customers'),
        ('products', 'Products'),
        ('traffic', 'Traffic'),
        ('conversion', 'Conversion Rate'),
    ]
    
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPE_CHOICES)
    metric_value = models.DecimalField(max_digits=15, decimal_places=2)
    metric_date = models.DateField()
    comparison_period_value = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    percentage_change = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-metric_date', 'metric_type']
    
    def __str__(self):
        return f"{self.metric_type}: {self.metric_value} on {self.metric_date}"
