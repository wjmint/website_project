from django.shortcuts import render
from catalog.models import Cat, CatSpecies, CatColour   

# Create your views here.
def index(request):
    # view function for the home page of the site

    # Generate counts of some of the main objects
    num_cats = Cat.objects.all().count()

    context = {
        'num_cats': num_cats
    }

    return render(request, 'index.html', context=context)