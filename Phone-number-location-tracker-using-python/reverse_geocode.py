from opencage.geocoder import OpenCageGeocode

# Your OpenCage API key
key = "715c0ade80c74a559d4d56e85c636288"

def reverse_geocode(lat, lng):
    try:
        geocoder = OpenCageGeocode(key)
        result = geocoder.reverse_geocode(lat, lng)

        if result:
            formatted_address = result[0]['formatted']
            print(f"Address: {formatted_address}")
            return formatted_address
        else:
            print("No result found.")
            return None
    except opencage.geocoder.NotAuthorizedError:
        print("Error: Your API key is not authorized. Please check your OpenCage API key.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    lat = 23.00357
    lng = 71.74960
    reverse_geocode(lat, lng)
