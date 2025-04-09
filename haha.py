'''from bs4 import BeautifulSoup

html_content = """
<div class="cb-col-100 cb-col cb-series-brdr cb-series-matches ng-scope"
            ng-class="{true:'cb-series-brdr'}[filter_set || 1 =='1' ]"
            ng-if="(!filters_set.venue || filters_type.set_venue_id =='Chandigarh') && (!filters_set.team || (filters_type.set_team_id =='65' || filters_type.set_team_id =='61')) && (!filters_set.match || filters_type.set_match_type_id =='t20')">
            <div class="cb-col-25 cb-col pad10 schedule-date ng-isolate-scope" ng-show="!filter_set"><span
                    ng-bind=" 1711188000000| date:'MMM dd, EEE' : '+05:30'" class="ng-binding">Mar 23, Sat</span></div>
            <div class="cb-col-25 cb-col pad10 ng-hide"
                ng-show="filter_set || (filters_type.set_venue_id =='Chandigarh' || filters_type.set_team_id =='65' || filters_type.set_team_id =='61' || filters_type.set_match_type_id =='T20')">
                <span ng-bind=" 1711188000000| date:'MMM dd, EEE' : '+05:30'" class="ng-binding">Mar 23, Sat</span>
            </div>
            <div class="cb-col-75 cb-col">
                <div class="cb-col-60 cb-col cb-srs-mtchs-tm"><a class="text-hvr-underline"
                        href="/cricket-scores/89661/pbks-vs-dc-2nd-match-indian-premier-league-2024"
                        title="PUNJAB KINGS vs DELHI CAPITALS Live Cricket Score and ball by ball commentary"><span>PUNJAB
                            KINGS vs DELHI CAPITALS, 2nd Match</span></a>
                    <div class="text-gray">Maharaja Yadavindra Singh International Cricket Stadium, Mullanpur,
                        Chandigarh</div><a href="/cricket-scores/89661/pbks-vs-dc-2nd-match-indian-premier-league-2024"
                        class="cb-text-complete">Punjab Kings won by 4 wkts</a>
                </div>
                <div class="cb-col-40 cb-col cb-srs-mtchs-tm"><span class="schedule-date ng-isolate-scope"
                        timestamp="1711188000000" format="h:mm a" venue="+05:30">3:30 PM</span>
                    <div class="cb-font-12 text-gray"><span>10:00 AM </span>GMT /<span> 03:30 PM</span> LOCAL</div>
                </div>
            </div>
        </div>
        <!-- end ngIf: (!filters_set.venue || filters_type.set_venue_id =='Chandigarh') && (!filters_set.team || (filters_type.set_team_id =='65' || filters_type.set_team_id =='61')) && (!filters_set.match || filters_type.set_match_type_id =='t20') --><!-- ngIf: (!filters_set.venue || filters_type.set_venue_id =='Kolkata') && (!filters_set.team || (filters_type.set_team_id =='63' || filters_type.set_team_id =='255')) && (!filters_set.match || filters_type.set_match_type_id =='t20') -->
        <div class="cb-col-100 cb-col cb-series-matches ng-scope"
            ng-class="{true:'cb-series-brdr'}[filter_set || 1 =='' ]"
            ng-if="(!filters_set.venue || filters_type.set_venue_id =='Kolkata') && (!filters_set.team || (filters_type.set_team_id =='63' || filters_type.set_team_id =='255')) && (!filters_set.match || filters_type.set_match_type_id =='t20')">
            <div class="cb-col-25 cb-col pad10 schedule-date ng-isolate-scope" ng-show="!filter_set"> </div>
            <div class="cb-col-25 cb-col pad10 ng-hide"
                ng-show="filter_set || (filters_type.set_venue_id =='Kolkata' || filters_type.set_team_id =='63' || filters_type.set_team_id =='255' || filters_type.set_match_type_id =='T20')">
                <span ng-bind=" 1711202400000| date:'MMM dd, EEE' : '+05:30'" class="ng-binding">Mar 23, Sat</span>
            </div>
            <div class="cb-col-75 cb-col">
                <div class="cb-col-60 cb-col cb-srs-mtchs-tm"><a class="text-hvr-underline"
                        href="/cricket-scores/89665/kkr-vs-srh-3rd-match-indian-premier-league-2024"
                        title="KOLKATA KNIGHT RIDERS vs SUNRISERS HYDERABAD Live Cricket Score and ball by ball commentary"><span>KOLKATA
                            KNIGHT RIDERS vs SUNRISERS HYDERABAD, 3rd Match</span></a>
                    <div class="text-gray">Eden Gardens, Kolkata</div><a
                        href="/cricket-scores/89665/kkr-vs-srh-3rd-match-indian-premier-league-2024"
                        class="cb-text-complete">Kolkata Knight Riders won by 4 runs</a>
                </div>
                <div class="cb-col-40 cb-col cb-srs-mtchs-tm"><span class="schedule-date ng-isolate-scope"
                        timestamp="1711202400000" format="h:mm a" venue="+05:30">7:30 PM</span>
                    <div class="cb-font-12 text-gray"><span>02:00 PM </span>GMT /<span> 07:30 PM</span> LOCAL</div>
                </div>
            </div>
        </div>
        <!-- end ngIf: (!filters_set.venue || filters_type.set_venue_id =='Kolkata') && (!filters_set.team || (filters_type.set_team_id =='63' || filters_type.set_team_id =='255')) && (!filters_set.match || filters_type.set_match_type_id =='t20') --><!-- ngIf: (!filters_set.venue || filters_type.set_venue_id =='Jaipur') && (!filters_set.team || (filters_type.set_team_id =='64' || filters_type.set_team_id =='966')) && (!filters_set.match || filters_type.set_match_type_id =='t20') -->
        <div class="cb-col-100 cb-col cb-series-brdr cb-series-matches ng-scope"
            ng-class="{true:'cb-series-brdr'}[filter_set || 1 =='1' ]"
            ng-if="(!filters_set.venue || filters_type.set_venue_id =='Jaipur') && (!filters_set.team || (filters_type.set_team_id =='64' || filters_type.set_team_id =='966')) && (!filters_set.match || filters_type.set_match_type_id =='t20')">
            <div class="cb-col-25 cb-col pad10 schedule-date ng-isolate-scope" ng-show="!filter_set"><span
                    ng-bind=" 1711274400000| date:'MMM dd, EEE' : '+05:30'" class="ng-binding">Mar 24, Sun</span></div>
            <div class="cb-col-25 cb-col pad10 ng-hide"
                ng-show="filter_set || (filters_type.set_venue_id =='Jaipur' || filters_type.set_team_id =='64' || filters_type.set_team_id =='966' || filters_type.set_match_type_id =='T20')">
                <span ng-bind=" 1711274400000| date:'MMM dd, EEE' : '+05:30'" class="ng-binding">Mar 24, Sun</span>
            </div>
            <div class="cb-col-75 cb-col">
                <div class="cb-col-60 cb-col cb-srs-mtchs-tm"><a class="text-hvr-underline"
                        href="/cricket-scores/89668/rr-vs-lsg-4th-match-indian-premier-league-2024"
                        title="RAJASTHAN ROYALS vs LUCKNOW SUPER GIANTS Live Cricket Score and ball by ball commentary"><span>RAJASTHAN
                            ROYALS vs LUCKNOW SUPER GIANTS, 4th Match</span></a>
                    <div class="text-gray">Sawai Mansingh Stadium, Jaipur</div><a
                        href="/cricket-scores/89668/rr-vs-lsg-4th-match-indian-premier-league-2024"
                        class="cb-text-complete">Rajasthan Royals won by 20 runs</a>
                </div>
                <div class="cb-col-40 cb-col cb-srs-mtchs-tm"><span class="schedule-date ng-isolate-scope"
                        timestamp="1711274400000" format="h:mm a" venue="+05:30">3:30 PM</span>
                    <div class="cb-font-12 text-gray"><span>10:00 AM </span>GMT /<span> 03:30 PM</span> LOCAL</div>
                </div>
            </div>
        </div>
"""

# Base URL of the website (replace if different)
base_url = "https://www.cricbuzz.com" # Example

# Initialize a list to hold data for all matches
all_match_data = []

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the main divs containing match information
match_divs = soup.find_all('div', class_='cb-series-matches')

# Loop through each match div found
for match_div in match_divs:
    date = "Date not found"
    relative_url = "URL not found"
    full_url = "URL not found"
    time = "Time not found"

    # --- Extract Date ---
    # Find the second 'cb-col-25' div, which seems to reliably contain the date span
    date_containers = match_div.find_all('div', class_='cb-col-25', limit=2)
    if len(date_containers) > 0:
        # Try the first one first, if it's not just whitespace ( )
        date_span_first = date_containers[0].find('span', class_='ng-binding')
        if date_span_first and date_span_first.get_text(strip=True):
             date = date_span_first.get_text(strip=True)
        # Otherwise, try the second one if it exists
        elif len(date_containers) > 1:
            date_span_second = date_containers[1].find('span', class_='ng-binding')
            if date_span_second:
                date = date_span_second.get_text(strip=True)

    # --- Extract URL ---
    link_container = match_div.find('div', class_='cb-col-60 cb-col cb-srs-mtchs-tm')
    if link_container:
        url_tag = link_container.find('a', class_='text-hvr-underline')
        if url_tag and url_tag.has_attr('href'):
            relative_url = url_tag['href']
            full_url = base_url + relative_url # Construct the full URL

    # --- Extract Time ---
    time_container = match_div.find('div', class_='cb-col-40 cb-col cb-srs-mtchs-tm')
    if time_container:
        time_span = time_container.find('span', class_='schedule-date')
        if time_span:
            time = time_span.get_text(strip=True)

    # Append the extracted data (using full_url now) as a list to the main list
    match_data = [date, full_url, time]
    all_match_data.append(match_data)

# Print the final list of lists


for i in all_match_data:
    print(i)
    
    '''
    
