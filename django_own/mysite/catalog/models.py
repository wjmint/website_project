from django.db import models

# Create your models here.

class CatSpecies(models.Model):
    # model representing the species of the cats (e.g. Scottish fold, persian)
    name = models.CharField(
        max_length=200,
        help_text='Enter a cat species (e.g. Scottish fold, Persian etc.)'
    )
    
    def __str__(self):
        # String for representing the Model obj. (in Admin site etc.)
        return self.name

class CatColour(models.Model):
    # model representing the cat's colour and pattern (e.g. grey, tuxedo etc.)
    name = models.CharField(
        max_length=200,
        help_text='Enter a colour or pattern of the cat (e.g. Grey, Tuxedo, Tabby)'
    )

class Cat(models.Model):
    name = models.CharField(
        max_length=200
    )
    
    Species = models.ForeignKey(
        'CatSpecies', on_delete=models.SET_NULL, null=True
    )

    Details = models.TextField(
        max_length=1000,
        help_text='Enter any details like character of cat'
    )

    class Meta:
        ordering = ['name', 'Species']

    def display_CatColour(self):
        return ', '.join([CatColour.name for CatColour in self.CatColor.all()[:3]])

    display_CatColour.short_description = 'CatColour'

    def get_absolute_url(self):
        return reverse('Cat-Detail', args=[str(self.id)])
        
    def __str__(self):
        return self.name

