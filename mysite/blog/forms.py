from django import forms

class ItemsPerPageForm(forms.Form):
    items_per_page = forms.ChoiceField(label="Постов на странице",
        choices=[('3', '3'), ('6', '6'), ('10', '10')],
        widget=forms.Select(attrs={'onchange': 'this.form.submit()'}),
        initial='3'
    )