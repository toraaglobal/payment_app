from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, AccountViewSet, KYCViewSet, TransactionViewSet, NotificationViewSet, CreditCardViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)
router.register("accounts", AccountViewSet)
router.register("kycs", KYCViewSet)
router.register("transactions", TransactionViewSet)
router.register("notifications", NotificationViewSet)
router.register("creditcards", CreditCardViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
