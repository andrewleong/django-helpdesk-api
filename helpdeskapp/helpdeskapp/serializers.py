from rest_framework import serializers
from django.contrib.auth.models import User
from ticket.models import Ticket, Category

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, style={"input_type":"password"})
    is_staff = serializers.BooleanField(default=False)

    # Will call when create a new user object
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    # returns existing user instance
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = (
            'id',
            'title',
            'content',
            'category',
            'ticket_id',
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
