from rest_framework import serializers
from . models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [ 'firstName', 'lastName', 'ssn', 'age' ]

    def validate(self, attrs):
        ssn = attrs.get("ssn")
        age = attrs.get("age")
        if len(ssn) != 9:
            raise serializers.ValidationError("ssn must be 9 digits.")
        if age > 130 or age < 18:
            raise serializers.ValidationError("age must be between 18 and 130")
        return attrs

