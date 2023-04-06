import flet as ft


def main(page: ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your prompt"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))

    txt_name = ft.TextField(label="Your prompt")

    page.add(txt_name, ft.ElevatedButton("Generate!", on_click=btn_click))


flet.app(target=main, view=None, port=8502)
