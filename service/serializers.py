from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User, Product, Shop, Category, ProductInfo, Parameter, ProductParameter


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    type = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):

        email = data.get('email', None)
        password = data.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        return {
            'email': user.email,
            'username': user.username,
            'token': user.token,
            'type': user.type,
        }


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token', 'type',)

        read_only_fields = ('token',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance


# class ListShop(serializers.ModelSerializer):
#     class Meta:
#         model = Shop
#         fields = ('id', 'name', 'user', 'state',)
#
#
# class ListCategory(serializers.ModelSerializer):
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'shops', )
#

class ListUser(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'position', 'type', 'token' )


class ListProduct(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'category',)

# class ListProductInfo(serializers.ModelSerializer):
#
#     class Meta:
#         model = ProductInfo
#         fields = ('model', 'external_id','product', 'shop', 'quantity', 'price', 'price_rrc')


class ListParameter(serializers.ModelSerializer):

    class Meta:
        model = Parameter
        fields = ('name', )


class ListProductParameter(serializers.ModelSerializer):

    class Meta:
        model = ProductParameter
        fields = ('product_info', 'parameter','value')