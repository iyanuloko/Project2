from django.db import models
from django.conf import settings

class Category(models.Model):
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.category

class Severity(models.Model):
    role = (
        ('Low', "Low"),
        ('Medium', "Medium"),
        ('High', "High")
    )
    roles = models.CharField(max_length=10, choices=role, default='Low')
    def __str__(self):
        return self.roles

class RSev(models.Model):
    sev = (
        ('Low', "Low"),
        ('Medium', "Medium"),
        ('High', "High")
    )
    severity = models.CharField(max_length=10, choices=sev, default='Low')
    def __str__(self):
        return self.severity

class RiskRegister(models.Model):
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    explanation = models.TextField(blank=True)
    roles = models.ForeignKey(Severity, on_delete=models.CASCADE)
    responderID = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_responderID', blank=True, null=True, on_delete=models.CASCADE)
    severity = models.ForeignKey(RSev, blank=True, null=True, on_delete=models.CASCADE)
    action_taken_explanation = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

