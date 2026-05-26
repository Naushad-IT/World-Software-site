import os
from flask import Flask, render_template

app = Flask(__name__)

# 📦 WORLD SOFTWARE PRODUCTS DATABASE (SAUDI RIYAL - SAR)
# Aap yahan apni marzi se naye products jod sakte hain ya price badal sakte hain!
PRODUCTS = [
    {
        "name": "Windows 11 Pro Retail Key",
        "category": "Operating System",
        "price": "45 SAR",
        "status": "In Stock",
        "description": "Original lifetime activation digital key with official support."
    },
    {   "name": "Laptop/PC General Maintance",
        "category": "Service",
        "price": "60 SAR",
        "status": "In Stock",
        "description": "Original and Geniun work."
    },
    {
        "name": "Microsoft Office 2021 Pro Plus",
        "category": "Productivity",
        "price": "69 SAR",
        "status": "In Stock",
        "description": "Full version lifetime bind key for 1 PC."
    },
    {
        "name": "Internet Security Antivirus (1 Year)",
        "category": "Cybersecurity",
        "price": "25 SAR",
        "status": "In Stock",
        "description": "Complete protection against malware, ransomware, and phishing."
    },
    {
        "name": "Laptop/PC Formatting & OS Installation",
        "category": "Services",
        "price": "50 SAR",
        "status": "Available",
        "description": "Complete Windows backup, installation, drivers setup, and optimization."
    },
    {
        "name": "Biometric Machine Configuration",
        "category": "Services",
        "price": "60 SAR",
        "status": "Available",
        "description": "ZKTeco or any biometric machine IP configuration and software linking."
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)

if __name__ == '_main_':
    # 🚀 HOSTING LOGIC: Yeh line server ka port automatically detect kar legi
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)