from django.forms import widgets
from rest_framework import serializers
from akrasia_messages.models import Message

class MessageSerializer(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	urlprofile = serializers.CharField(required=False, allow_blank=True, max_length=100)
	message = serializers.CharField(required=False, allow_blank=True, max_length=100)
	name = serializers.CharField(required=False, allow_blank=True, max_length=100)

	def create(self, validated_data):
		return Message.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.message = validated_data.get('message', instance.message)
		instance.name = validated_data.get('name', instance.name)
		instance.urlprofile = validated_data.get('urlprofile', instance.urlprofile)
