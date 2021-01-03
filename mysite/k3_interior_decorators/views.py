from django.shortcuts import render
from .models import MenuItem
from django.http import HttpResponse

# Create your views here.


def index(request):
    menuitem1 = MenuItem()
    menuitem1.name = 'Home'
    menuitem1.desc = 'This is the Home page'

    menuitem2 = MenuItem()
    menuitem2.name = 'About'
    menuitem2.desc = 'This is the About page'

    menuitem3 = MenuItem()
    menuitem3.name = 'Services'
    menuitem3.desc = 'This is the Services page'

    menuitem4 = MenuItem()
    menuitem4.name = 'Portfolio'
    menuitem4.desc = 'This is the Portfolio page'

    menuitem5 = MenuItem()
    menuitem5.name = 'Contacts'
    menuitem5.desc = 'This is the Contacts page'

    menuitems = [menuitem1, menuitem2, menuitem3, menuitem4, menuitem5]



    return render( request, 'index.html', {'menuitems':menuitems});