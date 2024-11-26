import json

def merge_json_files(file_paths):
    merged_data = []
    seen_urls = set()  # Using a set to track URLs

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                # Check if the URL is unique
                if item['url'] not in seen_urls:
                    merged_data.append(item)
                    seen_urls.add(item['url'])

    return merged_data

# List of JSON file paths
json_files = ["result/kamala_harris_news.json", "result/kamala_harris_news_2.json", "result/kamala_harris_news_3.json"]

# Merge the JSON files
merged_data = merge_json_files(json_files)

# Save the merged data to a new JSON file
with open("kamala_harris_news.json", "w") as output_file:
    json.dump(merged_data, output_file, indent=4)

print("Merging complete. Data saved to 'kamala_harris_news.json'.")