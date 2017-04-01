
from flask import Flask, render_template, request
import os
import map
import dbSearch




app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def menu():
      if request.method == "POST":
        data = request.form['text']
        bldg = dbSearch.mysql_search(data)
        result = map.add_building(bldg)
        return render_template('Menu.html', data = bldg, maps = result)
      else:
        bldg = dbSearch.mysql_search('wlit 118')
        result = map.add_building(bldg)
        return render_template('Menu.html', data = bldg, maps = result)



# @app.route('/mapfunction', methods=['GET', 'POST'])
# def datainput():
#     if request.method == "POST":
#         data = request.form['text']['text']
#         bldg = dbSearch.mysql_search(data)
#         result = map.add_building(bldg)
#         return render_template('Menu.html', data = data)
#     else:
#         return render_template('Menu.html', data = None)





port = os.getenv('PORT', '5001')
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=int(port), use_reloader=False)
