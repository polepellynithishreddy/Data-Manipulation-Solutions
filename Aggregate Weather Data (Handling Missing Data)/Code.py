def aggregate_weather_data(records):
    # Initialize an empty dictionary to store weather data per city
    city_weather = {}

    # Loop through each record in the dataset
    for record in records:
        city = record['city']  # Extract city name
        
        if city not in city_weather:
            # Initialize totals and counts if city is not already in the dictionary
            city_weather[city] = {
                'temperature_total': 0,
                'temperature_count': 0,
                'humidity_total': 0,
                'humidity_count': 0
            }
        
        # Check if the 'temperature' key exists in the record and update
        if 'temperature' in record:
            city_weather[city]['temperature_total'] += record['temperature']
            city_weather[city]['temperature_count'] += 1
        
        # Check if the 'humidity' key exists in the record and update
        if 'humidity' in record:
            city_weather[city]['humidity_total'] += record['humidity']
            city_weather[city]['humidity_count'] += 1

    # Prepare final aggregated data
    aggregated_data = {}

    # Loop through each city and calculate averages
    for city in city_weather:
        temperature_count = city_weather[city]['temperature_count']
        humidity_count = city_weather[city]['humidity_count']

        # Calculate average temperature and humidity for each city
        avg_temperature = city_weather[city]['temperature_total'] / temperature_count if temperature_count > 0 else None
        avg_humidity = city_weather[city]['humidity_total'] / humidity_count if humidity_count > 0 else None

        # Store the results
        aggregated_data[city] = {
            'average_temperature': avg_temperature,
            'average_humidity': avg_humidity
        }

    return aggregated_data

# Example usage
records = [
    {'city': 'New York', 'temperature': 22, 'humidity': 60},
    {'city': 'Los Angeles', 'temperature': 28},
    {'city': 'New York', 'humidity': 65},
    {'city': 'Los Angeles', 'temperature': 30, 'humidity': 40},
    {'city': 'Chicago', 'temperature': 15, 'humidity': 55}
]

result = aggregate_weather_data(records)
print(result)
