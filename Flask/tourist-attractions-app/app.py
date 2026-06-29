from flask import Flask, render_template, request, redirect, url_for
from locations import Locations
from forms import AddLocationForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET_PROJECT'

visit = Locations()
categories = {"recommended": "Recommended", "tovisit": "Places To Go", "visited": "Visited!!!"}

UP_ACTION = "\u2197"
DEL_ACTION = "X"

@app.route("/<category>", methods=["GET", "POST"])
def locations(category):
    locations = visit.get_list_by_category(category)
    ## Create form instance
    add_location = AddLocationForm()
    add_form = AddLocationForm(csrf_enabled=False)
    ## Check the request for form data and process
    if request.method == "POST":
        [(name, action)] = request.form.items()

        if action == UP_ACTION:
            visit.moveup(name)
        elif action == DEL_ACTION:
            visit.delete(name)

    ## Return the main template with variables
    return render_template(
        "locations.html",
        template_category=category,
        template_categories=categories,
        template_locations=locations,
        add_location=add_location   # <-- fixed comma
    )


@app.route("/add_location", methods=["POST"])
def add_location():
    ## Validate and collect the form data
    add_form = AddLocationForm(csrf_enabled=False)
    if add_form.validate_on_submit():
        # Collect form data
        name = add_form.name.data
        description = add_form.description.data
        category = add_form.category.data

        # Add the new location
        visit.add(name, description, category)

        # Redirect to the category page chosen
        return redirect(
            url_for("locations", category=category, _external=True, _scheme="http")
        )

    # If validation fails, redirect to recommended
    return redirect(
        url_for("locations", category="recommended", _external=True, _scheme="http")
    )


@app.route("/")
def index():
    ## Redirect to locations route function
    return redirect(
        url_for("locations", category="recommended", _external=True, _scheme="http")
    )
