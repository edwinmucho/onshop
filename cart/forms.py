from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class AddProductForm(forms.Form):
    quantity = forms.IntegerField(label="구매 개수", label_suffix=" = ", min_value=1)
    is_update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    # 유효성 체크
    def clean_quantity(self):
        data = self.cleaned_data['quantity']

        #Check lte zero
        if data <= 0:
            raise ValidationError(_("Invalid data : Quantity isn\'t minus"))

        return data
