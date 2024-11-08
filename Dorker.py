import time
import webbrowser
import urllib.parse

# Banner art displayed at the start
banner_art = """
██████╗░░█████╗░██████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░██║██║░░██║██████╔╝█████═╝░█████╗░░██████╔╝
██║░░██║██║░░██║██╔══██╗██╔═██╗░██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░░██║██║░╚██╗███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""
print(banner_art)

# Function to open a URL in the web browser
def open_in_browser(search_query):
    # Encode the search query for the URL
    time.sleep(0.3)
    encoded_query = urllib.parse.quote(search_query)
    webbrowser.open(url=f'https://www.google.com/search?q={encoded_query}')

# Function to print a search query to the console
def display_search_result(query):
    time.sleep(0.3)
    print("\n" + query)

# Function to print a search query formatted for Google Dorking in URL form
def display_search_result_with_url(query):
    time.sleep(0.3)
    print("\n" + f"allinurl:{primary_keyword} {query}")

# Function to print the search query and open it in the browser
def display_and_open_search_result_with_url(query):
    time.sleep(0.3)
    formatted_query = f"allinurl:{primary_keyword} {query}"
    print("\n" + formatted_query)
    open_in_browser(formatted_query)

# Function to print the search query formatted for text-based Google Dorking
def display_search_result_in_text(query):
    time.sleep(0.3)
    print("\n" + f"allintext:{primary_keyword} {query}")

# Function to print the search query in text format and open it in the browser
def display_and_open_search_result_in_text(query):
    time.sleep(0.3)
    formatted_query = f"allintext:{primary_keyword} {query}"
    print("\n" + formatted_query)
    open_in_browser(formatted_query)

# Main function to start the search process and interact with the user
def start_google_dorking_search():
    # Ask user for options on how to search
    open_browser_choice = input("Open in browser? (y/n): ").strip().lower()
    global primary_keyword
    primary_keyword = input("Primary keyword: ").strip()
    has_secondary_keyword = input("Is there another keyword? (y/n): ").strip().lower()

    # List of social media platforms to include in the search
    social_media_platforms = ["x", "reddit", "tiktok", "instagram", "github", "facebook"]

    # Search handling based on user's input
    if has_secondary_keyword == "y" and open_browser_choice == "n":
        secondary_keyword = input("Secondary keyword: ").strip()
        display_search_result_with_url(secondary_keyword)

        for platform in social_media_platforms:
            display_search_result_with_url(f"{secondary_keyword} {platform}")

        display_search_result_in_text(secondary_keyword)

        for platform in social_media_platforms:
            display_search_result_in_text(f"{secondary_keyword} {platform}")

    elif has_secondary_keyword == "n" and open_browser_choice == "n":
        display_search_result(f'"{primary_keyword}"')
        display_search_result(f'inurl:{primary_keyword}')

        for platform in social_media_platforms:
            display_search_result_with_url(platform)

        display_search_result(f'intitle:{primary_keyword}')
        display_search_result(f'intext:{primary_keyword}')

        for platform in social_media_platforms:
            display_search_result_in_text(platform)

    elif has_secondary_keyword == "y" and open_browser_choice == "y":
        secondary_keyword = input("Secondary keyword: ").strip()
        display_and_open_search_result_with_url(secondary_keyword)

        for platform in social_media_platforms:
            display_and_open_search_result_with_url(f"{secondary_keyword} {platform}")

        display_and_open_search_result_in_text(secondary_keyword)

        for platform in social_media_platforms:
            display_and_open_search_result_in_text(f"{secondary_keyword} {platform}")

    elif has_secondary_keyword == "n" and open_browser_choice == "y":
        open_in_browser(f'"{primary_keyword}"')
        open_in_browser(f'inurl:{primary_keyword}')
        open_in_browser(f'intitle:{primary_keyword}')
        open_in_browser(f'intext:{primary_keyword}')

        for platform in social_media_platforms:
            display_and_open_search_result_with_url(platform)

        for platform in social_media_platforms:
            display_and_open_search_result_in_text(platform)

    else:
        print("Invalid input. Please type 'y' or 'n'.")
        start_google_dorking_search()

    return prompt_for_next_action()

# Function to prompt user for next action: either exit or another search
def prompt_for_next_action():
    action_choice = input("1) Exit  2) Another search: ").strip()

    if action_choice == "2":
        start_google_dorking_search()
    elif action_choice == "1":
        return 0
    else:
        print("Invalid choice. Please type '1' or '2'.")
        prompt_for_next_action()

# Start the program
start_google_dorking_search()
