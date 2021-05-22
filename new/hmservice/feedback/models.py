from django.db import models

class MainFeedBack(models.Model):

	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Заявка с главной страницы'
		verbose_name_plural = 'Заявки с главной страницы'

class FeedBack(models.Model):

	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	brand = models.CharField(max_length=50, null=True)
	model = models.CharField(max_length=100, null=True)
	serv = models.CharField(max_length=100, null=True)
	date = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Заявка со страниц моделей'
		verbose_name_plural = 'Заявки со страниц моделей'