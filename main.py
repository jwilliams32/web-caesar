from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

rotation = "rot"
string_input = "" 

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
        
    </head>
    <body>
    <form action='/encrypt' method='post'>
        <label for="rot">Rotate by:</label>
            
        <input type="text" name="rot" value="0" />
        
        <textarea name="text">{0}</textarea>
        <input type="submit"/> 
        



    </form>
      <!-- create your form here -->
    </body>
</html>
"""



@app.route("/encrypt", methods=['POST'])
def encrypt():
     
    string = request.form['text']
    rotation_input = int(request.form['rot'])

    encrypt_text = rotate_string(string, rotation_input)
   
    encrypt_string = form.format(encrypt_text)
   
    return encrypt_string
    #new_encrpytion = encrpyt_string
     
@app.route("/")
def index():

    encrypt_string = ""
    
    
    return form.format(encrypt_string)


 


app.run()