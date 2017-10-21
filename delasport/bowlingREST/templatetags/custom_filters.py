from django import template

register = template.Library()

@register.filter
def addClass(field, cls):
    old_classes = field.field.widget.attrs.get('class',None)
    updated_classes = old_classes + ' ' + cls if old_classes else cls
    return field.as_widget(attrs={'class':updated_classes})

@register.filter
def at_index(array, index):
    return str(array[index])
