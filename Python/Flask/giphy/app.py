from flask import Flask, render_template, request
import giphy as gp

app = Flask(__name__)

@app.route("/")
def index():
    """검색어를 입력받음"""
    return render_template("index.html")
    
@app.route("/search")
def search():
    """
    1. 입력받은 검색어로 giphy 요청을 보내 짤방 정보를 받아옴
    2. 받아온 정보를 보여줌
    """
    query = request.args.get("query")
    search_url = gp.join_giphy_url(query, 12)
    res = gp.send_request(search_url)
    infos = gp.get_iurls_titles_ratings_link_from_res(res)
    return render_template("search.html", infos=infos)
    
@app.route("/trending")
def trending():
    """인기있는 짤을 보여준다
    API -> Trending
    """
    trending_url = gp.get_trending_url(6)
    res = gp.send_request(trending_url)
    infos = gp.get_iurls_titles_ratings_link_from_res(res)
    return render_template("trending.html", infos=infos)
    