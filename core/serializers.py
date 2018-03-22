from rest_framework import serializers

from core.models import CodeGenerated


class CodeGeneratedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodeGenerated
        fields = '__all__'
