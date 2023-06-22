from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Please write your review here',
                             widget=forms.Textarea(attrs={'class' : 'myform',
                                                          'rows' : '2', 'cols' : '2'}))