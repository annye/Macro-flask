import os
from flask import Flask, render_template, request, current_app
from flask_pager import Pager
import pdb
import sys 
import json


app = Flask(__name__)
app.secret_key = os.urandom(42)
app.config['PAGE_SIZE'] = 1
app.config['VISIBLE_PAGE_COUNT'] = 10


def open_json_files(filepath, input_dict):
    """ Open Json File"""
    try:
        with open(filepath) as data_file:
            input_dict = json.load(data_file)
    except IOError as e:
        print(e)
        print('IOError: Unable to open json Terminating execution')
        sys.exit(1)
    return input_dict

cwd = os.getcwd()
destinations = {}

JSON_FILE_PATH = '%s/%s' % (cwd, '//destinations.json')
destination_dict = open_json_files(JSON_FILE_PATH,
                                destinations
                                )

responses2 = destination_dict['Greece']
responses3 = destination_dict['Cyprus']

@app.route("/")
def index():
    page = int(request.args.get('page', 1))
 
    count = 10
    data = responses2
    data2 = responses3
    pager = Pager(page, count)
    
    pages = pager.get_pages()
   
    skip = (page - 1) * current_app.config['PAGE_SIZE']
    
    limit = current_app.config['PAGE_SIZE']
    data_to_show = data[skip: skip + limit]
   
    return render_template('index.html', pages=pages,data_to_show=data_to_show)




if __name__ == '__main__':
    app.run(debug=True)
