from rest_framework.serializers import (
    CharField, 
    ModelSerializer,
    ValidationError)
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from django.db.models import Q

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(
                username = username,
            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.set_password(instance.password)
        instance.save()
        return instance



class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise ValidationError("required to login")

        user = User.objects.filter(
            Q(username=username)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("This Username is not valid")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again.")

        data["token"] = "SOME RANDOM TOKENf"

        
        return data


class UserListSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
        ]


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
        ]
