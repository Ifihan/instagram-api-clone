# from .models import User
from rest_framework import serializers
from accounts.models import AppUser

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'username']

class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(min_length=8, write_only=True)
    password = serializers.CharField(min_length=8, write_only=True)
    password2 = serializers.CharField(min_length=8, write_only=True)

    
    def create(self, validated_data):
        user = AppUser.objects.create_user(**validated_data)
        return user

    def validate(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")

        if password != self.data.get('password2'):
            raise serializers.ValidationError("Passwords must match")

    class Meta:
        model = AppUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2')

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(min_length=8, write_only=True)
    password = serializers.CharField(min_length=8, write_only=True)
    token = serializers.SerializerMethodField()

    def get_token(self, obj):
        user = AppUser.objects.filter(email=self.data.get('email'))

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = AppUser.objects.filter(email=email).first()
            if user:
                if user.check_password(password):
                    return user
                else:
                    raise serializers.ValidationError("Incorrect password")
            else:
                raise serializers.ValidationError("User does not exist")

    class Meta:
        model = AppUser
        fields = ('email', 'password')


# email authentication serializer
# logout view serializer
# password reset view serializer