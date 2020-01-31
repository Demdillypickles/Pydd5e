class Spell:
    """Interactive object that provides information about a spell."""

    def __init__(self, entry: str):
        """Requires a text file that fits specified format. See 'docs\\README.txt'"""  # TODO
        spell_path = entry.replace(' ', '_')
        prepared = {}  # prepared spell attributes
        with open(r'.\\Spells2\\' + spell_path, 'r') as raw_spell:
            prepared['name'] = raw_spell.readline()

            # next line contains 2 attributes
            _type = raw_spell.readline().split(' ')
            prepared['school'] = _type[1].capitalize()
            prepared['level'] = _type[0] + '\n'

            prepared['casting_time'] = raw_spell.readline()
            prepared['range'] = raw_spell.readline()
            prepared['components'] = raw_spell.readline()
            # perform a check if components is multi-line
            if 'M' in prepared['components']:
                while ')' not in prepared['components']:
                    prepared['components'] = ''.join([prepared['components'], raw_spell.readline()])
            prepared['duration'] = raw_spell.readline()
            prepared['description'] = ''.join(raw_spell.readlines())

        # Accessible attributes
        self.name = prepared['name']
        self.school = prepared['school']
        self.level = prepared['level']
        self.casting_time = prepared['casting_time']
        self.range = prepared['range']
        self.components = prepared['components']
        self.duration = prepared['duration']
        self.description = prepared['description']

        # if spell is a cantrip, swaps attrs to correct spots
        if self.school == 'cantrip':
            self.school, self.level = self.level, self.school

        self.fulltext = ''.join(prepared.values())
# ---------------------------------------------------------------

    def __repr__(self):
        return str("Spell Object: " + self.name)


if __name__ == '__main__':
    test = Spell('aid')
    print(test.fulltext)
