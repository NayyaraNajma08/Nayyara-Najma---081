def get_city_country(city, country, population=''):
    """Kembalikan 'City, Country' atau 'City, Country - population xxx'."""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    return f"{city.title()}, {country.title()}"
