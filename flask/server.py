#需要安装包
#sudo pip3 install flask_failsafe  flask_cors flask-mysql

from flask_failsafe import failsafe

def create_app():
    from uniquemachine_app import app
    return app

if __name__ == "__main__":
    create_app().run(host = '0.0.0.0')

