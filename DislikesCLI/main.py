import re, requests, argparse
from flask import Flask, request, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/get_id', methods=['POST'])
def get_id():
    url = request.form['id']
    match = re.search("(?:v=|be/|shorts/)([a-zA-Z0-9-]+)", url)
    if match:
        video_id = match.group(1)
        return render_template('id.html', video_id=video_id)
    else:
        print("The link does not contain a valid YouTube video ID.")

@app.route('/get_stats', methods=['POST'])
def get_stats():
    url = request.form['url']
    match = re.search("(?:v=|be/|shorts/)([a-zA-Z0-9-]+)", url)
    if match:
        video_id = match.group(1)
        getInfo = requests.get(
            f"https://returnyoutubedislikeapi.com/votes?videoId={video_id}"
        ).json()
        views = getInfo["viewCount"]
        likes = getInfo["likes"]
        dislikes = getInfo["dislikes"]
        totalVotes = int(likes + dislikes)
        deleted = getInfo["deleted"]
        views = "{:,}".format(views).replace(",", ".")
        likes = "{:,}".format(likes).replace(",", ".")
        dislikes = "{:,}".format(dislikes).replace(",", ".")
        totalVotes = "{:,}".format(totalVotes).replace(",", ".")
        return render_template('stats.html', views=views, likes=likes, dislikes=dislikes, totalVotes=totalVotes, deleted=deleted)
    else:
        return "The link does not contain a valid YouTube video ID."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Retrieve video information from YouTube.")
    parser.add_argument("mode", choices=["get_id", "get_stats","web_ui"], help="The mode to run the program in.")
    parser.add_argument("-u", "--url", help="The YouTube video URL.")
    args = parser.parse_args()

    if args.mode == "get_id":
        video_id = get_id(args.url)
        if video_id:
            print("Video ID:", video_id)
        else:
            print("The link does not contain a valid YouTube video ID.")
    elif args.mode == "get_stats":
        video_id = get_id(args.url)
        if video_id:
            get_stats(video_id)
        else:
            print("The link does not contain a valid YouTube video ID.")
    elif args.mode == "web_ui":
        app.run(host='0.0.0.0',port=8000)