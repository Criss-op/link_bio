import reflex as rx

def preloader() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div("Cargando", class_name="preloader__title"),
                rx.el.div(
                    rx.el.svg(
                        rx.el.circle(class_name="ring__track", cx="60", cy="60", r="46"),
                        rx.el.circle(class_name="ring__bar", cx="60", cy="60", r="46"),
                        view_box="0 0 120 120",
                    ),
                    rx.el.div(
                        rx.el.span("0", id="pl-pct"),
                        "%",  # texto literal
                        class_name="preloader__pct",
                    ),
                    class_name="preloader__ring",
                    aria_label="Progreso de carga",
                ),
                class_name="preloader__top",
            ),

            rx.el.div(
                rx.el.div("Cargando CSS…", class_name="pl-line", data_step="css"),
                rx.el.div("Cargando imágenes…", class_name="pl-line", data_step="img"),
                rx.el.div("Cargando scripts…", class_name="pl-line", data_step="js"),
                rx.el.div("Finalizando…", class_name="pl-line", data_step="done"),
                class_name="preloader__status",
            ),

            rx.el.div(
                rx.el.span("✓", class_name="check"),
                rx.el.span("Listo", class_name="done-text"),
                class_name="preloader__done",
            ),



            class_name="preloader__card",
        ),
        id="preloader",
        class_name="preloader",
    )
