from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "maina_entrepreneur_secure_key_123"

# Comprehensive database of 20 vehicle models matching global trends
CAR_DATABASE = [
    {"name": "Tesla Model Y", "type": "Top-Selling", "image_url": "/static/tesla.jpg", "description": "The world's highest-selling crossover electric vehicle.", "specs": "Range: 320 mi | 0-60: 3.5s"},
    {"name": "Porsche 911 GT3 RS", "type": "New Model", "image_url": "/static/porsche.jpg", "description": "Track-focused engineering with extreme active aerodynamics.", "specs": "Power: 518 hp | Top Speed: 184 mph"},
    {"name": "Toyota RAV4 Hybrid", "type": "Top-Selling", "image_url": "/static/toyota.jpg", "description": "A dominant global sales leader offering supreme hybrid efficiency.", "specs": "MPG: 41 City / 38 Hwy"},
    {"name": "Hyundai Ioniq 5 N", "type": "New Model", "image_url": "/static/hyundai.jpg", "description": "High-performance EV tracking massive driving engagement.", "specs": "Power: 641 hp | 0-60: 3.2s"},
    {"name": "Ford F-150 Lightning", "type": "Top-Selling", "image_url": "/static/ford.jpg", "description": "America's favorite pickup truck re-engineered for the electric era.", "specs": "Towing: 10,000 lbs | Range: 320 mi"},
    {"name": "BMW M4 Competition", "type": "New Model", "image_url": "/static/bmw.jpg", "description": "Aggressive design coupled with twin-turbo performance refinement.", "specs": "Power: 503 hp | inline 6 engine"},
    {"name": "Honda Civic Type R", "type": "Top-Selling", "image_url": "/static/honda.jpg", "description": "The ultimate front-wheel-drive hot hatchback on the market.", "specs": "Engine: 2.0L Turbo | 315 hp"},
    {"name": "Mercedes-AMG SL 63", "type": "New Model", "image_url": "/static/mercedes.jpg", "description": "Luxurious open-top grand tourer re-imagined by AMG.", "specs": "Engine: V8 Biturbo | 577 hp"},
    {"name": "Chevrolet Corvette E-Ray", "type": "New Model", "image_url": "/static/corvette.jpg", "description": "First-ever all-wheel-drive hybrid mid-engine American supercar.", "specs": "0-60 mph: 2.5s | 655 hp Combined"},
    {"name": "Kia EV6 GT", "type": "Top-Selling", "image_url": "/static/kia.jpg", "description": "Award-winning crossover matching sports car acceleration.", "specs": "Power: 576 hp | Charge: 10-80% in 18m"},
    {"name": "Audi RS e-tron GT", "type": "Top-Selling", "image_url": "/static/audi.jpg", "description": "Striking electric sedan combining luxury grand touring with raw speed.", "specs": "Range: 249 mi | 637 hp Boost"},
    {"name": "Mazda CX-90 Premium", "type": "New Model", "image_url": "/static/mazda.jpg", "description": "Three-row flagship SUV built on a rear-biased performance platform.", "specs": "Engine: Inline 6 Turbo Mild-Hybrid"},
    {"name": "Nissan Z Performance", "type": "New Model", "image_url": "/static/nissan.jpg", "description": "A modern homage to iconic classic Japanese sports cars.", "specs": "Engine: Twin-Turbo V6 | 400 hp"},
    {"name": "Volkswagen Golf R", "type": "Top-Selling", "image_url": "/static/vw.jpg", "description": "All-weather performance hatchback with advanced torque vectoring AWD.", "specs": "Power: 315 hp | Drift Mode Included"},
    {"name": "Lexus RX 500h F Sport", "type": "Top-Selling", "image_url": "/static/lexus.jpg", "description": "The pinnacle of reliable premium luxury crossover transportation.", "specs": "Powertrain: Direct4 Hybrid System"},
    {"name": "Land Rover Defender 130", "type": "New Model", "image_url": "/static/defender.jpg", "description": "Extended adventure vehicle built to conquer extreme overlanding trails.", "specs": "Seats: Up to 8 adults | Air Suspension"},
    {"name": "Subaru WRX TR", "type": "New Model", "image_url": "/static/subaru.jpg", "description": "Rally-bred performance sedan equipped with Brembo performance braking.", "specs": "Engine: 2.4L Boxer Turbo | Symmetrical AWD"},
    {"name": "Jeep Wrangler Rubicon 4xe", "type": "Top-Selling", "image_url": "/static/jeep.jpg", "description": "The best-selling plug-in hybrid vehicle in North America.", "specs": "Pure EV Range: 21 mi | Trail Rated"},
    {"name": "Ferrari Purosangue", "type": "New Model", "image_url": "/static/ferrari.jpg", "description": "Ferrari’s legendary first-ever four-door, four-seat high-riding machine.", "specs": "Engine: Naturally Aspirated V12 | 715 hp"},
    {"name": "Volvo EX30 Ultra", "type": "New Model", "image_url": "/static/volvo.jpg", "description": "A small, highly sustainable electric SUV packing a massive punch.", "specs": "0-60 mph: 3.4s | Eco-friendly interior"}
]

@app.route("/")
def home():
    return render_template("home.html", role=session.get("role", "Guest"), username=session.get("username", ""))

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "adminpassword":
            session["username"] = "Admin Account"
            session["role"] = "Admin"
            return redirect(url_for("cars"))
        elif username == "user" and password == "userpassword":
            session["username"] = username
            session["role"] = "User"
            return redirect(url_for("cars"))
        else:
            error = "Invalid credentials. Admin (admin/adminpassword) | User (user/userpassword)"
    return render_template("login.html", error=error)

@app.route("/cars")
def cars():
    # Only allow authenticated sessions to view our structural car catalog
    if "role" not in session:
        return redirect(url_for("login"))
    return render_template("cars.html", cars=CAR_DATABASE, role=session.get("role"), username=session.get("username"))

@app.route("/ads")
def ads():
    return render_template("ads.html", role=session.get("role", "Guest"), username=session.get("username", ""))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)


