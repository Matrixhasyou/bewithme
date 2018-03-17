from .models import Choice

class ChoiceForm(ModelForm):
        class Meta:
        model = Choice
        fields = ('choice_text',)
