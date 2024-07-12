# import flet as ft
# import asyncio
# from time import sleep

# class AnimatedChatBubble(ft.Container):
#     def __init__(self):
#         super().__init__()
#         self.dots = [self.animated_dot() for _ in range(3)]
#         self.content = ft.Container(
#             content=ft.Row(self.dots, spacing=4),
#             width=10,
#             height=40,
#             bgcolor="#E6F8F1",
#             border_radius=ft.border_radius.only(
#                 top_left=2,
#                 top_right=20,
#                 bottom_left=20,
#                 bottom_right=20
#             ),
#             padding=ft.padding.all(16),
#         )

#     def animated_dot(self):
#         return ft.Container(
#             width=7,
#             height=7,
#             border_radius=50,
#             bgcolor="#6CAD96",
#             offset=ft.transform.Offset(0, 0),
#             animate_offset=ft.animation.Animation(600, ft.AnimationCurve.EASE_IN_OUT),
#         )

    # def animate_dots(self):
    #     while True:
    #         for i, dot in enumerate(self.dots):
    #             # sleep(0.2 * i)  
    #             dot.offset = ft.transform.Offset(0, 0 if dot.offset.y == -1 else -1)
    #             self.update()
            # sleep(0.6)  

    # def build(self):
    #     asy = self.animate_dots()
    #     return self.content

# async def main(page: ft.Page):
#     animated_chat_bubble = AnimatedChatBubble()
#     page.add(animated_chat_bubble)

# ft.app(target=main)


import flet as ft


class AnimatedChatBubble(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text(value="Thinking...")
        self.margin = 10
        
    
    
