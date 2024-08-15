from django.contrib import admin
from account.models import Account, KYC
from import_export.admin import ImportExportModelAdmin



class AccountAdminModel(ImportExportModelAdmin):
    list_editable = ['account_status', 'account_balance', 'kyc_submitted', 'kyc_approved'] 
    list_display = ['user', 'account_number' ,'account_status', 'account_balance', 'kyc_submitted', 'kyc_approved'] 
    list_filter = ['account_status']


class KYCAdminModel(ImportExportModelAdmin):
    list_display = ['user', 'identity_type', 'identity_number', 'identity_image'] 
    list_filter = ['identity_type']




admin.site.register(Account, AccountAdminModel)
admin.site.register(KYC, KYCAdminModel)

