from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    return "Running successfully"


if __name__ == "__main__":
    app.run()