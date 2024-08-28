from flask import request, render_template

def init_web_routes(app):
    mycol = app.mycol
    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"

    # PT_family

    ## main page
    @app.route('/PT_family', methods=['GET', 'POST'])
    def pt_main_page():
        return render_template('pt_main.html')

    # page for video
    @app.route('/PT_family/pt_video')
    def pt_video():
        return render_template('pt_video.html')

    # introduce for each pig
    @app.route('/PT_family/<name>', methods=['GET'])
    def Puntang(name):
        item = mycol.find_one({"name": name}, {'_id': 0})
        if item:
            return render_template('pt_pigs.html', name=name, item=item)
        return render_template('pt_pigs.html', name=None, item=None)