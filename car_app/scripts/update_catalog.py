import xml.etree.ElementTree as ET
import requests
from car_app.models import Mark, Model
from django.db import transaction

@transaction.atomic
def update_autoru_catalog():
    url = "https://auto-export.s3.yandex.net/auto/price-list/catalog/cars.xml"
    response = requests.get(url)
    root = ET.fromstring(response.content)

    Mark.objects.all().delete()
    Model.objects.all().delete()

    for mark_elem in root.findall(".//mark"):
        mark_name = mark_elem.get("name")
        mark = Mark.objects.create(name=mark_name)

        for folder_elem in mark_elem.findall(".//folder"):
            model_name = folder_elem.get("name").split(",")[0]
            Model.objects.create(mark=mark, name=model_name)

if __name__ == "__main__":
    update_autoru_catalog()