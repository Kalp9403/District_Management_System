# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Citizens(models.Model):
    c_id = models.IntegerField(primary_key=True)
    c_name = models.CharField(max_length=50)
    c_email = models.CharField(max_length=60)
    c_contact_no = models.CharField(max_length=50)
    c_dob = models.DateField()
    c_address = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'citizens'


class Complaints(models.Model):
    cp_id = models.IntegerField(primary_key=True)
    cp_issue = models.CharField(max_length=100)
    cp_registration_date = models.DateField()
    cp_location = models.CharField(max_length=50)
    c = models.ForeignKey(Citizens, models.DO_NOTHING)
    td = models.ForeignKey('Tehsildars', models.DO_NOTHING)
    l = models.ForeignKey('LawEnforcementAgency', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'complaints'


class Feedback(models.Model):
    f_rating = models.IntegerField(primary_key=True)
    f_review = models.CharField(max_length=100)
    cp = models.ForeignKey(Complaints, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'feedback'
        unique_together = (('f_rating', 'f_review', 'cp'),)


class Issue(models.Model):
    r_reason = models.CharField(primary_key=True, max_length=100)
    r_reopen_date = models.DateField()
    cp = models.ForeignKey(Complaints, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'issue'
        unique_together = (('r_reason', 'r_reopen_date', 'cp'),)


class LawEnforcementAgency(models.Model):
    l_id = models.IntegerField(primary_key=True)
    l_name = models.CharField(max_length=50)
    l_helpline_no = models.CharField(max_length=50)
    td = models.ForeignKey('Tehsildars', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'law_enforcement_agency'


class Status(models.Model):
    ts_status = models.CharField(primary_key=True, max_length=50)
    ts_duration = models.IntegerField()
    cp = models.ForeignKey(Complaints, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'status'
        unique_together = (('ts_status', 'ts_duration', 'cp'),)


class SubDivisionOfficer(models.Model):
    s_zone = models.CharField(primary_key=True, max_length=10)
    s_name = models.CharField(max_length=50)
    s_email = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'sub_division_officer'


class Tehsil(models.Model):
    t_id = models.IntegerField(primary_key=True)
    t_name = models.CharField(max_length=50)
    t_office_address = models.CharField(max_length=100)
    td = models.ForeignKey('Tehsildars', models.DO_NOTHING)
    s_zone = models.ForeignKey(SubDivisionOfficer, models.DO_NOTHING, db_column='s_zone')

    class Meta:
        managed = False
        db_table = 'tehsil'


class Tehsildars(models.Model):
    td_id = models.IntegerField(primary_key=True)
    td_name = models.CharField(max_length=50)
    td_email = models.CharField(max_length=60)
    td_contact_no = models.CharField(max_length=50)
    td_salary = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tehsildars'
