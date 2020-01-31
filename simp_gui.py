import PySimpleGUI as Sg
from SpellGen import Spell

while True:
    query = Sg.PopupGetText('SpellGen', 'Enter spell name to retrieve entry')
    text = Spell(query).fulltext
    Sg.PopupScrolled(text, title=query)
