from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home(): return 'Hello, Flask!'\nif __name__ == '__main__': app.run(debug=True)
