from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


ROLE_CHOICES = (
    ('', 'Please Select'),
    ('teacher', 'Teacher'),
    ('secretary', 'Secretary'),
    ('accountant', 'Accountant'),
    ('hr', 'Human Resource'),
    ('librarian', 'Librarian'),
    ('academy', 'Academy'),
    ('matron', 'Matron'),
    ('vehicle', 'Vehicle'),
)

class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'role']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        if len(password1) < 8:
            raise forms.ValidationError('It must be 8 character or more')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CreateStaffForm(forms.ModelForm):
    role = forms.ChoiceField(
        widget=forms.Select,
        choices=ROLE_CHOICES,
        label='Select user role'
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'role',]


class UpdateStaffForm(forms.ModelForm):
    role = forms.ChoiceField(
        widget=forms.Select,
        choices=ROLE_CHOICES,
        label='Select user role'
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'role',]
