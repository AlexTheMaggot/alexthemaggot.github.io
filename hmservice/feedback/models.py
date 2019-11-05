from django.db import models

class MainFeedBack(models.Model):

	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'MainFeedback'
		verbose_name_plural = 'MainFeedbacks'

class FeedBack(models.Model):

	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	brand = models.CharField(max_length=50, null=True)
	model = models.CharField(max_length=100, null=True)
	serv = models.CharField(max_length=100, null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Feedback'
		verbose_name_plural = 'Feedbacks'