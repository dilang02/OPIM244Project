
# this is the "web_app/routes/unemployment_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.FINANCE_DSS import tool_1, tool_2, tool_3

DSS_routes = Blueprint("DSS_routes", __name__)


@DSS_routes.route("/DSS/dashboard")
def DSS_dashboard():
    print("DECISION SUPPORT SYSTEM...")

    try:
        from getpass import getpass
        API_KEY = getpass("Please input your AlphaVantage API Key: ")



        #flash("Fetched Latest Unemployment Data!", "success")
        return render_template("DSS.html",
            while True:
                if tool_number == "1": # Call requested functionality based on user input
                    tool_1()
                elif tool_number == "2":
                    tool_2()
                elif tool_number == "3":
                    tool_3() 
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