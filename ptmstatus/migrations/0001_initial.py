# Generated by Django 2.2.2 on 2019-06-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PtmStatus',
            fields=[
                ('ptm_id', models.IntegerField()),
                ('pmg_id', models.IntegerField()),
                ('ptm_rf_id', models.AutoField(primary_key=True, serialize=False)),
                ('last_status_time', models.DateTimeField(blank=True, null=True)),
                ('last_touch_time', models.DateTimeField(blank=True, null=True)),
                ('dimming_value', models.IntegerField()),
                ('last_access_ptm_time', models.DateTimeField(blank=True, db_column='last_access_PTM_time', null=True)),
                ('current_consumption', models.TextField(blank=True, null=True)),
                ('cummulative_consumption', models.IntegerField(blank=True, null=True)),
                ('critical_cnt', models.IntegerField(blank=True, null=True)),
                ('error_cnt', models.IntegerField(blank=True, null=True)),
                ('warning_cnt', models.IntegerField(blank=True, null=True)),
                ('info_cnt', models.IntegerField(blank=True, null=True)),
                ('dimming_mode', models.IntegerField()),
                ('i_rms', models.TextField(blank=True, null=True)),
                ('u_rms', models.TextField(blank=True, null=True)),
                ('p_w', models.TextField(blank=True, null=True)),
                ('cos_fi', models.TextField(blank=True, null=True)),
                ('temp', models.IntegerField(blank=True, null=True)),
                ('luxmeter_value', models.IntegerField()),
                ('luxmeter_value_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Ptm_status',
                'managed': False,
            },
        ),
    ]
