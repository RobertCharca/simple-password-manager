from rest_framework import serializers

from pmb_base.models import *

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_us
        fields = "__all__"
        read_only_fields = ['us_pub_date', 'us_upd_date']