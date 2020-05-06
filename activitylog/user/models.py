from django.db import models

# Create your models here.
class UsersMan(models.Model):
    s_no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    time_zone = models.CharField(max_length=50)
    #activity_periods = models.ForeignKey(Log, related_name='activity_periods', on_delete =models.CASCADE)

    class Meta:
        db_table="Users"
        managed = True