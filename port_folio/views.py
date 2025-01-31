from django.shortcuts import render,redirect
from .form import MessageForm
from .models import Message

# Create your views here.



def home(request):
    return render(request, 'port_folio/home.html')

 

 

from django.db import models


class Message_view(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
    


def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # Save the message to the database
            return redirect('success_page')  # Redirect to a success page
    else:
        form = MessageForm()
    return render(request, 'port_folio/contact.html', {'form': form})

def message_list_view(request):
    messages = Message.objects.all().order_by('-created_at')
    return render(request, 'port_folio/message_list.html', {'messages': messages})


def success_page (request):
    return render(request, 'port_folio/succes.html')


def servicePage(request):
    return render(request, 'port_folio/service.html')





