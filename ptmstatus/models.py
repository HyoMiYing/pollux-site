from django.db import models

class PtmStatus(models.Model):
    ptm_id = models.IntegerField()
    pmg_id = models.IntegerField()
    ptm_rf_id = models.AutoField(primary_key=True)
    last_status_time = models.DateTimeField(blank=True, null=True)
    last_touch_time = models.DateTimeField(blank=True, null=True)
    dimming_value = models.IntegerField()
    last_access_ptm_time = models.DateTimeField(db_column='last_access_PTM_time', blank=True, null=True)  # Field name made lowercase.
    current_consumption = models.TextField(blank=True, null=True)  # This field type is a guess.
    cummulative_consumption = models.IntegerField(blank=True, null=True)
    critical_cnt = models.IntegerField(blank=True, null=True)
    error_cnt = models.IntegerField(blank=True, null=True)
    warning_cnt = models.IntegerField(blank=True, null=True)
    info_cnt = models.IntegerField(blank=True, null=True)
    dimming_mode = models.IntegerField()
    i_rms = models.TextField(blank=True, null=True)  # This field type is a guess.
    u_rms = models.TextField(blank=True, null=True)  # This field type is a guess.
    p_w = models.TextField(blank=True, null=True)  # This field type is a guess.
    cos_fi = models.TextField(blank=True, null=True)  # This field type is a guess.
    temp = models.IntegerField(blank=True, null=True)
    luxmeter_value = models.IntegerField()
    luxmeter_value_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ptm_status'