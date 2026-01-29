import reflex as rx


class UIState(rx.State):
    mobile_open: bool = False
    contact_open: bool = False

    def toggle_menu(self):
        self.mobile_open = not self.mobile_open

    def close_menu(self):
        self.mobile_open = False

    def open_contact(self):
        self.contact_open = True

    def close_contact(self):
        self.contact_open = False


class ProjectsState(rx.State):
    
    password_input: str = ""
    authorized: bool = False
    error_message: str = ""

    
    _PASSWORD: str = "cambia-esto"

    def set_password_input(self, value: str):
        self.password_input = value

    def clear_error(self):
        self.error_message = ""

    def validate_password(self):
        # regla simple: compara y habilita
        if self.password_input.strip() == self._PASSWORD:
            self.authorized = True
            self.error_message = ""
            # opcional: limpiar input al entrar
            self.password_input = ""
        else:
            self.authorized = False
            self.error_message = "Contraseña incorrecta."
