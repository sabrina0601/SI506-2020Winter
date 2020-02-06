# Lecture 09_02 Exercise Objectives

# 01. Work with nested lists
# 02. Write function to extract locations
# 03. Write function to format location string
# 04. Control execution path from main() function
# 05. Implement accumulator pattern
# 06. Write for loops and conditional statements to filter data
# 08. Write expressions using a membership operator (in, not in)
# 09. Read a function's Docstring


def format_event_location(event, location='building'):
    """Return formatted event location string. Optional location
    parameter determines geographical scope of the location string
    to  be returned.

    Location values accepted:
    'building': '<building>, <city>, <country>'
    'city': <city>, <country>'
    'country': <country>'

    Parameters:
        event (list): list of event attributes
        location (str): determines geographical scope of location

    Returns:
        str: venue location as scoped by location argument
    """

    pass


def get_event_locations(tour_dates, location='building'):
    """Returns list of event locations, filtering out duplicates.
    Format location strings by calling format_event_location() passing
    location and string constant that sets the location scope (i.e.,
    building, city, country).

    Parameters:
        tour_dates (list): list of events
        locations (str): optional string that determines location scope.

    Returns:
        list: list of formatted event locations
    """

    pass


def main():
    """Entry point for program.

    Parameters:
        None

    Returns:
        None
    """

    tour_dates = [
        ['JLCO','February 10, 2020','DR Koncerthuset','Copenhagen','Denmark'],
        ['JLCO','February 11, 2020','Musikkens Hus','Aalborg','Denmark'],
        ['JLCO','February 12, 2020','Elbphilharmonie','Hamburg','Germany'],
        ['JLCO','February 13, 2020','Konzerthaus Dortmund','Dortmund','Germany'],
        ['JLCO','February 14, 2020','Philharmonie Luxembourg','Luxembourg City','Luxembourg'],
        ['JLCO','February 16, 2020','HET Concertgebouw', 'Amsterdam','Netherlands'],
        ['JLCO','February 16, 2020','HET Concertgebouw','Amsterdam','Netherlands'],
        ['JLCO','February 18, 2020','Henry Le Boeuf Hall - BOZAR','Brussels','Belgium'],
        ['JLCO','February 19, 2020','Henry Le Boeuf Hall - BOZAR','Brussels','Belgium'],
        ['JLCO','February 22, 2020','National Forum of Music','Wrocław','Poland'],
        ['JLCO','February 23, 2020','National Polish Radio Symphony Orchestra','Katowice','Poland'],
        ['JLCO','February 24, 2020','Wiener Konzerthaus','Vienna','Austria'],
        ['JLCO','February 25, 2020','Wiener Konzerthaus','Vienna','Austria'],
        ['JLCO','February 26, 2020','Wiener Konzerthaus','Vienna','Austria'],
        ['JLCO','February 28, 2020','Palau de la Música Catalana','Barcelona','Spain']
    ]

    # Count tour dates
    event_count = len(tour_dates)

    print(f"\nTour dates count = {event_count}\n")

    # NESTED LIST INDEXING AND SLICING

    # Use indexing and list slicing to return subsets of elements

    # Get 1st event: country
    country = tour_dates[0][-1]

    print(f"1st event: country = {country}\n")

    # Get 2nd event: city and country
    city_country = None

    print(f"2nd event: city, country = {city_country}\n")

    # Get Last event: building, city, country
    venue = None

    print(f"Last event: building, city, country = {venue}\n")


    # 2.0 EXERCISE
    # Write function to retrieve tour locations
    # Pass in optional filter value (see Docstring)
    # Format string return value (see Docstring)


    # UNCOMMENT Tour venues (building, city, country)
    # venues = get_event_locations(tour_dates)

    # print(f"\nTour Venues (n={len(venues)})")
    # for venue in venues:
    #     print(venue)


    # UNCOMMENT Tour cities (city, country)
    # cities = get_event_locations(tour_dates, 'city')

    # print(f"\nTour Cities (n={len(cities)})")
    # for city in cities:
    #     print(city)


    # Tour countries (country)
    # countries = get_event_locations(tour_dates, 'country')

    # print(f"\nTour Countries (n={len(countries)})")
    # for country in countries:
    #     print(country)

    print('\n') # padding

if __name__ == '__main__':
    main()
