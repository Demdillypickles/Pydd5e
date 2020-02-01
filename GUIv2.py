import PySimpleGUI as Sg
from SpellGen import Spell


# search_controls - Frame containing the controls for the Spell Search ------------------------------------

# Internal Widgets
instructions = Sg.Text("Enter the spell you're looking for here:")

search_input = Sg.InputText('', key="QUERY")

search_button = Sg.Button('Search', key='SEARCH', bind_return_key=True)

# Sizer for search_controls
control_layout = [[instructions],
                  [search_input],
                  [search_button]]

# Frame Widget - container for above 'Internal Widgets'
search_controls = Sg.Frame('Enter Search', layout=control_layout)


# Sizer for main window. Has no parent, this is the top level -------------------------------------------
display = Sg.Text('Spell Entry', key='DISPLAY', size=(50, 20), auto_size_text=True)

main_layout = [[display, search_controls]]


window = Sg.Window('Pydd5e', main_layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'SEARCH':
        try:
            text = Spell(values['QUERY']).fulltext
            window['DISPLAY'].update(text)
            window['QUERY'].update("")
        except FileNotFoundError:
            window['DISPLAY'].update(f"Sorry, couldn't find: {values['QUERY']}")
            window['QUERY'].update("")


window.close()
