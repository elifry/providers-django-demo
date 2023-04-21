from django.db import migrations, models
import json

def load_data(apps, schema_editor=None):
    Provider = apps.get_model("providers", "Provider")
    with open("./providers.json", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            # Django will automatically assign a value to id_uuid when you save the provider instance since we define it as a primary key with auto increment (BigAutoField)
            provider = Provider(**item)
            provider.save()

def delete_data(apps, schema_editor=None):
    Provider = apps.get_model("providers", "Provider")
    Provider.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name="Provider",
            fields=[
                ("id_uuid", models.BigAutoField(primary_key=True)),
                ("id", models.IntegerField()),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("sex", models.CharField(max_length=10)),
                ("birth_date", models.DateField()),
                ("rating", models.FloatField()),
                ("primary_skills", models.JSONField()),
                ("secondary_skill", models.CharField(max_length=50)),
                ("company", models.CharField(max_length=50)),
                ("active", models.BooleanField()),
                ("country", models.CharField(max_length=50)),
                ("language", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["-rating"],
            },
        ),
        migrations.RunPython(load_data, reverse_code=delete_data),
    ]