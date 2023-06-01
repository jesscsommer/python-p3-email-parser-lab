import re 

class EmailAddressParser:

    def __init__(self, address_string):
        self.address_string = address_string

    def parse(self):
        pattern = r"[^0-9^\W][\w.]+[@][\w.]+"
        regex = re.compile(pattern)
        matches = regex.findall(self.address_string)
        unique_matches = set(matches)
        return sorted(list(unique_matches))