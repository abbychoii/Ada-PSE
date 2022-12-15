def get_highest_rated(restaurants):
    highest_rating = 0
    highest_rating_restaurant = {}
    if len(restaurants) >= 1:
        for restaurant in restaurants:
            if restaurant["rating"] > highest_rating: 
                highest_rating_restaurant = restaurant
        return highest_rating_restaurant
    return None

# restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]
# restaurants = [{"name": "Crow's Nest", "rating": 1}]
restaurants = []
print(get_highest_rated(restaurants))

