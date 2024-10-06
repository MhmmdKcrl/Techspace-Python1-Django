from django import forms

from core.models import Contact


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = ["name", 'email', 'subject', 'message']

        widgets = {
            "name" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder": "Your Name"
            }),
            "email": forms.EmailInput(attrs={
                "class" : "form-control",
                "placeholder" : "Your Email"
            }),
            "subject" : forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder": "Subject"
            }),
            "message": forms.Textarea(attrs={
                "class" : "form-control",
                "placeholder": "Message",
                "rows": 7,
                "cols": 30
            })
        }

    # def clean(self):
    #     value = self.cleaned_data["email"]
    #     if not value.endswith(".com"):
    #         raise forms.ValidationError("Mail must be .com!")

    #     return value
    
    # def clean_email(self):
    #     value = self.cleaned_data["email"]
    #     if not value.endswith(".com"):
    #         raise forms.ValidationError("Mail must be .com!")

    #     return value
    

    def clean_name(self):
        value = self.cleaned_data.get('name')
        if value == "admin":
            raise forms.ValidationError("Name cant be admin!")

        return value