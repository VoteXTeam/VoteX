# Generated by Django 4.2.1 on 2023-06-05 13:17

import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('VoteXApi', '0007_remove_customuser_register_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='organization',
            field=models.CharField(choices=[('softserve', 'SoftServe'), ('google', 'Google'), ('bing', 'Bing')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='region',
            field=models.CharField(choices=[('vinnytsia', 'Vinnytsia'), ('volyn', 'Volyn'), ('dnipropetrovsk', 'Dnipropetrovsk'), ('donetsk', 'Donetsk'), ('zhytomyr', 'Zhytomyr'), ('zakarpattia', 'Zakarpattia'), ('zaporizhzhia', 'Zaporizhzhia'), ('ivano-frankivsk', 'Ivano-Frankivsk'), ('kyiv', 'Kyiv'), ('kirovohrad', 'Kirovohrad'), ('luhansk', 'Luhansk'), ('lviv', 'Lviv'), ('mykolaiv', 'Mykolaiv'), ('odesa', 'Odesa'), ('poltava', 'Poltava'), ('rivne', 'Rivne'), ('sumy', 'Sumy'), ('ternopil', 'Ternopil'), ('kharkiv', 'Kharkiv'), ('kherson', 'Kherson'), ('khmelnytskyi', 'Khmelnytskyi'), ('cherkasy', 'Cherkasy'), ('chernivtsi', 'Chernivtsi'), ('chernihiv', 'Chernihiv')], max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='election',
            name='end_of_voting',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 6, 16, 17, 24, 844740)),
        ),
        migrations.AlterField(
            model_name='election',
            name='organizations',
            field=models.CharField(choices=[('softserve', 'SoftServe'), ('google', 'Google'), ('bing', 'Bing')], max_length=45),
        ),
        migrations.AlterField(
            model_name='election',
            name='regions',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('vinnytsia', 'Vinnytsia'), ('volyn', 'Volyn'), ('dnipropetrovsk', 'Dnipropetrovsk'), ('donetsk', 'Donetsk'), ('zhytomyr', 'Zhytomyr'), ('zakarpattia', 'Zakarpattia'), ('zaporizhzhia', 'Zaporizhzhia'), ('ivano-frankivsk', 'Ivano-Frankivsk'), ('kyiv', 'Kyiv'), ('kirovohrad', 'Kirovohrad'), ('luhansk', 'Luhansk'), ('lviv', 'Lviv'), ('mykolaiv', 'Mykolaiv'), ('odesa', 'Odesa'), ('poltava', 'Poltava'), ('rivne', 'Rivne'), ('sumy', 'Sumy'), ('ternopil', 'Ternopil'), ('kharkiv', 'Kharkiv'), ('kherson', 'Kherson'), ('khmelnytskyi', 'Khmelnytskyi'), ('cherkasy', 'Cherkasy'), ('chernivtsi', 'Chernivtsi'), ('chernihiv', 'Chernihiv')], max_length=45),
        ),
    ]