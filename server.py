from flask import Flask, render_template   # Import Flask to allow us to create our app
app = Flask(__name__) 



# @app.route("/")
# def printhtml():
#     return render_template("index.html")
    

# When a user visits http://localhost:5000/play, 
# have it render three beautiful looking blue boxes.
# Please use a template to render this.

# @app.route('/play')
# def renderingboxes():
#     return render_template('index.html')


# @app.route('/play/<int:num>')
# def renderingboxes(num):
#     return render_template("index.html", num = num)

# When a user visits localhost:5000/play/(x), 
# have it display the beautiful looking blue boxes x times. 
# For example, localhost:5000/play/7 should display these blue boxes 7 times.


@app.route('/play/<int:num>/<color>')
def renderingboxes(num, color):
    return render_template("index.html", num = num, color = color)

# When a user visits localhost:5000/play/(x)/(color),
# have it display beautiful looking boxes x times,

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)