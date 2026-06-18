import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import flet as ft
from ui.app import MSFSDiagApp

def main(page: ft.Page):
    MSFSDiagApp(page)

if __name__ == "__main__":
    ft.run(main)
