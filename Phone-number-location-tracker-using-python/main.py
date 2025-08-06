import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

# Your OpenCage API key
key = "715c0ade80c74a559d4d56e85c636288"

def track_phone_number(number, region="IN"):
    try:
        # Parse the phone number
        new_number = phonenumbers.parse(number, region)

        # Get location and carrier
        location = geocoder.description_for_number(new_number, "en")
        service_name = carrier.name_for_number(new_number, "en")
        
        print(f"Location: {location}")
        print(f"Carrier: {service_name}")

        # Geocode the location
        geocoder_service = OpenCageGeocode(key)
        query = str(location)
        result = geocoder_service.geocode(query)

        if result:
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']
            print(f"Latitude: {lat}, Longitude: {lng}")

            # Create a map with the location marker
            my_map = folium.Map(location=[lat, lng], zoom_start=9)
            folium.Marker([lat, lng], popup=location).add_to(my_map)
            my_map.save("location.html")
            print("Location tracking completed. Check the 'location.html' file.")

            # Reverse geocode the coordinates
            reverse_result = geocoder_service.reverse_geocode(lat, lng)
            if reverse_result:
                formatted_address = reverse_result[0]['formatted']
                print(f"Address: {formatted_address}")
            else:
                print("Reverse geocoding result not found.")
        else:
            print("Geocoding result not found.")

    except phonenumbers.NumberParseException as e:
        print(f"Error parsing number: {e}")
    except opencage.geocoder.NotAuthorizedError:
        print("Error: Your API key is not authorized. Please check your OpenCage API key.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    number = input("Please give your number (with country code, e.g., +919550722677): ")
    track_phone_number(number)
    print("Thank you")
