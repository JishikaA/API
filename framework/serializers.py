from rest_framework import serializers

from framework.models import Employee, Student


class SnippetSerialize(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = "__all__"

class StudentSerialize(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields =('name','last_name','mark')