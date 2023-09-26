from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    pass
    # def save(self, request):
    #     super(SignupForm, self).save(request)
    #     user = super().save(request)
    #     readers = Group.objects.get(name="readers")
    #     user.groups.add(readers)
    #     return user
