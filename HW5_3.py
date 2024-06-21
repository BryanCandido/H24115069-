import csv

file_name = "IMDB-Movie-Data.csv"

# Reads movie data from a CSV file and returns a list of dictionaries
def read_movie_data(file_name):
    movie_data = []
    with open(file_name, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Actors"] = row["Actors"].split("|")  # Splitting actors by "|"
            movie_data.append(row)
    return movie_data

# Returns the top 3 movies with the highest ratings in the year 2016
def top_3_movies_highest_ratings_2016(movie_data):
    movies_2016 = [movie for movie in movie_data if movie["Year"] == "2016"]
    sorted_movies = sorted(movies_2016, key=lambda x: float(x["Rating"]), reverse=True)
    top_3_movies = sorted_movies[:3]
    return top_3_movies

# Returns the director who is involved in the most movies
def director_most_movies(movie_data):
    directors = {}
    for movie in movie_data:
        director = movie["Director"]
        directors[director] = directors.get(director, 0) + 1
    sorted_directors = sorted(directors.items(), key=lambda x: x[1], reverse=True)
    return sorted_directors[0][0]

# Returns the actor generating the highest total revenue from their movies
def actor_highest_total_revenue(movie_data):
    actors_revenue = {}
    for movie in movie_data:
        actors = movie["Actors"]
        revenue = float(movie["Revenue (Millions)"]) if movie["Revenue (Millions)"] else 0
        main_actor = actors[0]  # Consider only the first actor as the main actor
        actors_revenue[main_actor] = actors_revenue.get(main_actor, 0) + revenue
    sorted_actors = sorted(actors_revenue.items(), key=lambda x: x[1], reverse=True)
    return sorted_actors[0][0]

# Returns the average rating of movies in which Emma Watson has acted
def average_rating_emma_watson_movies(movie_data):
    emma_watson_movies = [movie for movie in movie_data if "Emma Watson" in movie["Actors"]]
    total_ratings = sum(float(movie["Rating"]) for movie in emma_watson_movies)
    average_rating = total_ratings / len(emma_watson_movies) if len(emma_watson_movies) > 0 else 0
    return average_rating

# Returns the top 4 actors who have played the most number of movies
def top_4_actors_most_movies(movie_data):
    actors_movies = {}
    for movie in movie_data:
        actors = movie["Actors"]
        for actor in actors:
            actors_movies[actor] = actors_movies.get(actor, 0) + 1
    sorted_actors = sorted(actors_movies.items(), key=lambda x: x[1], reverse=True)
    return sorted_actors[:4]

# Returns the top 7 frequent collaboration pairs of directors and actors
def top_7_collaboration_pairs_director_actor(movie_data):
    director_actor_pairs = {}
    for movie in movie_data:
        director = movie["Director"]
        actors = movie["Actors"]
        for actor in actors:
            pair = (director, actor)
            director_actor_pairs[pair] = director_actor_pairs.get(pair, 0) + 1
    sorted_pairs = sorted(director_actor_pairs.items(), key=lambda x: x[1], reverse=True)
    return sorted_pairs[:7]

# Returns the top 3 directors who collaborate with the most number of actors
def top_3_directors_collaborate_most_actors(movie_data):
    director_actors = {}
    for movie in movie_data:
        director = movie["Director"]
        actors = movie["Actors"]
        if director not in director_actors:
            director_actors[director] = set()
        director_actors[director].update(actors)
    sorted_directors = sorted(director_actors.items(), key=lambda x: len(x[1]), reverse=True)
    return sorted_directors[:3]

# Returns the top 6 actors who have played in the most number of genres of movies
def top_6_actors_most_movie_genres(movie_data):
    actors_genres = {}
    for movie in movie_data:
        actors = movie["Actors"]
        genres = movie["Genre"]
        for actor in actors:
            if actor not in actors_genres:
                actors_genres[actor] = set()
            actors_genres[actor].update(genres)
    sorted_actors = sorted(actors_genres.items(), key=lambda x: len(x[1]), reverse=True)
    return sorted_actors[:6]

# Returns the top 3 actors whose movies lead to the largest maximum gap of years
def top_3_actors_largest_max_year_gap(movie_data):
    actors_movies = {}
    for movie in movie_data:
        actors = movie["Actors"]
        for actor in actors:
            if actor not in actors_movies:
                actors_movies[actor] = []
            actors_movies[actor].append(movie)

    actors_max_gaps = {}
    for actor, movies in actors_movies.items():
        years = get_movie_years(movies)
        max_gap = calculate_max_year_gap(years)
        actors_max_gaps[actor] = max_gap

    sorted_actors = sorted(actors_max_gaps.items(), key=lambda x: x[1], reverse=True)
    return sorted_actors[:3]

# Returns the years of movies from the given list of actor_movies
def get_movie_years(actor_movies):
    years = [int(movie["Year"]) for movie in actor_movies]
    return years

# Calculates the maximum gap in years between consecutive years in the given list
def calculate_max_year_gap(years):
    max_gap = 0
    years.sort()
    for i in range(1, len(years)):
        gap = years[i] - years[i-1]
        if gap > max_gap:
            max_gap = gap
    return max_gap

# Main program
file_name = "IMDB-Movie-Data.csv"
movie_data = read_movie_data(file_name)

# Question 1
print("\nTop-3 movies with the highest ratings in 2016:")
top_movies_2016 = top_3_movies_highest_ratings_2016(movie_data)
for i, movie in enumerate(top_movies_2016, 1):
    print(f"{i}. {movie['Title']}, Rating: {movie['Rating']}")

# Question 2
most_movies_director = director_most_movies(movie_data)
print(f"\nThe director involved in the most movies: {most_movies_director}")

# Question 3
highest_revenue_actor = actor_highest_total_revenue(movie_data)
print(f"\nThe actor generating the highest total revenue: {highest_revenue_actor}")

# Question 4
emma_watson_avg_rating = average_rating_emma_watson_movies(movie_data)
print(f"\nThe average rating of Emma Watson's movies: {emma_watson_avg_rating}")

# Question 5
print("\nTop-4 actors playing the most movies:")
top_actors_most_movies = top_4_actors_most_movies(movie_data)
for i, actor in enumerate(top_actors_most_movies, 1):
    print(f"{i}. {actor[0]}, Movies: {actor[1]}")

# Question 6
print("\nTop-7 frequent collaboration pairs of director & actor:")
collaboration_pairs = top_7_collaboration_pairs_director_actor(movie_data)
for i, pair in enumerate(collaboration_pairs, 1):
    director, actor = pair[0]
    print(f"{i}. Director: {director}, Actor: {actor}, Collaborations: {pair[1]}")

# Question 7
print("\nTop-3 directors who collaborate with the most actors:")
top_directors_collaborate_most_actors = top_3_directors_collaborate_most_actors(movie_data)
for i, director in enumerate(top_directors_collaborate_most_actors, 1):
    print(f"{i}. {director[0]}, Actors: {len(director[1])}")

# Question 8
print("\nTop-6 actors playing in the most genres of movies:")
top_actors_most_genres = top_6_actors_most_movie_genres(movie_data)
for i, actor in enumerate(top_actors_most_genres, 1):
    print(f"{i}. {actor[0]}, Genres: {len(actor[1])}")

# Question 9
print("\nTop-3 actors whose movies lead to the largest maximum gap of years:")
top_actors_largest_max_gap = top_3_actors_largest_max_year_gap(movie_data)
for i, actor in enumerate(top_actors_largest_max_gap, 1):
    print(f"{i}. {actor[0]}, Maximum Year Gap: {actor[1]}")