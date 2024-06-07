from rest_framework import generics, status
from rest_framework.response import Response

from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    print('여기까지 오나요??')

    def create(self, request, *args, **kwargs):
        print('Create 시도는 하나요??')
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            blog_post = serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        if serializer.is_valid():
            blog_post = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
