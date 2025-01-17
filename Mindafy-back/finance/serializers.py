from .models import DepositOptions, DepositProducts, SavingProducts, EtfProducts, SavingOptions
from rest_framework import serializers

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'

class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'

class EtfProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtfProducts
        fields = '__all__'