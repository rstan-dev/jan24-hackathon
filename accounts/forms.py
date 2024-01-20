from . import views


class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['categories']
