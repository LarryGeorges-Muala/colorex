from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):

	user_name = models.CharField(max_length=500, null=True, blank=True, default='Anonymous')
	has_a_user_name = models.BooleanField(default=False)

	'''
		Levels
	'''
	level_1_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_1_unlock = models.BooleanField(default=True)

	level_2_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_2_unlock = models.BooleanField(default=False)

	level_3_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_3_unlock = models.BooleanField(default=False)

	level_4_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_4_unlock = models.BooleanField(default=False)

	level_5_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_5_unlock = models.BooleanField(default=False)

	level_6_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_6_unlock = models.BooleanField(default=False)

	level_7_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_7_unlock = models.BooleanField(default=False)

	level_8_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_8_unlock = models.BooleanField(default=False)

	level_9_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_9_unlock = models.BooleanField(default=False)

	level_10_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	level_10_unlock = models.BooleanField(default=False)
	'''
		End Levels
	'''

	total_time = models.CharField(max_length=500, null=True, blank=True, default='0')
	total_time_numeric = models.IntegerField(default=0, null=True)

	''' Best Performance Handler '''
	def handle_performance(self, initial_time, new_time):
		if str(initial_time) == '0':
			return int(new_time)
		if int(new_time) < int(initial_time):
			return int(new_time)
		return int(initial_time)

	''' Update Timers '''
	def update_level_time(self, level_id, current_time):
		''' Find Level '''
		if int(level_id) == 1:
			self.level_2_unlock = True
			self.level_1_time = self.handle_performance(self.level_1_time, current_time)

		if int(level_id) == 2:
			self.level_3_unlock = True
			self.level_2_time = self.handle_performance(self.level_2_time, current_time)

		if int(level_id) == 3:
			self.level_4_unlock = True
			self.level_3_time = self.handle_performance(self.level_3_time, current_time)

		if int(level_id) == 4:
			self.level_5_unlock = True
			self.level_4_time = self.handle_performance(self.level_4_time, current_time)

		if int(level_id) == 5:
			self.level_6_unlock = True
			self.level_5_time = self.handle_performance(self.level_5_time, current_time)

		if int(level_id) == 6:
			self.level_7_unlock = True
			self.level_6_time = self.handle_performance(self.level_6_time, current_time)

		if int(level_id) == 7:
			self.level_8_unlock = True
			self.level_7_time = self.handle_performance(self.level_7_time, current_time)

		if int(level_id) == 8:
			self.level_9_unlock = True
			self.level_8_time = self.handle_performance(self.level_8_time, current_time)

		if int(level_id) == 9:
			self.level_10_unlock = True
			self.level_9_time = self.handle_performance(self.level_9_time, current_time)

		if int(level_id) == 10:
			self.level_10_unlock = True
			self.level_10_time = self.handle_performance(self.level_10_time, current_time)
		
		self.save()

		return True
	
	def update_total_time(self):
		# self.total_time = int(self.level_1_time) + int(self.level_2_time) + int(self.level_3_time) + int(self.level_4_time) + int(self.level_5_time) + int(self.level_6_time) + int(self.level_7_time) + int(self.level_8_time) + int(self.level_9_time) + int(self.level_10_time)
		''' From Level 1 To 5 '''
		self.total_time = int(self.level_1_time) + int(self.level_2_time) + int(self.level_3_time) + int(self.level_4_time) + int(self.level_5_time)
		self.total_time_numeric = int(self.total_time)
		self.save()
		return True

	def __str__(self):
		return self.user_name
