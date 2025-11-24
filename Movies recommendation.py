import random

# 🎬 Movie Database
movies = {
    "action": ["Avengers: Endgame", "John Wick", "Mad Max: Fury Road", "The Dark Knight"],
    "comedy": ["The Mask", "Home Alone", "21 Jump Street", "Mr. Bean’s Holiday"],
    "horror": ["The Conjuring", "It", "Annabelle", "Insidious"],
    "romance": ["Titanic", "La La Land", "The Notebook", "A Walk to Remember"],
    "sci-fi": ["Interstellar", "Inception", "The Matrix", "Avatar"]
}

def recommend_by_genre():
    print("\nAvailable genres:")
    for genre in movies.keys():
        print("-", genre.capitalize())

    choice = input("\nEnter a genre: ").lower()

    if choice in movies:
        print(f"\n🎬 Recommended {choice.capitalize()} Movies:")
        for movie in movies[choice]:
            print("👉", movie)
    else:
        print("\n❌ Genre not found!")

def random_recommendation():
    genre = random.choice(list(movies.keys()))
    movie = random.choice(movies[genre])
    print("\n🎞 Random Movie Recommendation:")
    print(f"👉 {movie} ({genre.capitalize()})")

def search_movie():
    name = input("\nEnter movie name to search: ").lower()
    found = False
    
    for genre, movie_list in movies.items():
        for movie in movie_list:
            if name in movie.lower():
                print(f"\n🔎 Found: {movie} (Genre: {genre.capitalize()})")
                found = True

    if not found:
        print("\n❌ Movie not found!")

def add_movie():
    genre = input("\nEnter genre: ").lower()
    movie = input("Enter movie name: ")

    if genre in movies:
        movies[genre].append(movie.title())
    else:
        movies[genre] = [movie.title()]

    print("✅ Movie added successfully!")

# 🏁 Main Program Menu
while True:
    print("\n==============================")
    print("🎥 Movie Recommendation System")
    print("==============================")
    print("1️⃣ Recommend movies by genre")
    print("2️⃣ Random movie suggestion")
    print("3️⃣ Search movie by name")
    print("4️⃣ Add your own movie")
    print("5️⃣ Exit")
    
    choice = input("\nEnter your choice: ")

    if choice == "1":
        recommend_by_genre()
    elif choice == "2":
        random_recommendation()
    elif choice == "3":
        search_movie()
    elif choice == "4":
        add_movie()
    elif choice == "5":
        print("\n👋 Thanks for using the system. Enjoy your movie! 🍿")
        break
    else:
        print("\n❌ Invalid choice, try again!")