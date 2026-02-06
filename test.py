class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,
                               min_length=5,
                               label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    email = forms.EmailField(min_length=5,
                             required = False,
                             label='E-mail',
                             widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    first_name = forms.CharField(max_length=50,
                                 required = False,
                                 label='Имя',
                                 widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    last_name = forms.CharField(max_length=50,
                                 required = False,
                                 label='Фамилия',
                                 widget=forms.TextInput(attrs={'class': 'form-register-input'}))
    password1 = forms.CharField(min_length=6,
                               label='Пароль',
                               widget=forms.PasswordInput(attrs={'class': 'form-register-input'}))
    password2 = forms.CharField(min_length=6,
                               label='Повтор пароля',
                               widget=forms.PasswordInput(attrs={'class': 'form-register-input'}))

    def clean(self):
        cleaned_data = super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-?!$#@_"
        if not (set(password1) <= set(ALLOWED_CHARS)):
            raise ValidationError("Некорректно введенный пароль.")
        elif len(password1) < 6:
            raise ValidationError("Слишком короткий пароль.")

        if password1 != password2:
            raise ValidationError("Пароли не совпадают.")

        return password




Объявите класс формы с именем RegisterForm, не связанной с моделью, со следующими полями:

username: текстовое поле; максимальная длина 50 символов, минимальная длина 5 символов, обязательное, название "Логин";
email: поле ввода адреса электронной почты; минимальная длина 5 символов, необязательное, название "E-mail";
first_name: текстовое поле; максимальная длина 50 символов, необязательное, название "Имя";
last_name: текстовое поле; максимальная длина 50 символов, необязательное, название "Фамилия";
password1: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Пароль";
password2: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Повтор пароля".

Атрибуты класса должны иметь те же названия и порядок, что и в описании.

Для полей формы через параметр widget укажите стили оформления: attrs={'class': 'form-register-input'}

Для проверки корректности полей password1 и password2 объявите в классе RegisterForm метод clean следующим образом:

def clean(self):
    cleaned_data = super().clean()
    # продолжение метода
В этом методе реализуйте проверку значений полей password1 и password2 по следующим критериям:

а) допустимые символы: буквы латинского алфавита (малые и большие), цифры и символы "-?!$#@_";
б) минимальная длина пароля 6 символов;
в) пароли password1 и password2 должны совпадать.

Если эти проверки не проходят, то генерировать исключения:

а) raise ValidationError("Некорректно введенный пароль.")
б) raise ValidationError("Слишком короткий пароль.")
в) raise ValidationError("Пароли не совпадают.")

P.S. На экран ничего выводить не нужно.
