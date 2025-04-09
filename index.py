import flet as ft


def main(page: ft.Page):
    page.title = "Meu Site com Logo"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 0
    page.bgcolor = "#f5f5f5"

    # LOGO (URL externa como exemplo)
    logo = ft.Image(
        src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo_TV_2015.png",
        width=40,
        height=40,
        fit=ft.ImageFit.CONTAIN
    )

    # Cabeçalho com logo + nome do site + menu
    navbar = ft.Container(
        content=ft.Row(
            [
                ft.Row([logo, ft.Text("Meu Site", size=20,
                       weight=ft.FontWeight.BOLD, color="white")]),
                ft.Row(
                    [
                        ft.TextButton(
                            "Início", style=ft.ButtonStyle(color="white")),
                        ft.TextButton(
                            "Contato", style=ft.ButtonStyle(color="white")),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    expand=True
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        ),
        bgcolor="#0077cc",
        padding=15,
        height=60
    )

    # Conteúdo principal
    content = ft.Container(
        content=ft.Column(
            [
                ft.Text("Bem-vindo ao meu site!", size=26,
                        weight=ft.FontWeight.BOLD),
                ft.Text("Este é um projeto simples feito com Flet.", size=18),
            ],
            spacing=10
        ),
        padding=30
    )

    page.add(navbar, content)


ft.app(target=main, view=ft.WEB_BROWSER)
