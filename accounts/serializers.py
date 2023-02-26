from rest_framework import serializers

from .models import Author, User


class AuthorRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=20, write_only=True)
    password = serializers.CharField(max_length=20, write_only=True)
    password_2 = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ['user']

    def validate(self, data):
        if data['password'].isdigit():
            raise serializers.ValidationError('В пароле должны быть буквы')

        if data['password'].isalpha():
            raise serializers.ValidationError('В пароле должны быть цифры')

        if len(data['password']) < 8:
            raise serializers.ValidationError('Пароль слишком короткий')

        if data['password'] != data['password_2']:
            raise serializers.ValidationError('Пароли должны совпадать')
        return data

    def create(self, validated_data):
        try:
            user = User(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()
        except Exception as e:
            raise serializers.ValidationError(f'Не удалось создать пользователя. {e}')
        else:
            author = Author.objects.create(
                user=user,
            )
            return author


class UserRegister(serializers.ModelSerializer):
    password = serializers.CharField(max_length=20, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

