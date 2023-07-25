from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    CHOICES = (
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    )
    status = models.CharField(max_length=50, choices=CHOICES, default='Not Started')
    assigned_team_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_member')
    CHOICE = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    priority = models.CharField(max_length=50, choices=CHOICE, default='low')

    def __str__(self):
        return self.title
