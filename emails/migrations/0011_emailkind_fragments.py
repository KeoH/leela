# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-24 10:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import emails.models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0010_emailentry_thirdparty_reject'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailKindFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='content fragment name')),
                ('description', models.CharField(default='', max_length=300, verbose_name='description')),
                ('content', models.TextField(verbose_name='template')),
                ('is_plain', models.BooleanField(default=False, help_text='tells if the content is should be used in plain text', verbose_name='is plain')),
                ('default_context', jsonfield.fields.JSONField(blank=True, default={}, verbose_name='default template context')),
            ],
        ),
        migrations.CreateModel(
            name='FragmentEmbeddedImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placeholder_name', models.CharField(max_length=100)),
                ('content_id', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to=emails.models.get_image_filename)),
                ('fragment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='emails.EmailKindFragment')),
            ],
            options={
                'ordering': ['fragment', 'placeholder_name'],
            },
        ),
        migrations.RemoveField(
            model_name='emailkind',
            name='images',
        ),
        migrations.AlterField(
            model_name='embeddedimage',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='emails.EmailKind'),
        ),
        migrations.AddField(
            model_name='emailkind',
            name='fragments',
            field=models.ManyToManyField(related_name='kinds', to='emails.EmailKindFragment'),
        ),
        migrations.AlterUniqueTogether(
            name='fragmentembeddedimage',
            unique_together=set([('fragment', 'placeholder_name')]),
        ),
    ]
