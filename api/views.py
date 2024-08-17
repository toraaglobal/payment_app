from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import UserSerializer,AccountSerializer,KYCSerializer,TransactionSerializer,NotificationSerializer,CreditCardSerializer
from userauths.models import User
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

from account.models import Account, KYC
from core.models import Transaction, Notification, CreditCard



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )



class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user = request.user
        ref_code = request.data.get("ref_code")
        account_status = request.data.get("account_status")
        kyc_submitted = request.data.get("kyc_submitted")
        kyc_approved = request.data.get("kyc_approved")
        recommended_by = request.data.get("recommended_by")

        new_account = Account.objects.create(
            user=user,
            ref_code=ref_code,
            account_status=account_status,
            kyc_submitted=kyc_submitted,
            kyc_approved=kyc_approved,
            recommended_by=recommended_by
        )
        return Response({'message': 'Account Created'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['GET'])
    def kyc(self, request, pk=None):
        account = self.get_object()
        kyc = KYC.objects.filter(account=account)
        serializer = KYCSerializer(kyc, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'])
    def transactions(self, request, pk=None):
        account = self.get_object()
        transactions = account.transactions.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'])
    def notifications(self, request, pk=None):
        account = self.get_object()
        notifications = account.notifications.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'])
    def credit_cards(self, request, pk=None):
        account = self.get_object()
        credit_cards = account.credit_cards.all()
        serializer = CreditCardSerializer(credit_cards, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['GET'])
    def balance(self, request, pk=None):
        account = self.get_object()
        balance = account.balance
        return Response({'balance': balance})
    
    @action(detail=True, methods=['GET'])
    def account_status(self, request, pk=None):
        account = self.get_object()
        account_status = account.account_status
        return Response({'account_status': account_status})
    
    @action(detail=True, methods=['GET'])
    def kyc_status(self, request, pk=None):
        account = self.get_object()
        kyc_status = account.kyc_approved
        return Response({'kyc_status': kyc_status})
    
    @action(detail=True, methods=['GET'])
    def account_number(self, request, pk=None):
        account = self.get_object()
        account_number = account.account_number
        return Response({'account_number': account_number})
    
    @action(detail=True, methods=['GET'])
    def account_user(self, request, pk=None):
        account = self.get_object()
        account_user = account.user
        return Response({'account_user': account_user})
    
    @action(detail=True, methods=['GET'])
    def account_created_at(self, request, pk=None):
        account = self.get_object()
        account_created_at = account.created_at
        return Response({'account_created_at': account_created_at})
    
    @action(detail=True, methods=['GET'])
    def account_kyc_submitted(self, request, pk=None):
        account = self.get_object()
        account_kyc_submitted = account.kyc_submitted
        return Response({'account_kyc_submitted': account_kyc_submitted})
    
    @action(detail=True, methods=['GET'])
    def account_recommended_by(self, request, pk=None):
        account = self.get_object()
        account_recommended_by = account.recommended_by
        return Response({'account_recommended_by': account_recommended_by})
    
    @action(detail=True, methods=['GET'])
    def account_kyc(self, request, pk=None):
        account = self.get_object()
        account_kyc = account.kyc
        return Response({'account_kyc': account_kyc})
    
    @action(detail=True, methods=['GET'])
    def account_transactions(self, request, pk=None):
        account = self.get_object()
        account_transactions = account.transactions
        return Response({'account_transactions': account_transactions})
    
    @action(detail=True, methods=['GET'])
    def account_notifications(self, request, pk=None):
        account = self.get_object()
        account_notifications = account.notifications
        return Response({'account_notifications': account_notifications})
    
    @action(detail=True, methods=['GET'])
    def account_credit_cards(self, request, pk=None):
        account = self.get_object()
        account_credit_cards = account.credit_cards
        return Response({'account_credit_cards': account_credit_cards})
    
    @action(detail=True, methods=['GET'])
    def account_balance(self, request, pk=None):
        account = self.get_object()
        account_balance = account.balance
        return Response({'account_balance': account_balance})
    
    @action(detail=True, methods=['GET'])
    def account_account_status(self, request, pk=None):
        account = self.get_object()
        account_account_status = account.account_status
        return Response({'account_account_status': account_account_status})
    
    @action(detail=True, methods=['GET'])
    def account_kyc_status(self, request, pk=None):
        account = self.get_object()
        account_kyc_status = account.kyc_approved
        return Response({'account_kyc_status': account_kyc_status})
    
    @action(detail=True, methods=['GET'])
    def account_account_number(self, request, pk=None):
        account = self.get_object()
        account_account_number = account.account_number
        return Response({'account_account_number': account_account_number})
    
    @action(detail=True, methods=['GET'])
    def account_account_user(self, request, pk=None):
        account = self.get_object()
        account_account_user = account.user
        return Response({'account_account_user': account_account_user})
    
    @action(detail=True, methods=['GET'])
    def account_account_created_at(self, request, pk=None):
        account = self.get_object()
        account_account_created_at = account.created_at
        return Response({'account_account_created_at': account_account_created_at})
    
    @action(detail=True, methods=['GET'])
    def account_account_kyc_submitted(self, request, pk=None):
        account = self.get_object()
        account_account_kyc_submitted = account.kyc_submitted
        return Response({'account_account_kyc_submitted': account_account_kyc_submitted})
    
    @action(detail=True, methods=['GET'])
    def account_account_recommended_by(self, request, pk=None):
        account = self.get_object()
        account_account_recommended_by = account.recommended_by
        return Response({'account_account_recommended_by': account_account_recommended_by})
    
    @action(detail=True, methods=['GET'])
    def account_account_kyc(self, request, pk=None):
        account = self.get_object()
        account_account_kyc = account.kyc
        return Response({'account_account_kyc': account_account_kyc})
    
    @action(detail=True, methods=['GET'])
    def account_account_transactions(self, request, pk=None):
        account = self.get_object()
        account_account_transactions = account.transactions
        return Response({'account_account_transactions': account_account_transactions})
    

class KYCViewSet(viewsets.ModelViewSet):
    queryset = KYC.objects.all()
    serializer_class = KYCSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

class CreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


class AccountTransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        account = self.request.user.account
        return account.transactions.all()

    def create(self, request, *args, **kwargs):
        account = request.user.account

        sender = request.user
        reciever = account.user

        sender_account = request.user.account
        reciever_account = account

        amount = request.data.get("amount")
        description = request.data.get("description")

        new_request = Transaction.objects.create(
            user=request.user,
            amount=amount,
            description=description,

            sender=sender,
            reciever=reciever,

            sender_account=sender_account,
            reciever_account=reciever_account,

            status="request_processing",
            transaction_type="request"
        )
        return Response({'message': 'Transaction Request Sent'}, status=status.HTTP_200_OK)


class AccountNotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        account = self.request.user.account
        return account.notifications.all()

    def create(self, request, *args, **kwargs):
        account = request.user.account

        notification_type = request.data.get("notification_type")
        amount = request.data.get("amount")

        new_notification = Notification.objects.create(
            user=request.user,
            notification_type=notification_type,
            amount=amount,
            is_read=False
        )
        return Response({'message': 'Notification Sent'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def mark_read(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = True
        notification.save()
        return Response({'message': 'Notification Marked as Read'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def mark_unread(self, request, pk=None):
        notification = self.get_object()
        notification.is_read = False
        notification.save()
        return Response({'message': 'Notification Marked as Unread'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def mark_all_read(self, request, pk=None):
        notifications = self.get_queryset()
        for notification in notifications:
            notification.is_read = True
            notification.save()
        return Response({'message': 'All Notifications Marked as Read'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def mark_all_unread(self, request, pk=None):
        notifications = self.get_queryset()
        for notification in notifications:
            notification.is_read = False
            notification.save()
        return Response({'message': 'All Notifications Marked as Unread'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete(self, request, pk=None):
        notification = self.get_object()
        notification.delete()
        return Response({'message': 'Notification Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_all(self, request, pk=None):
        notifications = self.get_queryset()
        for notification in notifications:
            notification.delete()
        return Response({'message': 'All Notifications Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_read(self, request, pk=None):
        notifications = self.get_queryset()
        for notification in notifications:
            if notification.is_read:
                notification.delete()
        return Response({'message': 'All Read Notifications Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_unread(self, request, pk=None):
        notifications = self.get_queryset()
        for notification in notifications:
            if not notification.is_read:
                notification.delete()
        return Response({'message': 'All Unread Notifications Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_all_read(self, request, pk=None):
        notifications = self.get_queryset()
        for notification in notifications:
            if notification.is_read:
                notification.delete()
        return Response({'message': 'All Read Notifications Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_all_unread(self, request, pk=None):
        notifications = self.get_queryset()
        for notification in notifications:
            if not notification.is_read:
                notification.delete()
        return Response({'message': 'All Unread Notifications Deleted'}, status=status.HTTP_200_OK)
    

class AccountCreditCardViewSet(viewsets.ModelViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )

    def get_queryset(self):
        account = self.request.user.account
        return account.credit_cards.all()

    def create(self, request, *args, **kwargs):
        account = request.user.account

        name = request.data.get("name")
        number = request.data.get("number")
        month = request.data.get("month")
        year = request.data.get("year")
        cvv = request.data.get("cvv")
        amount = request.data.get("amount")
        card_type = request.data.get("card_type")
        card_status = request.data.get("card_status")

        new_credit_card = CreditCard.objects.create(
            user=request.user,
            name=name,
            number=number,
            month=month,
            year=year,
            cvv=cvv,
            amount=amount,
            card_type=card_type,
            card_status=card_status
        )
        account.credit_cards.add(new_credit_card)
        return Response({'message': 'Credit Card Added'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete(self, request, pk=None):
        credit_card = self.get_object()
        credit_card.delete()
        return Response({'message': 'Credit Card Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_all(self, request, pk=None):
        credit_cards = self.get_queryset()
        for credit_card in credit_cards:
            credit_card.delete()
        return Response({'message': 'All Credit Cards Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_all_active(self, request, pk=None):
        credit_cards = self.get_queryset()
        for credit_card in credit_cards:
            if credit_card.card_status == "active":
                credit_card.delete()
        return Response({'message': 'All Active Credit Cards Deleted'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['GET'])
    def delete_all_inactive(self, request, pk=None):
        credit_cards = self.get_queryset()
        for credit_card in credit_cards:
            if credit_card.card_status == "inactive":
                credit_card.delete()
        return Response({'message': 'All Inactive Credit Cards Deleted'}, status=status.HTTP_200_OK)    
                        