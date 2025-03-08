from duckduckgo_search import DDGS
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
       search_term = request.form.get("search_term")
       if search_term[:3] == "ai|":
           resultsCHAT = DDGS().chat(search_term, model='claude-3-haiku')
           return render_template("ai.html",resultsCHAT=resultsCHAT,search_term=search_term)
       if search_term[:5] == "news|":
           resultsnews = DDGS().news(search_term, max_results=15)
           return render_template("news.html",resultsnews=resultsnews,search_term=search_term)
       if search_term[:6] == "image|":
           resultsimages = DDGS().images(search_term, max_results=200)
           return render_template("images.html",resultsimages=resultsimages,search_term=search_term)
       if search_term[:6] == "video|":
           resultsvid = DDGS().videos(search_term, max_results=10)
           return render_template("video.html",resultsvid=resultsvid,search_term=search_term)
       return redirect("/"+search_term)
    return render_template("index.html")

@app.route('/<search_term>')
def search(search_term):
    results = DDGS().text(search_term, region='wt-wt', max_results=25)
    sr = search_term
    return render_template("results.html", results=results, sr=sr)

if __name__ == '__main__':
    app.run(debug=True)