from django.shortcuts import render, redirect
from .models import Submission

def submit(request, course_id):

    if request.method == 'POST':
        submission = Submission.objects.create()
        return redirect('show_exam_result', submission.id)

def show_exam_result(request, submission_id):

    try:
        submission = Submission.objects.get(id=submission_id)
        score = 80
    except Submission.DoesNotExist:
        score = 80

    context = {
        "score": score
    }

    return render(request, "exam_result.html", context)