from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.utils.translation import gettext_lazy as _
from client.forms import RegistrationForm, ClientLoginForm
from django.contrib import messages


class ClientRegistration(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Ro'yxatdan o'tish")



    def get(self, request, *args, **kwargs):
        return render(request, 'layouts/login.html', {
            'form': RegistrationForm()
        })

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()

            messages.success(request, _("Siz muvaffaqiyatli ro'yxatdan o'tding!!"))


            return redirect("client:login")


        return render(request, "layouts/login.html", {
            "form": form
        })




class ClientLogin(View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)

        request.title = _("Ro'yxatdan o'tish")

    def get(self, request, *args, **kwargs):
        return render(request, 'layouts/sing.html', {
            'form': ClientLoginForm()
        })


    def post(self, request, *args, **kwargs):
        form = ClientLoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, _("Xush kelibsiz, {}!".format(user.username)))
                return redirect("main:test_list")

            form.add_error('password', _("Login yoki parol xato"))


        return render(request, "layouts/sing.html", {
            'form': form
        })





@login_required
def client_logout(request):
    messages.success(request, "Xayr {}".format(request.user.username))
    logout(request)

    return redirect("main:index")






# class ClinetProfile(LoginRequiredMixin, UpdateView):
#     model = User
#     fields = ["first_name", "last_name", "username", "email", "photo"]
#     template_name = "layouts/profile.html"
#     success_url = reverse_lazy("main:index")


#     def setup(self, request, *args,  **kwargs):
#         super().setup(request, *args, **kwargs)

#         request.title = _("Profile")
#         request.button_title = _("Saqlash")

#     def get_object(self, queryset=None):
#         return self.request.user



