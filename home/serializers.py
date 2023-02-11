import string
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Todo, Time


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField() 
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'Incorrect username or password.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
        )

        token, _ = Token.objects.get_or_create(user=user)

        return {
            'username': user.username,
            'token': token
        }

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'

    def validate(self, data):
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        
        if start_time > end_time:
            raise serializers.ValidationError({'start_time': 'Start time must be before end time.'})
        
        return data

class TodoSerializer(serializers.ModelSerializer):
    time = TimeSerializer()
    # time_ = serializers.PrimaryKeyRelatedField(queryset=Time.objects.all(), write_only=True)
    # time_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Todo
        # exclude=['user']
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
        depth = 1

    def validate_todo_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Todo title should have at least 5 characters")

        # if not value.isalpha():
        #     raise serializers.ValidationError("Todo title should only contain letters.")

        if any(char.isdigit() or char in string.punctuation for char in value):
            raise serializers.ValidationError("Todo title cannot contain numbers or special characters.")
        return value
    
    def validate_todo_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Todo description should have at least 10 characters")
        return value


    # def create(self, validated_data):
    #     time = validated_data.pop('time_')
    #     validated_data['time'] = time
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     time = validated_data.pop('time_')
    #     validated_data['time'] = time
    #     return super().update(instance, validated_data)