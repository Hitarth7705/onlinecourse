from django.shortcuts import render, redirect
from .models import Submission

def submit(request, course_id):

    if request.method == 'POST':
        submission = Submission.objects.create()
        return redirect('show_exam_result', submission.id)

def show_exam_result(request, submission_id):

    submission = Submission.objects.get(pk=submission_id)

    context = {
        "score": 80
    }

    return render(request, "exam_result.html", context)