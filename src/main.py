# ==== Imports ==== #
import flet as ft

from ui.app import MSFSDiagApp

# ==== Entry Point ==== #
def main(page: ft.Page):
    MSFSDiagApp(page)

if __name__ == "__main__":
    ft.run(main)
