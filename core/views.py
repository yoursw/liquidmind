from django.shortcuts import render, redirect
from.forms import ExperienceForm

def record_experience(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)  # Don't save yet
            experience.user = request.user  # Associate the experience with the logged-in user
            experience.save()
            return redirect('success_page')  # Redirect to a success page (you'll need to create this)
    else:
        form = ExperienceForm()
    return render(request, 'experience_form.html', {'form': form})
