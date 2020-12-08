from flask import Flask
from flask import render_template #import render_template
 
app = Flask(__name__)
 
 
@app.route('/')
def home():  
    return render_template('index.html') #here we are rendering our template file.
 
 
if __name__ == "__main__":
    app.run(debug=True)
