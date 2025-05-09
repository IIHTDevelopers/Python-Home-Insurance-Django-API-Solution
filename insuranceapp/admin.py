from django.contrib import admin
from insuranceapp.models import UserModel,QuoteModel,PolicyModel
class AdminUserModel(admin.ModelAdmin):
    list_display=['user_id','first_name','last_name','user_name']
admin.site.register(UserModel,AdminUserModel)

class AdminQuoteModel(admin.ModelAdmin):
    list_display=['quote_id','user_id','hno','city','state','country','residance_type','residance_use','detached_structure','market_value','year_build','square_foot_value','dwelling_style','roof_material','garage_type','numfullBaths','numhalfBaths','has_swimming_pool']
admin.site.register(QuoteModel,AdminQuoteModel)

class AdminPolicyModel(admin.ModelAdmin):
    list_display=['policy_key','quote_id','policy_term','policy_effective_date','policy_end_date','status']
admin.site.register(PolicyModel,AdminPolicyModel)
