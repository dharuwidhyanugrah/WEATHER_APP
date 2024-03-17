import streamlit as st
import requests
from datetime import datetime

API_KEY ="b74b14e5a74aa003391444764d3c0561"

def searchCity(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    weather = requests.get(url)
    weather = weather.json()

    desc = weather['weather'][0]['description']
    ico = weather['weather'][0]['icon']
    temp = weather['main']['temp']
    pressure = weather['main']['pressure']
    humidity = weather['main']['humidity']
    windspeed = weather['wind']['speed']
    lat = weather['coord']['lat']
    lon = weather['coord']['lon']

    url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"

    payload = {
            "voice_code": "en-US-1",
            "text": f"Hello, weather in {city} now is {desc} with the temperature {temp} fahrenheit and {humidity} relative humidity",
            "speed": "1.00",
            "pitch": "1.00",
            "output_type": "audio_url"
        }
    headers = {
            "content-type": "application/x-www-form-urlencoded",
            "X-RapidAPI-Key": "aa09f13f82mshdd259c17a2dd331p1d81fdjsna2eb9616385f",
            "X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
            }

    suara = requests.post(url, data=payload, headers=headers)
    suara = suara.json()
        
    linksuara = suara['result']['audio_url']

    return linksuara, desc, ico, temp, pressure, humidity, windspeed, lat, lon 


def predWeather(lat, lon):
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}"

    pred = requests.get(url)
    pred = pred.json()
    return pred

def convTime(dt):
    normalDate = datetime.fromtimestamp(dt)
    return normalDate


st.title('Weather App')

city = st.text_input("Search City...")
if st.button("Search"):
    linksuara, desc, ico, temp, pressure, humidity, windspeed, lat, lon = searchCity(city) 

    tab1, tab2 = st.tabs(["Current Weather", "Weather Prediction"])

    with tab1:
        st.title("Current Weather")
        st.write(':blue[_This is the summary audio, in case u need it_] :sunglasses:')
        st.audio(linksuara, format='audio/mp3',start_time=0)
        c1, c2, c3, c4, c5, c6 = st.columns(6)

        with c1:
            st.subheader('Weather')
            st.write(desc)

        with c2:
            st.subheader('Icon')
            st.image(f"https://openweathermap.org/img/wn/{ico}@2x.png")

        with c3:
            st.subheader("Temp")
            st.write(f"{temp}&deg;F")

        with c4:
            st.subheader("Pressure")
            st.write(pressure)

        with c5:
            st.subheader("Speed")
            st.write(windspeed)

        with c6:
            st.subheader("Humidity")
            st.write(humidity)

    with tab2:

        st.title(f"Weather Prediction in {city}")
        pred = predWeather(lat, lon)
        
        for i in pred['list']:
            iconPred = i['weather'][0]['icon']
            col1, col2,= st.columns(2)
            with col1:
                st.header(i['weather'][0]['description'])
                st.subheader(f"{i['main']['temp']}&deg;F" )
                st.image(f"https://openweathermap.org/img/wn/{iconPred}@2x.png")
            with col2:
                st.write(convTime(i['dt']))






# url = "https://cloudlabs-text-to-speech.p.rapidapi.com/synthesize"

# payload = {
#     "voice_code": "id-ID-1",
#     "text": f"Halo, untuk cuaca di {city} saat ini sedang {description} dengan temperatur {temp} dan kecepatan angin {windspeed}",
#     "speed": "1.00",
#     "pitch": "1.00",
#     "output_type": "audio_url"
# }
# headers = {
#     "content-type": "application/x-www-form-urlencoded",
#     "X-RapidAPI-Key": "07b2dd685emsh238ae8fcb562c7ap164b2ajsn0e014b229f45",
#     "X-RapidAPI-Host": "cloudlabs-text-to-speech.p.rapidapi.com"
#     }

# suara = requests.post(url, data=payload, headers=headers)
# suara = suara.json()
    
# linksuara = suara['result']['audio_url']


# def play_audio_from_url(url):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             audio_bytes = io.BytesIO(response.content)
#             audio = AudioSegment.from_file(audio_bytes, format="ogg")
#             st.audio(audio_bytes, format="audio/ogg", start_time=0)
#         else:
#             st.error(f"Failed to retrieve audio from {url}")
#     except Exception as e:
#         st.error(f"An error occurred: {str(e)}")

# for link in linksuara:
#     st.write(f"Audio dari: {link}")
#     play_audio_from_url(link)
    
# Misalkan 'linksuaraa' adalah list yang berisi URL audio

# Tampilkan UI untuk memainkan audio dari setiap URL
