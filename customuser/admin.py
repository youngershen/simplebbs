from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from customuser.models import User 
class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password_confirm = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'avatar', 'gender', 'is_admin')
    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise form.ValidationError("password do not match")
        return password_confirm

    def save(self, commit = True):
        user = super(userCreateForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ('email', 'avatar', 'gender', 'is_admin')

    def clean_password(self):
        return self.initial['password']


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('email', 'avatar', 'gender', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
                    (None, {'fields' : ('email', 'password')}),
                    ('personal info',{'fields' : ('avatar', 'gender')}),
                    ('permission', {'fields': ('is_admin',)})
                )

    add_fieldsets = (
            (None,{
                    'classes' : ('wide',),
                    'fields'  : ('email', 'avatar', 'gender', 'is_admin')
                    }),
            )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

