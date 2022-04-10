from django.test import TestCase
from .models import Category, Article

class CategoryModelTest(TestCase): 
    
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category='Sport', slug='sport')

    def test_get_absolute_url(self): 
        category = Category.objects.get(id=1)
        self.assertEquals(category.get_absolute_url(), '/articles/category/sport')

class ArticleModelTest(TestCase): 
    
    @classmethod
    def setUpTestData(cls):
        Article.objects.create(title='Стаття 4', slug='stattya-4', description='description', main_page=True,)

    def test_get_absolute_url(self): 
        article = Article.objects.get(id=1)
        self.assertEquals(article.get_absolute_url(), '/articles/2022/04/10/stattya-4')
