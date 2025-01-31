from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Non Ou',
                'style': 'background: #f9f9f9; border-radius: 10px;',
                'aria-label': 'Your Name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Imèl Ou',
                'style': 'background: #f9f9f9; border-radius: 10px;',
                'aria-label': 'Your Email',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Mesaj Ou',
                'rows': 5,
                'style': 'background: #f9f9f9; border-radius: 10px;',
                'aria-label': 'Your Message',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        # Add icons to placeholders using custom labels
        self.fields['name'].label = 'Non Ou <i class="bi bi-person-fill"></i>'
        self.fields['email'].label = 'Imèl Ou <i class="bi bi-envelope-fill"></i>'
        self.fields['content'].label = 'Mesaj Ou <i class="bi bi-chat-dots-fill"></i>'
