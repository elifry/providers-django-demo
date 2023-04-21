from django import template

register = template.Library()

# Determine whether or not the url contains the pattern, to check if it is the active tab
@register.simple_tag
def active(request, pattern):
    # Example: /group/ in /group/
    if pattern in request.path:
        # Filter out false positives of the home tab when other tabs are active
        if pattern == '/' and request.path != '/':
            return ''
        return 'active'
    return ''

# Change the greeting based on user permisson level 
@register.simple_tag
def user_welcome(name, permission_level):
    if permission_level == 'admin':
        welcome = f"Live long and prosper"
    else:
        welcome = f"Hello, {name}!"
    return welcome
