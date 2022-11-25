from rest_framework import serializers
from .models import Food

class FoodSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image must be smaller than 2MB.')

        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Height must be smaller than 4096px.')

        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Width must be smaller than 4096px.')

        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Food
        fields = [
            'id',
            'owner',
            'is_owner',
            'title',
            'content',
            'image',
            'created_on',
            'modified_on',
            'profile_id',
            'profile_image',
            'dress_code',
            'kids_friendly',
        ]
