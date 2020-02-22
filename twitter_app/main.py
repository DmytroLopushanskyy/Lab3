from flask import Flask, request, render_template, redirect
from twitterdata import get_info_by_nickname
from map import build_map

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/', methods=['GET'])
def index():
    """
    Homepage rendering
    """
    return render_template('index.html')


@app.route('/map', methods=['POST'])
def map_from_form():
    """
    Receive form data, validate it, and display results
    """
    username = request.form["name"]
    print(username)
    if username:
        try:
            data = get_info_by_nickname(username)
            check_num = len(data["users"])
        except:
            check_num = 0

        if check_num == 0:
            response = "No friends found for this username!"
            context = {"response": response}
            return render_template('index.html', **context)
        else:
            html_string = build_map(data)
            context = {"html": html_string}
            return render_template('friends.html', **context)
    return redirect('/')


@app.errorhandler(404)
def page_not_found(e):
    """
    Redirect to homepage on Not Found Error
    """
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=3456)
