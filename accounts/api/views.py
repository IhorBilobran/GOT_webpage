from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import Post, Profile
from .serializers import PostSerializer, UserSerializer, ProfileSerializer


class PostList(APIView):

	def get(self, request, format=None):
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = PostSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(owner=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):

    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        Post = self.get_object(pk)
        serializer = PostSerializer(Post)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Post = self.get_object(pk)
        serializer = PostSerializer(Post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Post = self.get_object(pk)
        Post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):

	def get(self, request, format=None):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

	def get_object(self, pk):
		try:
			return User.objects.get(pk=pk)
		except User.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		user = self.get_object(pk)
		serializer = UserSerializer(user, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileList(APIView):

	def get(self, request, format=None):
		profile = Profile.objects.all()
		serializer = ProfileSerializer(profile, many=True)
		return Response(serializer.data)


class ProfileDetail(APIView):

	def get_object(self, pk):
		try:
			return Profile.objects.get(pk=pk)
		except Profile.DoesNotExist:
			return Reponse(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk, format=None):
		profile = self.get_object(pk)
		serializer = ProfileSerializer(profile)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		profile = self.get_object(pk)
		serializer = ProfileSerializer(profile, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
