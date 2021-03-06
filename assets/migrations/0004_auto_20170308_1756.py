# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-08 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20170308_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(choices=[(b'Server', '\u670d\u52a1\u5668'), (b'Network', '\u7f51\u7edc\u8bbe\u5907'), (b'Storage', '\u5b58\u50a8\u8bbe\u5907'), (b'Security', '\u5b89\u5168\u8bbe\u5907'), (b'Equipment', '\u673a\u623f\u8bbe\u5907'), (b'Switch', '\u4ea4\u6362\u673a'), (b'Router', '\u8def\u7531\u5668'), (b'Firewall', '\u9632\u706b\u5899'), (b'NLB', 'NetScaler'), (b'Wireless', '\u65e0\u7ebfAP'), (b'Software', '\u8f6f\u4ef6\u8d44\u4ea7'), (b'Others', '\u5176\u5b83\u7c7b')], default=b'Server', max_length=64),
        ),
    ]
