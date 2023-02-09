from flask import Flask, render_template
# Khoi tao Flask
app = Flask(__name__)

# Request
@app.route("/", methods=['GET'])
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7640)