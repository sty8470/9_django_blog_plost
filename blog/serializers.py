from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'

    def validate(self, data):
        required_fields = ['name', 'title', 'contents']
        unique_fields = ['name', 'title', 'contents']

        # 필수 필드 검사
        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError({field: f"{field} is required"})

        # name 필드를 제외한 중복 검사 
        if BlogPost.objects.filter(title=data.get('title'), contents=data.get('contents')).exists():
            raise serializers.ValidationError({field: f"A blog post with this title and contents already exists."})

        return data

    def create(self, validated_data):
        instance = BlogPost.objects.create(**validated_data)
        # 로그 기록 예시
        print(f"New blog post created: {instance.title}")
        return instance
