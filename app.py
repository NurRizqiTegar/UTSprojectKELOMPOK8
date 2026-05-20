from flask import Flask, render_template, request
import requests

app = Flask(__name__)

JIKAN_BASE = "https://api.jikan.moe/v4"

def fetch_anime(endpoint, params=None):
    try:
        res = requests.get(f"{JIKAN_BASE}{endpoint}", params=params, timeout=10)
        res.raise_for_status()
        return res.json()
    except Exception as e:
        print(f"API Error: {e}")
        return None

@app.route("/")
def index():
    # Ambil top anime
    top_data = fetch_anime("/top/anime", {"limit": 12})
    top_anime = top_data["data"] if top_data else []

    # Ambil seasonal anime (currently airing)
    seasonal_data = fetch_anime("/seasons/now", {"limit": 8})
    seasonal_anime = seasonal_data["data"] if seasonal_data else []

    return render_template("index.html", top_anime=top_anime, seasonal_anime=seasonal_anime)

@app.route("/search")
def search():
    query = request.args.get("q", "").strip()
    genre = request.args.get("genre", "")
    page = int(request.args.get("page", 1))

    if not query and not genre:
        return render_template("search.html", results=[], query="", genre="", page=1, has_next=False)

    params = {"limit": 16, "page": page}
    if query:
        params["q"] = query
    if genre:
        params["genres"] = genre

    data = fetch_anime("/anime", params)
    results = data["data"] if data else []
    has_next = data["pagination"]["has_next_page"] if data and "pagination" in data else False

    return render_template("search.html", results=results, query=query, genre=genre, page=page, has_next=has_next)

@app.route("/anime/<int:anime_id>")
def detail(anime_id):
    data = fetch_anime(f"/anime/{anime_id}/full")
    anime = data["data"] if data else None

    # Ambil karakter
    char_data = fetch_anime(f"/anime/{anime_id}/characters")
    characters = char_data["data"][:8] if char_data else []

    return render_template("detail.html", anime=anime, characters=characters)

@app.route("/genre/<int:genre_id>")
def genre(genre_id):
    page = int(request.args.get("page", 1))
    data = fetch_anime("/anime", {"genres": genre_id, "limit": 16, "page": page})
    results = data["data"] if data else []
    has_next = data["pagination"]["has_next_page"] if data and "pagination" in data else False

    # Nama genre dari data pertama
    genre_name = "Genre"
    if results and results[0].get("genres"):
        for g in results[0]["genres"]:
            if g["mal_id"] == genre_id:
                genre_name = g["name"]
                break

    return render_template("genre.html", results=results, genre_id=genre_id, genre_name=genre_name, page=page, has_next=has_next)

if __name__ == "__main__":
    app.run(debug=True)
