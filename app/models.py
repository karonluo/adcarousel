# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Adcarousel(models.Model):
    id = models.CharField(primary_key=True, max_length=36, db_comment='轮播唯一编号')
    isselected = models.TextField(db_column='isSelected', blank=True, null=True, db_comment='是否参与轮播')  # Field name made lowercase. This field type is a guess.
    showtimeout = models.IntegerField(db_column='showTimeout', blank=True, null=True, db_comment='配置显示多少秒')  # Field name made lowercase.
    picpath = models.CharField(db_column='picPath', max_length=255, blank=True, null=True, db_comment='轮播图片地址')  # Field name made lowercase.
    fontcolor = models.CharField(db_column='fontColor', max_length=32, blank=True, null=True, db_comment='文字颜色')  # Field name made lowercase.
    fontposition = models.CharField(db_column='fontPosition', max_length=16, blank=True, null=True, db_comment='文字尺寸')  # Field name made lowercase.
    fontsize = models.SmallIntegerField (db_column='fontSize',blank=True, null=True, db_comment='文字位置')  # Field name made lowercase.
    orderkey = models.IntegerField(db_column='orderKey', blank=True, null=True, db_comment='轮播顺序号')  # Field name made lowercase. This field type is a guess.
    word = models.CharField(db_column='word', max_length=16, blank=True, null=True, db_comment='文字内容')  # Field name made lowercase.
    createby = models.CharField(db_column='createBy', max_length=32, blank=True, null=True, db_comment='创建人')  # Field name made lowercase.
    createat = models.DateTimeField(db_column='createAt', blank=True, null=True, db_comment='创建日期')  # Field name made lowercase.
    updateby = models.CharField(db_column='updateBy', max_length=255, blank=True, null=True, db_comment='更新人')  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True, db_comment='更新日期')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_adcarousel'
