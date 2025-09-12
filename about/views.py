from django.shortcuts import render

from .models import About
from django.contrib import messages
from .forms import CollaborateForm

# Create your views here.

def about(request):
    
    about = About.objects.all().order_by('-updated_on').first()    
    template = 'about/about.html'
    if request.method == 'POST':
        collaborte_form = CollaborateForm(data=request.POST)
        if collaborte_form.is_valid():
            collaborte_form.save()

            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )

    collaborte_form = CollaborateForm()
    
    return render(
        request,
        template,
        {"about":about,
         "collaborate_form": collaborte_form}
    )
    
