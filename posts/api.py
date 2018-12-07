from rest_framework import serializers, viewsets
from .models import PersonalPost


class PersonalPostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PersonalPost
        fields = ('title', 'content')

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = self.context['request'].user
        post = PersonalPost.objects.create(user=user, **validated_data)
        return post


class PersonalPostViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalPostSerializer
    queryset = PersonalPost.objects.all()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return PersonalPost.objects.none()

        else:
            return PersonalPost.objects.filter(user=user)