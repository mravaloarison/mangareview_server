from flask import Flask, request, jsonify
from flask_cors import CORS
from helpers import filter_data, get_details
import requests


app = Flask("__name__")
CORS(app, resources={r"/*": {"origin": "http://localhost:3000"}})


@app.route("/")
def main():
    filtered_data = [
        {
            'name': 'Latest update',
            'data': filter_data('https://kitsu.io/api/edge/manga?page[limit]=5&sort=updatedAt')
        },
        {
            'name': 'Most popular',
            'data': filter_data('https://kitsu.io/api/edge/trending/manga?page[limit]=5')
        },
        {
            'name': 'Start a new manga',
            'data': filter_data('https://kitsu.io/api/edge/manga?page[limit]=5&sort=-startDate')
        }
    ]

    return jsonify(filtered_data)

@app.route('/manga/<int:id>')
def manga(id):
    detail = get_details(f'https://kitsu.io/api/edge/manga/{id}')
    return jsonify(detail)