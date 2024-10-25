from django.shortcuts import render, redirect
from .forms import UploadForm
from django.core.mail import send_mail
import pandas as pd
from django.contrib import messages

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save()
            file_path = upload.file.path
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path, engine='openpyxl')
            summary = df.describe().to_string()

            send_mail(
                subject='Python Assignment - Ravuri Bhavya Neeraj',
                message=summary,
                from_email='bannubhavyaneeraj@gmail.com',
                recipient_list=['tech@themedius.ai'],
                fail_silently=False,
            )

            messages.success(request, 'File uploaded and email sent successfully.')
            print(summary)
            return redirect('thank_you')

    else:
        form = UploadForm()

    return render(request, 'uploader/upload.html', {'form': form})


def thank_you(request):
    return render(request, 'uploader/thank_you.html')

