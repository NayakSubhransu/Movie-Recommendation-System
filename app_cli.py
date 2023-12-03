# app_cli.py

import pickle
import requests
import argparse
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.text import Text

console = Console()

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return full_path, data['overview']

def list_all_movies(page_size=1000, page_number=1):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    table = Table(show_header=True, header_style="bold magenta", title=f"List of Movies (Page {page_number})", box=box.MINIMAL)
    table.add_column("Index", style="dim", justify="right")
    table.add_column("Title", style="bold yellow")

    for i, title in enumerate(movies['title'][start_index:end_index], start=start_index + 1):
        table.add_row(str(i), title)

    console.print(table)

def recommend(movie, num_recommendations=5):
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        raise ValueError(f"[red]Error:[/red] Movie '{movie}' not found in the database.")

    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    recommended_movie_data = []
    for i in distances[1:num_recommendations + 1]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_title = movies.iloc[i[0]].title
        poster_path, overview = fetch_poster(movie_id)
        recommended_movie_data.append({
            'title': movie_title,
            'poster': poster_path,
            'overview': overview
        })

    return recommended_movie_data

def display_recommendations(recommended_movie_data):
    console.print(f"\n[bold green]Top {len(recommended_movie_data)} Recommended Movies:[/bold green]\n")

    for movie in recommended_movie_data:
        panel = Panel(
            Text.from_markup(f"[bold cyan]Title:[/bold cyan] [yellow]{movie['title']}[/yellow]\n[magenta]Overview:[/magenta] {movie['overview']}"),
            title="[green]Movie Details[/green]",
            style="white",
            border_style="red",
            padding=(1, 3),
            # width=100  # Adjust the width as needed
        )
        console.print(panel)

def main():
    parser = argparse.ArgumentParser(description='Movie Recommender System CLI')
    parser.add_argument('--movie', required=True, help='Input movie title for recommendations')
    parser.add_argument('--num_recommendations', type=int, default=5, help='Number of recommendations to show (default: 5)')
    parser.add_argument('--page_number', type=int, default=1, help='Page number for listing movies (default: 1)')

    args = parser.parse_args()

    if args.movie.lower() == 'list':
        list_all_movies(page_number=args.page_number)
        return

    try:
        recommended_movie_data = recommend(args.movie, args.num_recommendations)
        display_recommendations(recommended_movie_data)
    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")

if __name__ == "__main__":
    movies = pickle.load(open('model/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('model/similarity.pkl', 'rb'))

    console.print("\n[bold yellow]Welcome to the Movie Recommender CLI![/bold yellow]\n")
    main()
    console.print("\n[bold yellow]Thank you for using the Movie Recommender CLI![/bold yellow]\n")
