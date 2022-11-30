
# this is the "web_app/routes/unemployment_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

#from app.FINANCE_DSS import tool_1, tool_2, tool_3

dss_routes = Blueprint("DSS_routes", __name__)


@dss_routes.route("/dss/dashboard")
def DSS_dashboard():
    print("DECISION SUPPORT SYSTEM...")

    try:




        #flash("Fetched Latest Unemployment Data!", "success")
        return render_template("DSS.html",
        data = [1,2,3]

        )
    except Exception as err:
        print('OOPS', err)

        #flash("Unemployment Data Error. Please try again!", "danger")
        return redirect("/")

#
# API ROUTES
#

#@DSS_routes.route("/api/unemployment.json")
#def unemployment_api():
 #   print("UNEMPLOYMENT DATA (API)...")
#
 #   try:
  #      data = fetch_unemployment_data()
   #     return data
    #except Exception as err:
     #   print('OOPS', err)
      #  return {"message":"Unemployment Data Error. Please try again."}, 404