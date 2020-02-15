import PySimpleGUI as Sg
import shelve


# Interface to database --------------------------------------------------------------------------------
def get_spell(spell: str):
    with shelve.open(r'.\spellbook\\spellbook', 'r') as book:
        entry = spell.upper().replace(' ', '_')
        return book[entry]


def read_spell(spell: str):
    entry = get_spell(spell)
    text = [v for (k, v) in entry.items()]
    return ''.join(text)


# search_controls - Frame containing the controls for the Spell Search ------------------------------------

# Internal Widgets
instructions = Sg.Text("Enter the spell you're looking for here:")

search_input = Sg.InputText('', key="QUERY", do_not_clear=False, focus=True)

search_button = Sg.Button('Search', key='SEARCH', bind_return_key=True)

# Sizer for search_controls
control_layout = [[instructions],
                  [search_input],
                  [search_button]]

# Frame Widget - container for above 'Internal Widgets'
search_controls = Sg.Frame('Enter Search', layout=control_layout)

# Sizer for main window. Has no parent, this is the top level -------------------------------------------

display = Sg.Multiline('Spell Entry', key='DISPLAY',
                       background_color='#d6d0d4', text_color='#b84242',
                       auto_size_text=True)

main_layout = [[display, search_controls]]


window = Sg.Window('Pydd5e', main_layout, resizable=True, finalize=True, )


while True:  # Main Event Loop -----------------------------------------------------------------------------------

    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'SEARCH':
        try:
            result = read_spell(values['QUERY'])
            length = result.count('\n')  # how many lines in the text entry. Used for six

            if length > 20:  # testing the length of the text entry and maxing the size at 20 lines
                window['DISPLAY'].set_size((None, 20))
            else:
                window['DISPLAY'].set_size((None, length + 2))  # adding 2 makes up for no '\n' at end

            window['DISPLAY'].update(result)

        except KeyError:
            window['DISPLAY'].update(f"Sorry, couldn't find: {values['QUERY']}")


window.close()
