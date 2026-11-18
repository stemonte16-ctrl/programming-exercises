"""Checking the global variable"""

user_logged_in = False

def requires_login(function):
    """Decorator to check if is true or false"""
    def wrapper():
        if not user_logged_in:
            raise ValueError("Usuario no autenticado")
        else:
            result = function()
        return result
    return wrapper

@requires_login
def view_profile():
    """Show message"""
    print("Mostrando perfil del usuario")

view_profile()