import requests
from bs4 import BeautifulSoup
import pprint
import time
try:
    from urllib.parse import urlparse
except ImportError:
    print("Warning: urllib.parse not found. URL parsing might be less robust.")
    urlparse = None # Define it as None if not available

# --- Configuration ---
# MAKE SURE THIS IS THE CORRECT URL for the schedule page
target_url = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/matches" # Example URL - CHANGE IF NEEDED

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# --- Base URL Determination ---
base_url = ""
if urlparse:
    try:
        parsed_uri = urlparse(target_url)
        base_url = f"{parsed_uri.scheme}://{parsed_uri.netloc}"
    except Exception as e:
        print(f"Warning: Could not parse URL to determine base_url: {e}")
else:
    # Basic fallback if urlparse isn't available
    if target_url.startswith("https://"):
         base_url = "https://" + target_url.split('/')[2]
    elif target_url.startswith("http://"):
         base_url = "http://" + target_url.split('/')[2]

if not base_url:
     # Final fallback - set manually if needed
     base_url = "https://www.cricbuzz.com"
     print(f"Warning: Could not determine base_url automatically. Using default: '{base_url}'")

print(f"Using Base URL: {base_url}")


def scrape_cricbuzz_schedule(url):
    """
    Fetches and scrapes match schedule data from a given URL.

    Args:
        url (str): The URL of the Cricbuzz schedule page.

    Returns:
        list: A list of lists, where each inner list contains
              [date (str), full_match_url (str), time (str)].
              Returns an empty list if fetching or parsing fails,
              or if no matches are found.
    """
    all_match_data = []
    try:
        print(f"Fetching URL: {url}...")
        response = requests.get(url, headers=headers, timeout=20) # Increased timeout slightly
        response.raise_for_status()
        print("Fetch successful.")

        # --- Optional: Save raw HTML for inspection ---
        # with open("cricbuzz_raw_debug.html", "w", encoding="utf-8") as f:
        #     f.write(response.text)
        # print("Saved raw HTML to cricbuzz_raw_debug.html for inspection.")
        # ---

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the main divs containing match information
        # Ensure this class selector is still correct by viewing page source
        match_divs = soup.find_all('div', class_='cb-series-matches')
        print(f"Found {len(match_divs)} potential match entries using class 'cb-series-matches'.")

        if not match_divs:
            print("\n*** WARNING: No match entries found ***")
            print("Check the 'cb-series-matches' class in the page source (Ctrl+U).")
            print("If the data loads via JavaScript, this script won't work. Consider Selenium/Playwright.")
            return []

        match_count = 0
        for i, match_div in enumerate(match_divs):
            match_count += 1
            # print(f"\n--- Processing Match Div {i+1} ---") # Uncomment for detailed debug
            # print(match_div.prettify()) # Uncomment to print the specific div being processed

            date = "Date not found"
            relative_url = "URL not found"
            full_url = "URL not found"
            time = "Time not found"

            # --- Extract Date (Revised Logic) ---
            # Look for any span with 'ng-binding' inside the match_div that contains date-like text.
            # Prioritize spans within the elements expected to hold the date.
            possible_date_parents = match_div.find_all('div', class_='cb-col-25', limit=2)
            found_date = False
            for parent in possible_date_parents:
                date_span = parent.find('span', class_='ng-binding')
                if date_span:
                    date_text = date_span.get_text(strip=True)
                    # Basic check if it looks like a date (contains comma or month abbreviation)
                    if date_text and (',' in date_text or any(m in date_text for m in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])):
                        date = date_text
                        found_date = True
                        # print(f"DEBUG Date Found: {date}") # Uncomment for debug
                        break # Found date in one of the expected parents

            # Fallback: Search more broadly if not found in expected parents
            if not found_date:
                 all_binding_spans = match_div.find_all('span', class_='ng-binding')
                 for span in all_binding_spans:
                     date_text = span.get_text(strip=True)
                     if date_text and (',' in date_text or any(m in date_text for m in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])):
                          date = date_text
                          # print(f"DEBUG Date Found (Fallback): {date}") # Uncomment for debug
                          break

            # --- Extract URL ---
            link_container = match_div.find('div', class_='cb-col-60 cb-col cb-srs-mtchs-tm')
            if link_container:
                url_tag = link_container.find('a', class_='text-hvr-underline')
                if url_tag and url_tag.has_attr('href'):
                    relative_url = url_tag['href']
                    if base_url and relative_url.startswith('/'):
                        full_url = base_url + relative_url
                    elif relative_url.startswith('http'):
                         full_url = relative_url
                    else:
                         full_url = relative_url # Keep as is if format unclear
                    # print(f"DEBUG URL Found: {full_url}") # Uncomment for debug


            # --- Extract Time (Revised Logic) ---
            # Look specifically for the span with class 'schedule-date' within the time container
            time_container = match_div.find('div', class_='cb-col-40 cb-col cb-srs-mtchs-tm')
            if time_container:
                time_span = time_container.find('span', class_='schedule-date')
                if time_span:
                    time_text = time_span.get_text(strip=True)
                    if time_text: # Ensure it's not empty
                        time = time_text
                        # print(f"DEBUG Time Found: {time}") # Uncomment for debug
                    # else:
                        # print("DEBUG: Found time span but text is empty.") # Uncomment for debug
                # else:
                    # print("DEBUG: Could not find span with class 'schedule-date' in time container.") # Uncomment for debug
            # else:
                 # print("DEBUG: Could not find div with class 'cb-col-40 cb-col cb-srs-mtchs-tm'.") # Uncomment for debug


            # Append the extracted data
            match_data = [date, full_url, time]
            all_match_data.append(match_data)

            # --- Add a small delay to be polite to the server ---
            # time.sleep(0.1) # Uncomment if scraping many pages/entries

    except requests.exceptions.Timeout:
        print(f"Error: Request timed out while fetching {url}")
    except requests.exceptions.HTTPError as http_err:
        print(f"Error: HTTP error occurred: {http_err} (Status code: {response.status_code})")
        print("Check if the URL is correct and accessible.")
    except requests.exceptions.RequestException as req_err:
        print(f"Error: Could not fetch URL {url}. Error: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred during scraping: {e}")
        import traceback
        traceback.print_exc() # Print detailed error traceback

    return all_match_data

# --- Main Execution ---
if __name__ == "__main__":
    scraped_data = scrape_cricbuzz_schedule(target_url)

    if scraped_data:
        print("\n--- Scraped Data ---")
        pprint.pprint(scraped_data)
        print(f"\nSuccessfully processed {len(scraped_data)} match entries.")

        # Check how many entries actually got a date/time
        dates_found = sum(1 for entry in scraped_data if entry[0] != "Date not found")
        times_found = sum(1 for entry in scraped_data if entry[2] != "Time not found")
        print(f"Dates successfully extracted: {dates_found}/{len(scraped_data)}")
        print(f"Times successfully extracted: {times_found}/{len(scraped_data)}")

        if dates_found < len(scraped_data) or times_found < len(scraped_data):
             print("\n*** WARNING: Some dates or times were not found. ***")
             print("This likely means the data is loaded by JavaScript after the page loads.")
             print("The initial HTML fetched by 'requests' may not contain this information.")
             print("Consider using Selenium or Playwright, or check the Network tab in browser DevTools for API calls.")

    else:
        print("\nNo data was scraped. Please double-check the target URL and review previous warnings.")  