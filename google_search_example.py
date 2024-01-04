from googlesearch import search


def google_search(keyword, num_results=10):
    try:
        search_results = list(search(keyword, num_results=num_results))
        return search_results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


if __name__ == "__main__":
    keyword = input("Enter the keyword to search for: ")
    num_results = int(input("Enter the number of results you want (default is 10): ") or 10)

    results = google_search(keyword, num_results)

    if results:
        print(f"Top {num_results} results for '{keyword}':")
        for i, result in enumerate(results, start=1):
            print(f"{i}. {result}")
    else:
        print("No results found.")
