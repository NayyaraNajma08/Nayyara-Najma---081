from city_functions import get_city_country

def test_city_country():
    """Apakah 'Santiago, Chile' bisa dihasilkan?"""
    result = get_city_country('santiago', 'chile')
    assert result == 'Santiago, Chile'
    
def get_city_country(city, country, population=''):
    """Kembalikan 'City, Country' atau 'City, Country - population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"