from django import forms


class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)


class MessageImageForm(forms.Form):
    images = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={"multiple": True})
    )
