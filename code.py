from flask import Flask
import os
import datetime
import subprocess

app = Flask(_name_)

@app.route('/htop')
def system_info():
    # Fetch system username
    username = os.getlogin()
    
    # Get IST time
    ist_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    # Create response HTML
    response = f"""
    <h1>System Information</h1>
    <p><b>Name:</b> Your Full Name</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {ist_time}</p>
    <pre>{top_output}</pre>
    """
    return response

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=5000)
