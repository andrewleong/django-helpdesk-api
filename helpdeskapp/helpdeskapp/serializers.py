from rest_framework import serializers
from django.contrib.auth.models import User
from ticket.models import Ticket, Category

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url',
            'username',
            'email',
            'is_staff'
        )

class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'id',
            'title',
            'content',
            'category',
            'ticker_id',
            'user',
            'created_date',
            'updated_date',
        )

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
        )
