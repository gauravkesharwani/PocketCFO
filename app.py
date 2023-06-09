import chatter
import logging
from flask import Flask, render_template, request, session
from datetime import datetime, timedelta

app = Flask(__name__)
app.static_folder = 'static'
# A very simple Flask Hello World app for you to get started with...

# Setup the secret key and the environment
app.config.update(SECRET_KEY='osd(99092=36&462134kjKDhuIS_d23', ENV='development')

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=4)

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'

)

logger = logging.getLogger(__name__)


@app.before_request
def check_session():
    if "login_time" not in session:
        session["login_time"] = str(datetime.now())


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    # login_time = datetime.strptime(session["login_time"], "%Y-%m-%d %H:%M:%S.%f")
    # elapsed_time = datetime.now() - login_time
    # print(elapsed_time.total_seconds())
    # if elapsed_time.total_seconds() > 180:
    #     session.clear()
    #     return "Looks like I was not able to help you, you can contact one of our concierges at contact@taramind.com"

    userText = request.args.get('msg')
    logger.debug("Conversation Customer:" + userText)

    response = chatter.get_response(userText)
    logger.debug("Conversation Chatbot: " + response)

    return response


if __name__ == "__main__":
    app.run(debug=True)
