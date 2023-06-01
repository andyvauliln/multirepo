app = Flask(__name__)


@app.route('/api/v1')
def home():
    return 'API Home page'


@app.route('/api/v1/about')
def about():
    return 'API About page'
