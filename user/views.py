from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .form import UserForm
# Create your views here.

def show(request):
    return HttpResponse("Thanks")

def show_email(request):
    
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        
        # Create and save a new User object
        user = User(email=email, password=password, shirt_size=None)
        user.save()
        
        return HttpResponse(f"User {email} saved successfully.")
    
    user=User.objects.all()
    
    context={
        "user" : user,
        "andha" : "thish is andha g",
             }
    
    return render(request,'index.html',context)

class Show_Email(generic.ListView):
    model = User 
    template_name = 'index_with_cbv.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['andha'] = "thish is andha g"
        return context
    


def detail(request,id):
    
    q=get_object_or_404(User,id=id)

    context={"u" : q}
    
    return render(request,'detail.html',context)


class Detail(generic.DetailView):
  
    model = User
    template_name = 'detail.html'  
    context_object_name = 'u'
    
    def get_object(self, queryset=None):
        # Retrieve the User object based on the id from URL parameters
        id = self.kwargs.get('id')
        return get_object_or_404(User, id=id)

def email_temp(request):
    return render(request,'email.html')


def user_view(request):
    
    print(request.POST)
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'email.html')
    else:
        form = UserForm()

    return render(request, 'user.html', {'form': form})

def update_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:detail1', id=user.id)
    else:
        form = UserForm(instance=user)
    
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'update_user.html', context)