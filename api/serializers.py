from api.models import Category, Comment, Genre, Review, Title, User
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        return GenreSerializer(value).data


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        return CategorySerializer(value).data


class TitleSerializer(serializers.ModelSerializer):
    genre = GenreField(
        many=True, slug_field='slug', queryset=Genre.objects.all()
    )
    category = CategoryField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        fields = '__all__'
        model = Title


class TitleSerializerWithRating(serializers.ModelSerializer):
    genre = GenreField(
        many=True, slug_field='slug', queryset=Genre.objects.all()
    )
    category = CategoryField(
        slug_field='slug', queryset=Category.objects.all()
    )
    rating = serializers.FloatField()

    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('first_name', 'last_name', 'username',
                  'bio', 'email', 'role', 'confirmation_code')
        model = User


class ConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class CheckConfirmationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    confirmation_code = serializers.CharField(required=True)


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate(self, data):
        user = self.context['request'].user
        title = self.context['view'].kwargs.get('title_id')
        if (self.context['request'].method == 'POST'
           and Review.objects.filter(author=user, title=title).exists()):
            raise serializers.ValidationError('Вы уже оставили отзыв.')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
