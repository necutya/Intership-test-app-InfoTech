from django import forms


class MessageForm(forms.Form):
    """ Form for a message """

    content = forms.CharField(widget=forms.Textarea)


class MessageImageForm(forms.Form):
    """ Form for images to a message """

    images = forms.ImageField(
        required=False, widget=forms.FileInput(attrs={"multiple": True})
    )
