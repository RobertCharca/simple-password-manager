from rest_framework import serializers

from pmb_base.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_us
        fields = "__all__"
        read_only_fields = ['us_pub_date', 'us_upd_date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_cat
        fields = "__all__"
        read_only_fields = ['cat_pub_date', 'cat_upd_date']

class ItemWebPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemWebPage_iwp
        fields = "__all__"
        read_only_fields = ['iwp_pub_date', 'iwp_upd_date']

class ItemPaymentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPaymentCard_ipc
        fields = "__all__"
        read_only_fields = ['ipc_pub_date', 'ipc_upd_date']