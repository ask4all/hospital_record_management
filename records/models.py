from django.db import models
from django.utils import timezone

# Create your models here.

class Cardiology(models.Model):
	title = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.title

class Endocrinology(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Ae(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Aefobs(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Aemaleobs(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Aepeadons(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Ancclinic(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Cardroom(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Casualitytheatre(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Deliveries(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Dental(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Dermatology(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Dressingroom(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Ecg(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Ent(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Femaleobs(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Ffactivities(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Fmw(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Hts(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Icu(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Immunization(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Injectionroom(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Inpatients(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Kschma(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Laboratory(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Lyingwarda(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Lyingwardb(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Maleopd(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Mmw(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Msw(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Neorology(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Neprology(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Newa(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Nhis(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Nursery(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Obtetrics(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Opthomology(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Othopedic(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Outpatients(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Paed(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Paediatricopd(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Paediatricsc(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Physiotheraphy(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Pmctc(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis
class Psycatrics(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Radiology(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Reomatism(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Sopd(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis

class Theatre(models.Model):
	diagonosis = models.CharField(max_length=255, help_text="Enter Your Diag Here")
	time = models.DateField(default = timezone.now)
	malea = models.CharField(max_length=255)
	totala = models.CharField(max_length=25)
	femaleb = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis
