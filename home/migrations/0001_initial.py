# Generated by Django 3.2.8 on 2021-12-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetailList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movieNm', models.TextField(verbose_name='movieNmEn')),
                ('prdtYear', models.TextField(verbose_name='prdtYear')),
                ('openDt', models.TextField(verbose_name='openDt')),
                ('showTm', models.TextField(verbose_name='showTm')),
                ('nations', models.TextField(verbose_name='nations')),
                ('genres', models.TextField(verbose_name='genres')),
                ('audits', models.TextField(verbose_name='audits')),
            ],
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('movieCd', models.TextField(default='0', verbose_name='movieCd')),
                ('movieNm', models.TextField(verbose_name='movieNmEn')),
                ('genreAlt', models.TextField(verbose_name='genreAlt')),
                ('prdtYear', models.TextField(verbose_name='prdtYear')),
                ('nationAlt', models.TextField(verbose_name='nationAlt')),
            ],
        ),
    ]
