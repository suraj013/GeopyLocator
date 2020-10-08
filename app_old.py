from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename

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


app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    global file
    if request.method=='POST':
        email=request.form["email_name"]
        file=request.files["file"]
        file.save(secure_filename("uploaded" + file.filename))
        with open("uploaded"+file.filename,"a") as f :
            f.write("This was added later!")
        send_email(email,df)
        return render_template("success.html")

        #return render_template("index.html", btn="download.html")

#@app.download("/")
#def download():
#    return send_file("uploaded" + file.filename, attatchment_filename="yourfile.csv", as_attatchment=True)

#{% include btn ignore missing %}

if __name__ == '__main__':
    app.debug=True
    app.run()