import re

from string import ascii_uppercase, ascii_lowercase


class PhoneNumber:

    def __init__(self, n):
        self.n = n

        if any(letter in self.n for letter in "!@#$%^&*_"):
            raise ValueError("punctuations not permitted")
        if any(letter in self.n for letter in ascii_lowercase + ascii_uppercase):
            raise ValueError("letters not permitted")

        digits_only = re.sub(r"\D", "", n)
        if len(digits_only) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits_only) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits_only) == 11 and not digits_only.startswith("1"):
            raise ValueError("11 digits must start with 1")
        
        (self.number, self.area_code, self.exchange_code, self.subscriber_number, self.international_code_number) = self.n_fixer_upper(self.n)

        
        if self.exchange_code.startswith("0"):
            raise ValueError("exchange code cannot start with zero")
        if self.exchange_code.startswith("1"):
            raise ValueError("exchange code cannot start with one")
        if self.area_code.startswith("0"):
            raise ValueError("area code cannot start with zero")
        if self.area_code.startswith("1"):
            raise ValueError("area code cannot start with one")



    def n_fixer_upper(self, n):
        number_match = re.fullmatch(r"(?P<international_code_number>\+1\s*|1\s*)?(?P<area_code>\(\d{3}\)|\d{3})[- .]*(?P<exchange_code>\d{3})[- .]*(?P<subscriber_number>\d{4})[- .]*", n)


        if number_match:
            international_code_number = ""

            if re.match(r"^\s*\+1", n) or re.match(r"^\s*1\b", n):
                if n.strip().startswith("+1"):
                    international_code_number = "+1"
                else:
                    international_code_number = "1"
            
            area_code = number_match.group('area_code').replace("(", "").replace(")", "")
            exchange_code = number_match.group('exchange_code')
            subscriber_number = number_match.group('subscriber_number')

            number = area_code + exchange_code + subscriber_number

            return (number, area_code, exchange_code, subscriber_number, international_code_number)

    def pretty(self):
        n = self.number
        return f"({n[:3]})-{n[3:6]}-{n[6:]}"
            


