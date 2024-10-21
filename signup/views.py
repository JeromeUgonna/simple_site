from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Create the user
            return redirect('login')  # Redirect to the login page after signup
    else:
        form = UserCreationForm()  # Create an empty form instance
    return render(request, 'signup/signup.html', {'form': form})  # Render the form
