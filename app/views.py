from app import app
from .converters import roman_numerals

@app.route('/<number>')
def home(number):
	return roman_numerals.encode(number)

