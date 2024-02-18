import uuid
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.name


class MessageDetail(models.Model):
    message_detail_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    detail = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.detail

    class Meta:
        ordering = ['created_at']


class Message(models.Model):
    message_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    message_detail = models.OneToOneField(
        MessageDetail, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['updated_at', 'created_at']
