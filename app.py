from flask import Flask, render_template, request
from stories import story_templates

app = Flask(__name__)

@app.route("/")
def index():
    stories = story_templates
    return render_template("index.html", story_templates=stories.values())

@app.route("/story_prompt", methods=['POST', 'GET'])
def show_story_prompt():
    story_id = request.args["currenttemplate"]
    story = story_templates[story_id]

    return render_template("story_prompt.html",
                           story_id=story_id,
                           prompts=story.prompts)

@app.route("/story")
def show_story():

    story_id = request.args["story_id"]
    story = story_templates[story_id]

    text = story.generate(request.args)
    return render_template("story.html", 
                           text=text,
                           title=story.title)
