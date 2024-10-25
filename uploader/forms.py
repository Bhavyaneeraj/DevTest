from django import forms
from .models import UploadModel

class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadModel
        fields = ['file']
    
    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(('.csv', '.xlsx')):
            raise forms.ValidationError('Only CSV and Excel files are allowed.')
        if file.size > 5 * 1024 * 1024:  # 5MB limit
            raise forms.ValidationError('File size must be under 5MB.')
        return file
