class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               min_length=5,
                               label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-login-input'}))
    password = froms.CharField(min_length=6,
                               label='Пароль',
                               widget=forms.TextInput(attrs={'class': 'form-login-input'}))

    def clean_password(self):
        password = self.cleaned_data['password']
        ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-?!$#@_"
        if not (set(password) <= set(ALLOWED_CHARS)) or len(password) < 6:
            raise ValidationError("Некорректно введенный пароль.")

        return password



Объявите класс формы с именем LoginForm, не связанной с моделью, со следующими полями:

username: текстовое поле; максимальная длина 50 символов, минимальная длина 5 символов, обязательное, название "Логин";
password: поле ввода пароля; минимальная длина 6 символов, обязательное, название "Пароль".

Атрибуты класса должны иметь те же названия и порядок, что и в описании.

Для полей формы через параметр widget укажите стили оформления: attrs={'class': 'form-login-input'}

Для проверки корректности поля password объявите в классе LoginForm метод с именем:

clean_<название поля>

В этом методе реализовать проверку значения поля password по следующим критериям:

допустимые символы: буквы латинского алфавита (малые и большие), цифры и символы "-?!$#@_";
минимальная длина пароля 6 символов.
Если эти проверки не проходят, то генерировать исключение:

raise ValidationError("Некорректно введенный пароль.")
Иначе метод должен возвращать введенный пароль (в виде строки).

P.S. На экран ничего выводить не нужно
