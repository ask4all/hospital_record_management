from django.db import models
from django.utils import timezone

# Create your models here.

class Cardiology(models.Model):
	title = models.CharField(max_length=255, help_text="Enter Patient Name")

class Endocrinology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Ae(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Aefobs(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Aemaleobs(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Aepeadons(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Ancclinic(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Cardroom(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Casualitytheatre(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Deliveries(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Dental(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Dermatology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Dressingroom(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Ecg(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Ent(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Femaleobs(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Ffactivities(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Fmw(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Hts(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Icu(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Immunization(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Injectionroom(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Inpatients(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Kschma(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Laboratory(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Lyingwarda(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Lyingwardb(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Maleopd(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Mmw(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Msw(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Neorology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Neprology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Newa(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Nhis(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Nursery(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Obtetrics(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Opthomology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Othopedic(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Outpatients(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Paed(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Paediatricopd(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Paediatricsc(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Physiotheraphy(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Pmctc(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Psycatrics(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Radiology(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Reomatism(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Sopd(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)

class Theatre(models.Model):
	diagonosis = models.CharField(max_length=255)
	time = models.DateField(default = timezone.now)
