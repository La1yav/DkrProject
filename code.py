from flask import Flask\napp = Flask(__name__)\n@app.route('/')\ndef home():\n    return 'Hello, Flask!'\nif __name__ == '__main__':\n    app.run(debug=True)
