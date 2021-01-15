#design a Flask API based on the queries that you have just developed.
from flask import Flask, jsonify

##########################
#Flask Setup
##########################
#initialize Flask app
app=Flask(__name__)

#########################
#Flask Routes
#########################
#Home page
#List all routes available
@app.route("/")
def index():
    return(
        f"Welcome to the API"<br/>
        f"Available routes:"<br/>
        f"/api/v1.0/precipitation"<br/>
        f"/api/v1.0/stations"<br/>
        f"/api/v1.0/tobs"<br/>
        f"/api/v1.0/<start>"<br/>
        f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
def precip():
  #Convert the query results to a dictionary using `date` as the key and `prcp` as the value.

  #Return the JSON representation of your dictionary.
    return()

@app.route("/api/v1.0/stations")
def stations():
#Return a JSON list of stations from the dataset.
    return()


@app.route("/api/v1.0/tobs")
def tobs()

  * Query the dates and temperature observations of the most active station for the last year of data.

  * Return a JSON list of temperature observations (TOBS) for the previous year.
    return()

@app.route("/api/v1.0/<start>")
    def start():
        return()

@app.route("/api/v1.0/<start>/<end>")
    def start_end():
        return()
* `/api/v1.0/<start>` and ``

  # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  # When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  # When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.




