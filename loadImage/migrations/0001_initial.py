

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='imageLoad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_img', models.CharField(max_length=255)),
                ('url_img', models.ImageField(upload_to='img/')),
                ('format_img', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edite', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]