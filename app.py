import gdata.youtube
import gdata.youtube.service
import random
from flask import Flask, render_template, redirect
app = Flask(__name__)

client = gdata.youtube.service.YouTubeService()
query = gdata.youtube.service.YouTubeVideoQuery()

query.vq = 'Music -VEVO'
query.max_results = 50
query.start_index = 1
query.racy = 'include'
query.format = '5'
query.orderby = 'viewCount'

@app.route('/<id>')
def play(id):
    return render_template('index.html', id=id)

def choose():
    #randomly select a video
    feed = client.YouTubeQuery(query)
    choice = random.choice(feed.entry)
    id = choice.media.player.url[32:43]
    return redirect('/'+id)

@app.route('/')
def main():
    return choose()
    

if __name__ == "__main__":
    app.debug = True
    app.run()
