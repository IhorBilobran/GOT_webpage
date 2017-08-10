from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from accounts.models import Post
from .serializers import PostSerializer

@api_view(['GET', 'POST'])
def post_list(request, format=None):

	if request.method == 'GET':
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(owner=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
