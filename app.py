from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)

app . secret_key = 'mypassword123'

@app.route('/')
def index():
    session ['question'] = 1
    return render_template('index.html')

@app.route('/techniques/')
def tech():
    session ['question'] = 1
    return render_template('techniques.html')

@app.route('/equipment/')
def equip():
    session ['question'] = 1
    return render_template('equipment.html')

@app.route('/grading/')
def grade():
    session ['question'] = 1
    return render_template('grading.html')

@app.route('/types/')
def types():
    session ['question'] = 1
    return render_template('types.html')

@app.route('/game/')
def game():
    q = None 
    qa = {'1':{'text' : 'What should you before getting on the wall?',
                'answer': '3',
                'answers': ['Nothing, just straight to climbing','Jog on the spot for 10 seconds','Warm Up and Stretch','Run around the mats to find a good climb']
         },  
          '2':{'text' : 'What are you allowed to bring onto the crash mats?',
                'answer': '2',
                'answers': ['A metal waterbottle','A chalk bag','A big rock','A knife']
         },
          '3':{'text' : 'Which technique would be used on a small edge, mainly utilising your fingertips?',
                'answer': '1',
                'answers': ['Crimping','Open-hand grip','Dynamic Movement','Flagging']
         },  
          '4':{'text' : 'What is is the most valuable technique for efficient climbing',
                'answer': '3',
                'answers': ['Toe hook','Smearing','Footwork','Mantling']
         },      
          '5':{'text' : 'What does putting chalk on your hands before climbing do?',
                'answer': '1',
                'answers': ['Keep your hands dry','Make the holds look cooler','Make your hands more sticky to improve grip','To add chalk to the hold making it rougher']
         }, 
          '6':{'text' : 'Why is using a helmet important practice when climbing outside?',
                'answer': '2',
                'answers': ['It stops the seagulls from trying to take your hair to build a nest','It protects the head from falling debris or accidental impacts','It isnt helmets are for losers','You can use it to push against the wall in desperate situations']
        }, 
          '7':{'text' : 'Which technique requires you to press your climbing shoe directly against the wall to create friction',
                'answer': '4',
                'answers': ['Heel hook','Flagging','Toe hook','Smearing']
        }
    }
    try:
        if (session['question']):
            q = int(session['question'])
    except KeyError:
        q = 1

    answer = request.args.get('answer', None)
    if answer is not None:
        correct = qa.get(str(q)).get('answer')
        if str(answer) == str(correct):
            q = q + 1
            session['question'] = q
            if q > len(qa):
                return redirect ('/win/')
            else:
                return render_template('game.html', text=qa[str(q)]['text'], answers=qa[str(q)]['answers'], number = q)
        else:
            return redirect('/lose/')
    else:
        return render_template('game.html', text=qa[str(q)]['text'], answers=qa[str(q)]['answers'], number = q)

@app.route('/win/')
def win():
    session ['question'] = 1
    return render_template('win.html')

@app.route('/lose/')
def loss():
    session ['question'] = 1
    return render_template('lose.html')

if __name__ == "__main__":
    app.run(debug=True)