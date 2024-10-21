from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('landingpage')  # Redirect to landing page after logout
    return render(request, 'logout_app/logout.html')  # Render a logout confirmation page
