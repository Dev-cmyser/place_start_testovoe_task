from django.db import models
import uuid

class BaseModel(models.Model):
    """Basic Model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
        
        
        
        
class Task(BaseModel):
    PRIORITY = (
        ('hight', "hight"),
        ('medium', "medium"),
        ('low', "low")
    )
    STATUS = (
        ('in progress', "in progress"),
        ('done', "done"),
        ('pending', "pending")
    )

    def __str__(self):
        return f'{self.title} |  {self.status} | {self.priority}'
    
    created_to = models.DateTimeField(null=True, blank=True)
    updated_to = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=6, choices=PRIORITY, default="low")
    status = models.CharField(max_length=30, choices=STATUS, default="pending")
    title = models.CharField(max_length=90)
    description = models.TextField()