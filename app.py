import secrets  # Secure random numbers ku idhu dhaan best
import string
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12)) # User kitta irundhu length vaangurem
        
        # ABCD, 1234, and symbols ellathayum mix panrom
        chars = string.ascii_letters + string.digits + string.punctuation
        
        # Secure-ah password generate panrom
        password = ''.join(secrets.choice(chars) for i in range(length))
        
    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)