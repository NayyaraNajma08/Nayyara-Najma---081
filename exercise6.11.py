cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10500000,
        'fact': 'It is located on the northwest coast of Java.',
    },
    'seoul': {
        'country': 'south korea',
        'population': 9700000,
        'fact': 'It is the largest city in South Korea.',
    },
    'moscow': {
        'country': 'russia',
        'population': 12000000,
        'fact': 'It is the largest city in Russia.',
    },
}
for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: about {info['population']}")
    print(f"\tFact: {info['fact']}\n")