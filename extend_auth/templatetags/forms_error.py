from django.template.defaulttags import register

@register.filter(name='show_error')
def show_error(dictionary):
    for error in dictionary.errors.as_data().values():
        return error[0].message