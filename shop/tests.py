from django.test import TestCase

from .models import Category, Product


class  CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name='FirstTest', description=None)
        Category.objects.create(name='<h1>SecondTest</h1>')
        Category.objects.create(name="<script>alert('sads')</script>")

    def test_category_name(self):
        categories = Category.objects.all()
        print([cat for cat in categories])

class ProductTestCase(TestCase):
    def setUp(self):
        cat = Category.objects.first()
        Product.objects.create(
            name='fuck you',
            category=cat,
            price= -23
            )

    def test_product(self):
        products = Product.objects.all()
