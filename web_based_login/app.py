
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Hardcoded credentials for demo purposes
DEMO_USER = "admin"
DEMO_PASS = "123456"

@app.route('/')
def home():
    return render_template('index.html')

# NEW ROUTE: Serves the landing page after successful login
@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data:
        return jsonify({"message": "Invalid request payload"}), 400
        
    username = data.get('username')
    password = data.get('password')

    # Server-side validation check
    if not username or not password:
        return jsonify({"message": "Username and password cannot be empty"}), 400

   
    if username == DEMO_USER and password == DEMO_PASS:
        
        return jsonify({
            "message": "Login Successful! Redirecting...",
            "redirect_url": "/welcome"
        }), 200
    else:
        return jsonify({"message": "Invalid username or password."}), 401

if __name__ == '__main__':
    app.run(debug=True)