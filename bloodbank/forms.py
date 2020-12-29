from django import forms
class Subscribe(forms.Form):
    Email = forms.EmailField()
    Context=forms.CharField(max_length=100)

    def _str_(self):
        return self.Email
