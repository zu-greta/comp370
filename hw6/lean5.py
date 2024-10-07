from json import load

def sum_sales(book_sales, game_sales):
	return sum(book_sales) + sum(game_sales)

# helper functions to load the sales data for given year and product type
def load_sales_data(year, product_type):
    return load(f"data/{product_type}_sales_{year}.csv")

# get all the sales data by product type
years = [2022, 2023, 2024]
product_types = ["book", "game"]

# calculate the total sales for each year
total_sales = {}
for year in years:
    book_sales = load_sales_data(year, "book")
    game_sales = load_sales_data(year, "game")
    total_sales[year] = sum_sales(book_sales, game_sales)

'''

# get all the sales data by product type
book_sales_2022 = load("data/book_sales_2022.csv")
book_sales_2023 = load("data/book_sales_2023.csv")
book_sales_2024 = load("data/book_sales_2024.csv")

game_sales_2022 = load("data/game_sales_2022.csv")
game_sales_2023 = load("data/game_sales_2023.csv")
game_sales_2024 = load("data/game_sales_2024.csv")

# calculate the total sales for each year
total_sales_2022 = sum_sales(book_sales_2022, game_sales_2022)
total_sales_2023 = sum_sales(book_sales_2023, game_sales_2023)
total_sales_2024 = sum_sales(book_sales_2024, game_sales_2024)

'''