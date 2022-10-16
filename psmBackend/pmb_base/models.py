from django.db import models

# Create your models here.
class Users_us(models.Model):
    us_name = models.CharField(max_length=20)
    us_email = models.EmailField(max_length=200)
    us_master_password = models.CharField(max_length=64, null=False)
    us_mp_hint = models.CharField(max_length=200, null=True)
    us_pub_date = models.DateTimeField('date_published')
    us_upd_date = models.DateTimeField('date_updated')

    def __str__(self):
        return self.us_name

class Category_cat(models.Model):
    user = models.ForeignKey(Users_us, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=50)
    cat_description = models.TextField()
    cat_pub_date = models.DateTimeField('date_published')
    cat_upd_date = models.DateTimeField('date_updated')

class ItemWebPage_iwp(models.Model):
    principal_user = models.ForeignKey(Users_us, on_delete=models.CASCADE)
    user_category = models.ForeignKey(Category_cat, on_delete=models.CASCADE)
    iwp_name = models.CharField(max_length=50, null=False)
    iwp_url = models.URLField(null=False)
    iwp_username = models.CharField(max_length=20, null=False)
    iwp_password = models.CharField(max_length=64, null=False)
    iwp_description = models.TextField()
    iwp_pub_date = models.DateTimeField('date_published')
    iwp_upd_date = models.DateTimeField('date_updated')

class ItemPaymentCard_ipc(models.Model):
    principal_user = models.ForeignKey(Users_us, on_delete=models.CASCADE)
    ipc_name = models.CharField(max_length=50, null=False)
    ipc_company = models.CharField(max_length=30, null=False)
    ipc_card_number = models.CharField(max_length=20, null=False)
    ipc_card_pin = models.IntegerField(null=False)
    ipc_card_strt_date = models.DateField(null=False)
    ipc_card_exp_date = models.DateField(null=False)
    ipc_card_description = models.TextField()
    ipc_pub_date = models.DateTimeField('date_published')
    ipc_upd_date = models.DateTimeField('date_updated')