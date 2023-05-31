from django.shortcuts import render, redirect
from .forms import ComplaintForm
from .models import Complaint
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'complaints/signup.html', {'form': form})



def dashboard(request):
    user_complaints = Complaint.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'complaints/dashboard.html', {'complaints': user_complaints})


def submit_feedback(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('dashboard')
    else:
        form = ComplaintForm()
    return render(request, 'complaints/submit_feedback.html', {'form': form})


def review_feedback(request, complaint_id):
    complaint = Complaint.objects.get(id=complaint_id, user=request.user)
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES, instance=complaint)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ComplaintForm(instance=complaint)
    return render(request, 'complaints/review_feedback.html', {'form': form, 'complaint': complaint})
