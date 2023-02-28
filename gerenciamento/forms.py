from django import forms


from .models import Gerais, Comissão



class Form_Gerais(forms.ModelForm):
   
    
 
    class Meta:
        model = Gerais
        fields = '__all__'
        
        widgets = {
        'data': forms.DateInput(format=('%Y-%m'), attrs={'class':'form-control', 'placeholder':'Select Date','type': 'date'}),
        'nome':forms.TextInput(attrs={'placeholder': 'Nome'})
    } 
        
        
class Form_Comissão(forms.ModelForm):

    class Meta:
        model = Comissão
        fields = '__all__'
        
        


