from django import forms

class Option(forms.Form):
    send_to =( ("1", "Saved"), ("2", "Unsaved"),("3","Attachment")) 
    option=forms.ChoiceField(choices = send_to)
    text = forms.CharField(max_length=200)
    # file_name = forms.CharField(max_length=200)