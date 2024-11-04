# Generated by Django 3.2.12 on 2024-05-29 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('veiculo', '0003_veiculo_foto'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('descricao', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncios_realizados', to=settings.AUTH_USER_MODEL)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anuncios', to='veiculo.veiculo')),
            ],
        ),
    ]