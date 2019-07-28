from django import forms

class AddCouponForm(forms.Form):
    code = forms.CharField(label='쿠폰을 입력하세요.')
