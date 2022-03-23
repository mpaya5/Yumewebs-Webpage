from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(label="Nombre", min_length=3, max_length=100, required=True,
        widget=forms.TextInput(attrs=
        {
            'placeholder': 'Escribe tu nombre',
            'name': 'subject',
            'class': 'form-control'
        }))
    email = forms.EmailField(label="Email", min_length=3, max_length=100, required=True,
        widget=forms.TextInput(attrs=
        {
            'placeholder': 'Escribe tu email',
            'name': 'email',
            'class': 'form-control'
        }))
    message = forms.CharField(label="Contenido", min_length=10, max_length=1000, required=True,
        widget=forms.Textarea(attrs=
        {
            'placeholder': 'Escribe tu mensaje',
            'name': 'message',
            'rows': 3,
            'class': 'form-control'
        }))