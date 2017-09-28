from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

rotation = "rot"
string_input = "text" 

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
            
        <input type="text" name="rot" value={1} />
        
        <textarea name="text">{0}</textarea>
        <input type="submit"/> 
        



    </form>
      <!-- create your form here -->
    </body>
</html>
""".format(string_input,rotation)



@app.route("/encrypt", methods=['POST'])
def encrypt():
     
    string = request.form['text']
    rotation_input = int(request.form['rot'])

    encrypt_text = rotate_string(string, rotation_input)
   
 
   
    return  """
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
            
        <input type="text" name="rot" />
        
        <textarea name="text">{0}</textarea>
        <input type="submit"/> 
        



    </form>
      <!-- create your form here -->
    </body>
</html>
""".format(encrypt_text)
    #new_encrpytion = encrpyt_string
     
@app.route("/")
def index():
    encrypt_string = ""
    rot = ""
    
    return  """
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
            
        <input type="text" name="rot" value={1} />
        
        <textarea name="text">{0}</textarea>
        <input type="submit"/> 
        



    </form>
      <!-- create your form here -->
    </body>
</html>
""".format(encrypt_string, rot)    


 


app.run()