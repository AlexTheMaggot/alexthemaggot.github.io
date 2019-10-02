from django.db import models

class Review(models.Model):
	name = models.CharField(max_length = 120)
	text = models.TextField()
	date = models.DateTimeField()

	def __str__(self):
		return self.name