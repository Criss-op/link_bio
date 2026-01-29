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
