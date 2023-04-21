from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse
from django import forms

# class NotificationsForm(forms.Form):
#     phone = forms.CharField(max_length=10)
#     email = forms.EmailField()
#
# class Notifications(FormView):
#     form = NotificationsForm
#     template = 'settings/notifications_test.html'
#
#     def get_success_url(self):
#         return reverse('some-form-success-view')
#
#     def form_valid(self, form):
#         # Do something with the form data like send an email.
#         return super().form_valid(form)

# Relative import of NotificationsForm
from .forms import NotificationsForm

class NotificationsView(FormView):
    # specify the Form you want to use
    form_class = NotificationsForm

    # specify name of template
    template_name = "settings/notifications.html"

    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/thanks/"

    def get(self, request, *args, **kwargs):
        print('get')
        form = NotificationsForm()
        context = {'form': form}
        return render(request, 'settings/notifications.html', context)

    def post(self, request, *args, **kwargs):
        form = NotificationsForm(data=request.POST)
        if form.is_valid():
            # self.send_mail(form.cleaned_data)
            print(form.cleaned_data)
            form = NotificationsForm()
            return render(request, 'settings/notifications.html', {'form': form})
        else:
            print('data not clean', form.errors)
        return render(request, 'settings/notifications.html', {'form': form})

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #
    #     # perform a action here
    #     print('henlo')
    #     print(form.cleaned_data)
    #     return super().form_valid(form)
