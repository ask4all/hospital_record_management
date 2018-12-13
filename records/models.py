from django.db import models
from django.utils import timezone

# Create your models here.

class Cardiology(models.Model):
	title = models.CharField(max_length=255, help_text="Enter Patient Name")
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Endocrinology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Ae(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Aefobs(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Aemaleobs(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Aepeadons(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Ancclinic(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Cardroom(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Casualitytheatre(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Deliveries(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Dental(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Dermatology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Dressingroom(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Ecg(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Ent(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Femaleobs(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Ffactivities(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Fmw(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Hts(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Icu(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Immunization(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Injectionroom(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Inpatients(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Kschma(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Laboratory(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Lyingwarda(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Lyingwardb(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Maleopd(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Mmw(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Msw(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Neorology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Neprology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Newa(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Nhis(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Nursery(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Obtetrics(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Opthomology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Othopedic(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Outpatients(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Paed(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Paediatricopd(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Paediatricsc(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Physiotheraphy(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Pmctc(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

	def __str__(self):
		'''
			this represent the class object in admin site
		'''
		return self.diagonosis
class Psycatrics(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Radiology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Reomatism(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Sopd(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)

class Theatre(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
	totala = models.CharField(max_length=25)
	totalb = models.CharField(max_length=25)
	totalab = models.CharField(max_length=25)
