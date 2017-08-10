from rest_framework import serializers

from accounts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'owner', 'title', 'text', 'created')
