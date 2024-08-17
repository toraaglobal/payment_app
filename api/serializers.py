from rest_framework import serializers
from userauths.models import User
from rest_framework.authtoken.models import Token

from account.models import Account, KYC
from core.models import Transaction, Notification, CreditCard



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'email', 'password', ]
        extra_kwargs = { 'password': {'write_only': True, 'required': True} }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user 


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'user', 'ref_code', 'account_status', 'created_at', 'kyc_submitted', 'kyc_approved', 'recommended_by']
        read_only_fields = ['ref_code', 'created_at', 'kyc_submitted', 'kyc_approved', 'recommended_by']
        ordering = ['-created_at']
    

class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYC
        fields = ['id', 'user', 'account', 'full_name', 'image', 'identity_image', 'marital_status', 'gender', 'identity_type', 'date_of_birth', 'signature', 'identity_number', 'country', 'state', 'city', 'mobile', 'fax', 'date']
        read_only_fields = ['date']
        ordering = ['-date']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_id', 'user', 'amount', 'description', 'reciever', 'sender', 'reciever_account', 'sender_account', 'status', 'transaction_type', 'date', 'updated']
        read_only_fields = ['transaction_id', 'date', 'updated']
        ordering = ['-date']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'notification_type', 'amount', 'is_read', 'date', 'nid']
        read_only_fields = ['date', 'nid']
        ordering = ['-date']


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ['id', 'user', 'card_id', 'name', 'number', 'month', 'year', 'cvv', 'amount', 'card_type', 'card_status', 'date']
        read_only_fields = ['card_id', 'date']
        ordering = ['-date']
