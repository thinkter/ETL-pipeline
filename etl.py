import requests
from bs4 import BeautifulSoup
import json
import sys
def match_data(a):
    url = "https://www.cricbuzz.com/api/html/cricket-scorecard/" + a
    urlb = "https://www.cricbuzz.com/cricket-scores/" + a
    output_filename = "scorecard_" + a + ".json" # Name of the file to save

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10) # Added timeout
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        html_doc = response.text
        print(f"Successfully fetched HTML from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        sys.exit(1) # Exit the script if fetching fails
    except Exception as e:
        print(f"An unexpected error occurred during fetching: {e}")
        sys.exit(1)

    # --- Parse the HTML ---
    try:
        soup = BeautifulSoup(html_doc, 'html.parser')
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        sys.exit(1)


    # --- Helper Function to Extract Innings Data (same as before) ---
    def extract_innings_data(innings_div):
        if not innings_div:
            return None

        innings_data = {}

        # Team Name and Score Summary
        header_div = innings_div.find('div', class_='cb-scrd-hdr-rw')
        if header_div:
            spans = header_div.find_all('span')
            if len(spans) >= 1: # Handle cases where score might be missing initially
                innings_data['team_name'] = spans[0].get_text(strip=True)
            if len(spans) >= 2:
                innings_data['score_summary'] = spans[1].get_text(strip=True)
            else:
                innings_data['score_summary'] = "N/A" # Or some default

        # Batting Data
        batting_table = []
        extras = None
        total = None
        did_not_bat = []
        # Find the container holding batting items, extras, total, dnb
        batting_container = innings_div.find('div', class_='cb-ltst-wgt-hdr') # First instance usually holds batting
        if batting_container:
            # Find all direct children divs that are score items or headers/dividers
            # This is slightly more robust than just finding 'cb-scrd-itms' if structure varies slightly
            potential_items = batting_container.find_all(lambda tag: tag.name == 'div' and 'cb-col' in tag.get('class', []) and 'cb-col-100' in tag.get('class', []), recursive=False)

            for item in potential_items:
                # Check if it's likely a batting row based on the presence of multiple cb-col-8 divs
                is_batter_row = len(item.find_all('div', class_='cb-col-8', recursive=False)) >= 5

                if is_batter_row and item.find('div', class_='cb-col-25') and item.find('div', class_='cb-col-25').find('a', class_='cb-text-link'):
                    cols = item.find_all('div', recursive=False)
                    try:
                        try:
                            # 1. Fetch the HTML content of the page
                            response2 = requests.get(urlb, headers=headers, timeout=10) # Added timeout
                            response2.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

                            # 2. Parse the HTML using BeautifulSoup
                            soup2 = BeautifulSoup(response2.text, 'html.parser')

                            # 3. Find the <a> tag with the specified attribute itemprop="location"
                            #    Using attrs dictionary is a reliable way to find by attribute
                            venue_tag = soup2.find('a', attrs={'itemprop': 'location'})

                            # 4. Check if the tag was found and extract the text
                            if venue_tag:
                                venue_text = venue_tag.get_text(strip=True) # Get text and remove leading/trailing whitespace
                                #print(f"Venue: {venue_text}")
                            else:
                                print("Could not find the venue information with itemprop='location'. The website structure might have changed.")
                                sys.exit(1) # Exit with an error code if not found

                        except requests.exceptions.RequestException as e:
                            print(f"Error fetching the URL: {e}")
                            sys.exit(1) # Exit with an error code on network/HTTP error
                        except Exception as e:
                            print(f"An error occurred during parsing: {e}")
                            sys.exit(1) # Exit with an error code on other error                    
                        
                        batter_info = {
                            'name': cols[0].find('a').get_text(strip=True),
                            'dismissal': cols[1].get_text(strip=True),
                            'R': cols[2].get_text(strip=True),
                            'B': cols[3].get_text(strip=True),
                            '4s': cols[4].get_text(strip=True),
                            '6s': cols[5].get_text(strip=True),
                            'SR': cols[6].get_text(strip=True)
                        }
                        
                        new_data = {
                            'name': cols[0].find('a').get_text(strip=True),
                            'dismissal': cols[1].get_text(strip=True),
                            'R': cols[2].get_text(strip=True),
                            'B': cols[3].get_text(strip=True),
                            '4s': cols[4].get_text(strip=True),
                            '6s': cols[5].get_text(strip=True),
                            'SR': cols[6].get_text(strip=True),
                            'Venue': venue_text
                        }
                        
                        file_path = "data.json"

                        # New dictionary to append
                        #new_data = {"name": "Alice", "age": 25, "city": "New York"}

                        try:
                            # Read existing data
                            with open(file_path, "r+") as file:
                                try:
                                    data = json.load(file)  # Load JSON data into Python object
                                except json.JSONDecodeError:
                                    data = []  # If file is empty or corrupted, initialize as empty list

                                if not isinstance(data, list):
                                    data = [data]  # Ensure data is a list

                                data.append(new_data)  # Append new dictionary

                                file.seek(0)  # Move cursor to the beginning of file
                                json.dump(data, file, indent=4)  # Write updated data
                                file.truncate()  # Remove any extra content after writing

                        except FileNotFoundError:
                            # If file doesn't exist, create it with the new data
                            with open(file_path, "w") as file:
                                json.dump([new_data], file, indent=4)

                        print("Data appended successfully!")

                        batting_table.append(batter_info)
                    except IndexError:
                        print(f"Warning: Skipping malformed batting row: {item.get_text(strip=True)}")
                        continue # Skip this row if it doesn't have expected columns
                else:
                    # Check for Extras/Total/DNB rows by looking for specific text/structure
                    first_col_text_div = item.find(['div', 'span'], class_=lambda c: c and ('cb-col-60' in c.split() or 'cb-col-27' in c.split()))
                    if first_col_text_div:
                        text = first_col_text_div.get_text(strip=True)
                        if "Extras" in text:
                            extras_val_div = item.find('div', class_='cb-col-8')
                            extras_detail_div = item.find('div', class_='cb-col-32')
                            if extras_val_div and extras_detail_div:
                                extras = f"{extras_val_div.get_text(strip=True)} {extras_detail_div.get_text(strip=True)}"
                        elif "Total" in text:
                            total_val_div = item.find('div', class_='cb-col-8')
                            total_detail_div = item.find('div', class_='cb-col-32')
                            if total_val_div and total_detail_div:
                                total = f"{total_val_div.get_text(strip=True)} {total_detail_div.get_text(strip=True)}"
                        elif "Did not Bat" in text or "Yet to Bat" in text:
                            dnb_players_div = item.find('div', class_='cb-col-73')
                            if dnb_players_div:
                                dnb_links = dnb_players_div.find_all('a', class_='cb-text-link')
                                did_not_bat = [a.get_text(strip=True) for a in dnb_links]

        innings_data['batting'] = batting_table
        innings_data['extras'] = extras if extras else "N/A"
        innings_data['total'] = total if total else "N/A"
        innings_data['did_not_bat'] = did_not_bat

        # Fall of Wickets (FOW)
        fow_data = []
        # Search within the specific innings_div for robustness
        fow_header = innings_div.find('div', class_='cb-scrd-sub-hdr', text=lambda t: t and 'Fall of Wickets' in t.strip())
        if fow_header:
            fow_details_div = fow_header.find_next_sibling('div', class_='cb-col-rt')
            if fow_details_div:
                fow_spans = fow_details_div.find_all('span')
                fow_data = [span.get_text(strip=True) for span in fow_spans]
        innings_data['fall_of_wickets'] = fow_data

        # Bowling Data
        bowling_table = []
        # Find all major sections within the innings_div; bowling is usually the second 'cb-ltst-wgt-hdr'
        # Need to be careful as structure might vary slightly (e.g., nested divs)
        bowling_section = None
        all_headers = innings_div.find_all('div', class_='cb-scrd-sub-hdr', recursive=True)
        bowler_header = next((h for h in all_headers if h.find('div', text=lambda t: t and 'Bowler' in t.strip())), None)

        if bowler_header:
            # Find the closest ancestor container that holds the items
            current = bowler_header.find_parent()
            while current and not current.find_all('div', class_='cb-scrd-itms'):
                current = current.find_parent()
            if current:
                bowling_items = current.find_all('div', class_='cb-scrd-itms') # Search within the found container
                for item in bowling_items:
                    cols = item.find_all('div', recursive=False)
                    # Check if it's a bowler row (has a link in the first column and enough columns)
                    if cols and len(cols) >= 8 and cols[0].find('a', class_='cb-text-link'):
                        try:
                            bowler_info = {
                                'name': cols[0].find('a').get_text(strip=True),
                                'O': cols[1].get_text(strip=True),
                                'M': cols[2].get_text(strip=True),
                                'R': cols[3].get_text(strip=True),
                                'W': cols[4].get_text(strip=True),
                                'NB': cols[5].get_text(strip=True),
                                'WD': cols[6].get_text(strip=True),
                                'ECO': cols[7].get_text(strip=True),
                            }
                            bowling_table.append(bowler_info)
                        except IndexError:
                            print(f"Warning: Skipping malformed bowling row: {item.get_text(strip=True)}")
                            continue # Skip this row if it doesn't have expected columns

        innings_data['bowling'] = bowling_table

        # Powerplays (Optional, structure might vary)
        powerplays = []
        # Find the Powerplays header similarly to Bowler header
        pp_header = next((h for h in all_headers if h.find('div', text=lambda t: t and 'Powerplays' in t.strip())), None)
        if pp_header:
            # Powerplay details are usually in a sibling or nearby div
            pp_container = pp_header.find_next_sibling('div', class_='cb-col-rt')
            if not pp_container: # Sometimes it's nested differently
                pp_parent = pp_header.find_parent()
                if pp_parent:
                    pp_container = pp_parent.find('div', class_='cb-col-rt')

            if pp_container:
                # Could be multiple powerplay divs inside
                pp_items = pp_container.find_all('div', recursive=False) # Direct children first
                if not pp_items: # If nested one level deeper
                    inner_container = pp_container.find('div')
                    if inner_container:
                        pp_items = inner_container.find_all('div', recursive=False)

                # Group items in threes if they are flat, or find rows
                if len(pp_items) % 3 == 0 and len(pp_items) > 0: # Simple flat structure heuristic
                    for i in range(0, len(pp_items), 3):
                        powerplays.append({
                            'type': pp_items[i].get_text(strip=True),
                            'overs': pp_items[i+1].get_text(strip=True),
                            'runs': pp_items[i+2].get_text(strip=True)
                        })
                else: # Try finding rows (assuming each PP is a direct child div)
                    for item in pp_container.find_all('div', class_='cb-col-100', recursive=False):
                        cols = item.find_all('div', recursive=False)
                        if len(cols) == 3:
                            powerplays.append({
                                'type': cols[0].get_text(strip=True),
                                'overs': cols[1].get_text(strip=True),
                                'runs': cols[2].get_text(strip=True)
                            })

        innings_data['powerplays'] = powerplays

        return innings_data

    # --- Main Extraction ---
    scorecard_data = {}


    # Match Result
    # Handle potential variations in class names or structure for result
    result_div = soup.find('div', class_=lambda c: c and 'cb-scrcrd-status' in c.split() and 'cb-text-' in c)
    if not result_div: # Fallback selector
        result_div = soup.find('div', class_='cb-text-complete')
    scorecard_data['match_result'] = result_div.get_text(strip=True) if result_div else "Result Not Found"

    # Innings 1
    innings_1_div = soup.find('div', id='innings_1')
    scorecard_data['innings_1'] = extract_innings_data(innings_1_div) if innings_1_div else {"error": "Innings 1 data not found"}

    # Innings 2
    innings_2_div = soup.find('div', id='innings_2')
    scorecard_data['innings_2'] = extract_innings_data(innings_2_div) if innings_2_div else None # Use None if innings 2 hasn't started or doesn't exist

    # Match Info & Squads
    match_info = {}
    squads = {}
    # Find the "Match Info" header more reliably
    match_info_header = soup.find('div', class_='cb-scrd-hdr-rw', text='Match Info')
    if match_info_header:
        # Find the container relative to the header
        info_container = match_info_header.find_parent('div', class_=lambda c: c and 'cb-col-100' in c.split() and not c.split()[-1].startswith('cb-ltst-wgt-hdr')) # Avoid innings containers
        if not info_container: # Try another parent level up if needed
            info_container = match_info_header.find_parent().find_parent()

        if info_container:
            # Basic Info Items
            info_items = info_container.find_all('div', class_='cb-mtch-info-itm')
            for item in info_items:
                label_div = item.find('div', class_='cb-col-27')
                value_div = item.find('div', class_='cb-col-73')
                if label_div and value_div:
                    label = label_div.get_text(strip=True)
                    # Get text but exclude known dynamic span content if needed
                    value = ' '.join(value_div.find_all(string=True, recursive=False)).strip() # Get direct text
                    if not value: # If text is inside spans/links
                        value = value_div.get_text(strip=True)
                    match_info[label] = value

            # Squads - Find all divs related to team info within the container
            all_squad_related_divs = info_container.find_all('div', class_='cb-minfo-tm-nm')
            current_team = None

            for div in all_squad_related_divs:
                # Check if this div contains the 'Squad' text directly or in a child
                squad_text_node = div.find(string=lambda t: 'Squad' in t, recursive=True)
                is_squad_header = squad_text_node is not None

                if is_squad_header:
                    current_team = div.get_text(strip=True).replace(' ', ' ').replace('Squad', '').strip()
                    if current_team: # Ensure we got a team name
                        squads[current_team] = {'Playing': [], 'Bench': []}
                elif current_team: # Only process if we have identified a team
                    label_div = div.find('div', class_='cb-col-27')
                    players_div = div.find('div', class_='cb-col-73')
                    if label_div and players_div:
                        label = label_div.get_text(strip=True)
                        player_links = players_div.find_all('a', class_='margin0')
                        player_names = [a.get_text(strip=True).replace('(c)', '').replace('(wk)', '').strip() for a in player_links]

                        if label == 'Playing' and current_team in squads:
                            squads[current_team]['Playing'] = player_names
                        elif label == 'Bench' and current_team in squads:
                            squads[current_team]['Bench'] = player_names
                        # Could add 'Support Staff' if needed


    scorecard_data['match_info'] = match_info
    scorecard_data['squads'] = squads


    # --- Save the Extracted Data to JSON ---
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            # Use ensure_ascii=False to prevent non-ASCII characters (like player names)
            # from being escaped.
            json.dump(scorecard_data, f, indent=2, ensure_ascii=False)
        print(f"Successfully saved data to {output_filename}")
    except IOError as e:
        print(f"Error writing to file {output_filename}: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred during saving: {e}")
        sys.exit(1)
        
        


if len(sys.argv) > 1:
    argument1 = sys.argv[1]

    if len(sys.argv) > 2:
        argument2 = sys.argv[2]
else:
    print("No arguments provided.")
    
for i in range(int(argument1) , int(argument2) + 1):
    match_data(str(i))