from flask import Flask
from colorama import Fore, Style

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <body>
            <h1 style='color: red;'>This is my Docker first project</h1>
            <p style='color: green;'>Created Successfully.</p>
            <p style='color: blue;'>Have a Nice Day.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)