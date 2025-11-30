import requests
import argparse
from typing import Optional

class Brewery:
    def __init__(
        self,
        id: str,
        name: str,
        brewery_type: str,
        city: str,
        country: str,
        state_province: Optional[str] = None,
        postal_code: Optional[str] = None,
        address_1: Optional[str] = None,
        longitude: Optional[str] = None,
        latitude: Optional[str] = None,
        phone: Optional[str] = None,
        website_url: Optional[str] = None,
        **kwargs
    ):
        self.id: str = id
        self.name: str = name
        self.brewery_type: str = brewery_type
        self.city: str = city
        self.country: str = country
        self.state_province: Optional[str] = state_province
        self.postal_code: Optional[str] = postal_code
        self.address_1: Optional[str] = address_1
        self.longitude: Optional[str] = longitude
        self.latitude: Optional[str] = latitude
        self.phone: Optional[str] = phone
        self.website_url: Optional[str] = website_url,
        

    def __str__(self) -> str:
        return f"{self.name} | Miasto: {self.city} | Typ: {self.brewery_type}"

def main():
 
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", help="Filtrowanie po mieście", type=str, default=None)
    args = parser.parse_args()

    
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {"per_page": 20} #

    
    if args.city:
        params["by_city"] = args.city

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return

   
    breweries_list = []
    for item in data:
       
        brewery = Brewery(**item)
        breweries_list.append(brewery)

   
    for brewery_instance in breweries_list:
        print(brewery_instance)

if __name__ == "__main__":
    main()