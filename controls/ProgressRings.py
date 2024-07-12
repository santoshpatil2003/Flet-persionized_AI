import flet as ft


# ft.SafeArea(
#     content=ft.Column(
#         controls=[
#             ft.Container(
#                 content=ft.Row(
#                     controls=[
#                         ft.Container(
#                             content=ft.ProgressRing(),
#                             width=30,
#                             height=30,
#                             alignment=ft.alignment.center,
#                         ),
#                         ft.SafeArea()
#                     ],
#                     alignment=ft.MainAxisAlignment.CENTER,
#                     vertical_alignment=ft.CrossAxisAlignment.CENTER,
#                 ),
#                 alignment=ft.alignment.center,
#                 expand=True
#             )
#         ],
#         alignment=ft.MainAxisAlignment.CENTER,
#         spacing=0,
#         expand=True
#     ),
#     expand=True
# )


class ProgressRings(ft.SafeArea):
    def __init__(self):
        content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Container(
                                content=ft.ProgressRing(),
                                width=30,
                                height=30,
                                alignment=ft.alignment.center,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=0,
            expand=True
        )
        super().__init__(content=content)
        self.expand = True
