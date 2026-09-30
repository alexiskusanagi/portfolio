from flask import Flask, jsonify, render_template_string, request
import requests

app = Flask(__name__)

# ------------------------------------------------------------------
# CONFIGURATION - INSERT YOUR TMDB API KEY HERE
# ------------------------------------------------------------------
API_KEY = '304354587f5fcd1ae0898cf39f4dc337'
LANGUAGE = "en-US"

GENRES_MAP = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Sci-Fi",
    53: "Thriller",
    10752: "War",
    37: "Western",
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Google Search - Movies Carousel</title>
    <link href="https://jsdelivr.net" rel="stylesheet">
    <link rel="stylesheet" href="https://jsdelivr.net" />
    <style>
        /* Exact Google Search Dark Theme Colors */
        body { background-color: #202124; color: #e8eaed; font-family: 'Google Sans', Roboto, Helvetica, Arial, sans-serif; padding: 30px; }
        .search-container { max-width: 1200px; margin: 0 auto; }
        h1 { font-size: 1.6rem; font-weight: 400; color: #e8eaed; margin-bottom: 20px; display: flex; align-items: center; gap: 15px; }
        h2 { font-size: 1.15rem; font-weight: 400; color: #bdc1c6; margin-top: 30px; margin-bottom: 12px; }
        
        /* Google Style Dropdown Pill */
        .google-pill { background-color: #303134; color: #e8eaed; border: 1px solid #5f6368; border-radius: 100px; padding: 6px 16px; font-size: 0.9rem; cursor: pointer; outline: none; }
        .google-pill:focus { border-color: #8ab4f8; }

        /* Swiper Container Layout */
        .swiper { width: 100%; height: auto; position: relative; overflow: visible !important; }
        .swiper-wrapper { display: flex; }
        .swiper-slide { width: 140px; display: flex; flex-direction: column; cursor: pointer; }
        
        /* Card styling following Google Knowledge Graph cards */
        .card-container { background: #303134; border-radius: 8px; overflow: hidden; border: 1px solid #3c4043; transition: background 0.15s; height: 100%; display: flex; flex-direction: column; }
        .card-container:hover { background: #3c4043; }
        .poster { width: 100%; aspect-ratio: 2/3; object-fit: cover; }
        .movie-title { font-size: 0.8rem; font-weight: 400; padding: 8px; color: #e8eaed; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; line-height: 1.2; text-align: left; }
        
        /* Native Google-like Navigation Circles */
        .swiper-button-next, .swiper-button-prev { background: rgba(32, 33, 36, 0.9); border: 1px solid #5f6368; width: 40px; height: 40px; border-radius: 50%; color: #e8eaed !important; box-shadow: 0 1px 3px rgba(0,0,0,0.4); }
        .swiper-button-next:after, .swiper-button-prev:after { font-size: 14px; font-weight: bold; }
        .swiper-button-disabled { display: none !important; }
        .swiper-button-prev { left: -20px; }
        .swiper-button-next { right: -20px; }
    </style>
</head>
<body>

    <div class="search-container">
        <h1>
            <span>Movies Released In</span>
            <select id="yearSelect" class="google-pill">
                {% for y in range(2027, 2014, -1) %}
                    <option value="{{ y }}" {% if y == 2026 %}selected{% endif %}>{{ y }}</option>
                {% endfor %}
            </select>
        </h1>

        <!-- The container where rows load dynamically via Javascript API requests -->
        <div id="carouselWrapper">
            <div class="text-muted">Loading Google Knowledge Graph...</div>
        </div>
    </div>

    <script src="https://jsdelivr.net"></script>
    <script>
        // Store Swiper instances globally so we can cleanly wipe and rebuild them on year changes
        let activeSliders = [];

        async function loadMovies(year) {
            const wrapper = document.getElementById('carouselWrapper');
            wrapper.innerHTML = '<div class="text-muted">Loading movies...</div>';
            
            // Destroy older instances to clear out browser memory leaks
            activeSliders.forEach(s => { if(typeof s.destroy === 'function') s.destroy(); });
            activeSliders = [];

            try {
                const response = await fetch(`/api/movies?year=${year}`);
                const data = await response.json();
                
                wrapper.innerHTML = ''; // Wipe out loader text

                // Loop through genres sent from Python and dynamically inject the HTML
                for (const [genre, movies] of Object.entries(data)) {
                    if (movies.length === 0) continue;

                    let rowHtml = `
                        <h2>${genre}</h2>
                        <div class="swiper swiper-${genre.replace(/\s+/g, '')}">
                            <div class="swiper-wrapper">
                    `;

                    movies.forEach(movie => {
                        rowHtml += `
                            <div class="swiper-slide">
                                <div class="card-container">
                                    <img class="poster" src="${movie.poster}" alt="${movie.title}" loading="lazy">
                                    <div class="movie-title">${movie.title}</div>
                                </div>
                            </div>
                        `;
                    });

                    rowHtml += `
                            </div>
                            <div class="swiper-button-next"></div>
                            <div class="swiper-button-prev"></div>
                        </div>
                    `;

                    wrapper.insertAdjacentHTML('beforeend', rowHtml);
                }

                // Re-initialize Slider movement behaviors instantly
                document.querySelectorAll('.swiper').forEach(el => {
                    const slider = new Swiper(el, {
                        slidesPerView: 'auto',
                        spaceBetween: 12,
                        slidesPerGroup: 4, // Slide cards over by blocks like Google
                        navigation: {
                            nextEl: el.querySelector('.swiper-button-next'),
                            prevEl: el.querySelector('.swiper-button-prev'),
                        },
                    });
                    activeSliders.push(slider);
                });

            } catch (err) {
                wrapper.innerHTML = '<div class="text-danger">Failed to sync movie results. Check your API key.</div>';
            }
        }

        // Event listener watching user selection changes on the Dropdown selector
        document.getElementById('yearSelect').addEventListener('change', (e) => {
            loadMovies(e.target.value);
        });

        // Trigger initial paint load for the active baseline setting
        loadMovies(document.getElementById('yearSelect').value);
    </script>
</body>
</html>
"""

# HTML Delivery Entry Route
@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

# JSON API Route consumed asynchronously by Frontend Javascript
@app.route("/api/movies")
def api_movies():
    year = request.args.get("year", default=2026, type=int)
    url = f"https://themoviedb.org{API_KEY}&primary_release_year={year}&language={LANGUAGE}&sort_by=popularity.desc&page=1"
    
    response = requests.get(url)
    movies_by_genre = {name: [] for name in GENRES_MAP.values()}
    
    if response.status_code == 200:
        movies_data = response.json().get("results", [])
        for movie in movies_data:
            poster_path = movie.get("poster_path")
            if not poster_path:
                continue
                
            poster_url = f"https://tmdb.org{poster_path}"
            genre_ids = movie.get("genre_ids", [])
            
            for g_id in genre_ids:
                genre_name = GENRES_MAP.get(g_id)
                if genre_name:
                    movies_by_genre[genre_name].append({
                        "title": movie.get("title"),
                        "poster": poster_url
                    })
                    
    return jsonify(movies_by_genre)

if __name__ == "__main__":
    app.run(debug=True)
