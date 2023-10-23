from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=60, blank=False)
    description = models.TextField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}'
class Person(models.Model):
    # lista wartości do wyboru w formie krotek
    class Sex(models.IntegerChoices):
        MALE = 1
        FEMALE = 2
        OTHER = 3
    name = models.CharField(max_length=60, blank=False)
    surrname = models.CharField(max_length=60, blank=False)
    # wskazanie listy poprzez przypisanie do parametru choices
    sex_type = models.IntegerField(choices=Sex.choices)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.surrname}'

    class Meta:
        ordering = ["surrname"]
