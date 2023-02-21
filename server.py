from flask import Flask,render_template

app = Flask(__name__)

@app.route('/', defaults={'x': 8, 'y': 8})
@app.route('/<int:y>' , defaults={'x': 8})
@app.route('/<int:x>/<int:y>' , defaults={'color1': 'black','color2': 'white'})
@app.route('/<int:x>/<int:y>/<string:color1>' , defaults={'color2': 'white'})
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def construct(x,y,color1,color2):
    print(color1)
    print(color2)   
    board = []
    pair = False
    for i in range(0,x):
        row = []
        
        if pair:
            row.append('dark')
        else:
            row.append('light')
        for c in range(1,y):
            if row[c-1] == 'dark':
                row.append('light')
            else:
                row.append('dark')
        pair = not pair
        print(pair)
        board.append(row)
    color1 = f'style=background-color:{color1}'
    color2 = f'style=background-color:{color2}'
    return render_template("index.html", board = board, color1=color1 , color2 = color2)



if __name__ == "__main__":
    app.run(debug = True, port=5000)