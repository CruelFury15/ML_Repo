from flask import Flask
from helper import pets

app = Flask(__name__)
@app.route('/')
def index():
  return f'''
  <h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry friend:</p>
  <ul>
  <li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/cats">Cats</a></li>
  <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''
@app.route('/animals/<pet_type>')
def animals(pet_type):
    pet_list = pets[pet_type]

    html = f"<h1>List of {pet_type}</h1><ul>"
    for index, pet in enumerate(pet_list):
        html += f'<li><a href="/animals/{pet_type}/{index}">{pet["name"]}</a></li>'
    html += "</ul>"

    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    try:
        chosen_pet = pets[pet_type][pet_id]
    except (KeyError, IndexError):
        return "<h1>Pet not found</h1>", 404

    html = f"""
        <h1>{chosen_pet['name']}</h1>
        <img src="{chosen_pet['url']}" alt="{chosen_pet['name']}">
        <p>{chosen_pet['description']}</p>
        <ul>
            <li>Breed: {chosen_pet['breed']}</li>
            <li>Age: {chosen_pet['age']}</li>
        </ul>
        <a href="/animals/{pet_type}">Back to {pet_type} list</a>
    """
    return html

