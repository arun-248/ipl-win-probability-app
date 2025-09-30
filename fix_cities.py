import joblib
from pathlib import Path

valid_cities = [
    "Ahmedabad",
    "Bangalore",
    "Chennai",
    "Delhi",
    "Hyderabad",
    "Kolkata",
    "Mumbai",
    "Chandigarh",
    "Jaipur",
    "Vizag"
]

ASSETS_PATH = Path("assets/city.pkl")
ASSETS_PATH.parent.mkdir(parents=True, exist_ok=True)

joblib.dump(sorted(valid_cities), ASSETS_PATH)
print("✅ city.pkl updated with only valid cities")
