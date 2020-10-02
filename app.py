print('start app')
from core import app

import startpage

@app.route('/')
def main():
    return 'Hello from Main!!!'

