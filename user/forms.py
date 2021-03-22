from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Username")
    password=forms.CharField(label="Password",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Username")
    password=forms.CharField(max_length=20,label="Password",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Confirm Password",widget=forms.PasswordInput)
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")

        if password and confirm and password !=confirm:
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        values={
            "username" :username,
             "password":password
}
        return values