from geopy.geocoders import Nominatim
import pandas
from send_email import send_email

nom = Nominatim(user_agent="my-app")

df=pandas.read_csv("address.csv")

#nom.geocode("3995 23rd St, San Francisco, CA 94114")

#nom.geocode("723133 ")

df["Coordinates"]=df["Address"].apply(nom.geocode)
df["Latitude"] = df ["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df ["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)