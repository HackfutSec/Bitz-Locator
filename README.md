# 📍 **Bitz Locator**  

## 📚 **Description**  
**Bitz Locator** is a Python-based phone number geolocation tool that retrieves and displays detailed information about a phone number, including location, carrier, and a visual map representation. Powered by OpenCage API, this tool offers precise geolocation data for security auditing and research purposes.  

---

## ⚙️ **Features**  
- ✅ **Phone Number Geolocation:** Get detailed information about a phone number's approximate location.  
- ✅ **Carrier Information:** Identify the service provider associated with the phone number.  
- ✅ **Map Integration:** Generate an interactive map using Folium.  
- ✅ **Google Maps Integration:** Direct access to the location via Google Maps.  
- ✅ **API Integration:** OpenCage Geocode API for accurate data retrieval.  

---

## 🚀 **Installation**  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/HackfutSec/Bitz-Locator.git
   cd Bitz-Locator
   ```

2. **Ensure Python is Installed:**  
   ```bash
   python --version
   ```

3. **Install Required Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ **Usage**  

1. **Run the Script:**  
   ```bash
   python bitz_locator.py
   ```

2. **Provide Information:**  
   - Enter the phone number in international format (e.g., `+1XXXXXXXXXX`).  
   - Provide a valid **OpenCage API key**.  

3. **Output Includes:**  
   - Location details (Country, City, Latitude, Longitude).  
   - Service Provider information.  
   - An interactive HTML map saved as `cartefound.html`.  
   - A direct Google Maps link to the location.  

4. **Open the Map:**  
   ```bash
   open cartefound.html
   ```

---

## 🔑 **API Key**  
- You will need a valid **OpenCage API Key**.  
- Get one from [OpenCage Geocoding API](https://opencagedata.com/).  

---

## 📊 **Dependencies**  
- `phonenumbers`  
- `folium`  
- `opencage`  
- `requests`  

Install them via:  
```bash
pip install phonenumbers folium opencage requests
```

---

## 🔒 **Disclaimer**  
⚠️ **This tool is intended for educational and security research purposes only.**  
The author assumes no responsibility for misuse or malicious activities.  

---

## 📞 **Contact**  
- **Author:** Hackfut  
- **Telegram:** [t.me/HackfutSec](https://t.me/HackfutSec)  

---

## 📄 **License**  
This project is licensed under the **MIT License**. See the `LICENSE` file for details.  
