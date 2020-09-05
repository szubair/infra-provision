from flask import Flask, render_template, url_for, request, redirect
import json

app = Flask(__name__)

app_dict = {}
resources = {'resources':app_dict}

#dummy = {'appname':'wordpress','provider':'AWS', 'desc':'my personal website'}

@app.route('/')
#HomePage-requirements
def FinalHome():
    return render_template('home-page.html')

#HomePage->Select your application and cloud-resources
@app.route('/home/', methods = ['GET','POST'])
def createApplication():
    if request.method == 'POST':
        app_dict['appName'] = request.form['appname']
        app_dict['desc'] = request.form['desc']
        app_dict['provider'] = request.form['cloudpro']
        with open('app-reqs.json', 'w') as outfile:
            json.dump(resources, outfile)
        return redirect(url_for('viewSelection'))
    else:
        return render_template('page.html')

#Display the selection 
@app.route('/webui/success/')
def viewSelection():
    return render_template('success.html', app_dict=app_dict)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)


