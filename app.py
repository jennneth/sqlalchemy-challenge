#design a Flask API based on the queries that you have just developed.
import datetime as dt
import numpy as np
import pandas as pd 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#########################
# Database Setup
#########################
engine = create_engine("Sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)

#save reference to  the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

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
        f"Welcome to the Hawaii Climate Analysis API!"<br/>
        f"Available routes:"<br/>
        f"/api/v1.0/precipitation"<br/>
        f"/api/v1.0/stations"<br/>
        f"/api/v1.0/tobs"<br/>
        f"/api/v1.0/<start>"<br/>
        f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
def precip():
    session = Session(engine)
    year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
    results = session.query(Measurement.date, Measurement.prcp)\
        .filter(Measurement.date >= year_ago).all()
    session.close()
 
    #Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    all_results = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_results.append(prcp_dict)

    #set the index in the dictionary
    all_results.set_index('date', inplace = True)
    #Return the JSON representation of your dictionary.
    return jsonify(all_results)

@app.route("/api/v1.0/stations")
def stations():
    #Return a JSON list of stations from the dataset.
    session = Session(engine)
    active_stations = session.query(Measurement.station)\
        .group_by(Measurement.station)\
        .desc().all()
    session.close()
    return jsonify(active_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    # Query the dates and temperature observations of the most active station for the last year of data.
   session=Session(engine)
   year_ago = dt.date(2017,8,23) - dt.timedelta(days=365)
   most_active_station = session.query(Measurement.station, func.count(Measurement.station))\
        .filter(Measurement.date >= year_ago)\
        .group_by(Measurement.station)\
        .order_by(func.count(Measurement.station).desc()).first()
    temps = session.query(Measurement.tobs)\
        .filter(Measurement.station == most_active_station[0])\
        .filter(Measurement.date >= year_ago).all()
    session.close()
  * Return a JSON list of temperature observations (TOBS) for the previous year.
    return jsonify(temps)

@app.route("/api/v1.0/<start>")
    def start():
        return(f"Start module")

@app.route("/api/v1.0/<start>/<end>")
    def start_end():
        return(f"Start End Module")


  # Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  # When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  # When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

if __name__ == '__main__':
    app.run(debug = True)


