#!/usr/bin/env python3
"""
Script to generate a prep file for downloading Sefer HaMitzvot content from Wikisource.
Based on the URL structure: https://he.wikisource.org/wiki/ספר_המצוות
"""

import urllib.parse
import json
from pathlib import Path

def generate_urls():
    """Generate URLs for all pages in Sefer HaMitzvot structure."""
    
    base_url = "https://he.wikisource.org/wiki"
    main_page = "ספר_המצוות"
    
    # Structure based on the documented content organization
    pages = {
        "main": f"{base_url}/{urllib.parse.quote(main_page)}",
        "content": {
            "peticha": f"{base_url}/{urllib.parse.quote(main_page)}",
            "introduction": f"{base_url}/{urllib.parse.quote(f'{main_page}_הקדמה')}",
            "positive_mitzvot": f"{base_url}/{urllib.parse.quote(f'{main_page}_עשה')}",
            "negative_mitzvot": f"{base_url}/{urllib.parse.quote(f'{main_page}_לא_תעשה')}"
        },
        "sources": f"{base_url}/{urllib.parse.quote(f'{main_page}/מקורות')}",
        "external_links": f"{base_url}/{urllib.parse.quote(f'{main_page}/קישורים_חיצוניים')}"
    }
    
    # Generate roots pages (14 roots: א through יד)
    roots_pages = []
    for i in range(1, 15):
        hebrew_num = number_to_hebrew(i)
        url_path = f"{main_page}_שורש_{hebrew_num}"
        encoded_url = f"{base_url}/{urllib.parse.quote(url_path)}"
        roots_pages.append({
            "number": i,
            "hebrew_number": hebrew_num,
            "url": encoded_url,
            "title": f"שורש {hebrew_num}"
        })
    
    # Generate numbered commandment pages (based on traditional 613 mitzvot)
    positive_mitzvot_pages = []
    negative_mitzvot_pages = []
    
    # Positive commandments (typically 248)
    for i in range(1, 249):
        hebrew_num = number_to_hebrew(i)
        url_path = f"{main_page}_עשה_{hebrew_num}"
        encoded_url = f"{base_url}/{urllib.parse.quote(url_path)}"
        positive_mitzvot_pages.append({
            "number": i,
            "hebrew_number": hebrew_num,
            "url": encoded_url,
            "title": f"מצווה {hebrew_num}"
        })
    
    # Negative commandments (typically 365)
    for i in range(1, 366):
        hebrew_num = number_to_hebrew(i)
        url_path = f"{main_page}_לא_תעשה_{hebrew_num}"
        encoded_url = f"{base_url}/{urllib.parse.quote(url_path)}"
        negative_mitzvot_pages.append({
            "number": i,
            "hebrew_number": hebrew_num,
            "url": encoded_url,
            "title": f"איסור {hebrew_num}"
        })
    
    pages["roots_pages"] = roots_pages
    pages["positive_mitzvot_pages"] = positive_mitzvot_pages
    pages["negative_mitzvot_pages"] = negative_mitzvot_pages
    
    return pages

def number_to_hebrew(num):
    """Convert number to Hebrew representation."""
    hebrew_numbers = {
        1: "א", 2: "ב", 3: "ג", 4: "ד", 5: "ה", 6: "ו", 7: "ז", 8: "ח", 9: "ט", 10: "י",
        11: "יא", 12: "יב", 13: "יג", 14: "יד", 15: "טו", 16: "טז", 17: "יז", 18: "יח", 19: "יט", 20: "כ",
        21: "כא", 22: "כב", 23: "כג", 24: "כד", 25: "כה", 26: "כו", 27: "כז", 28: "כח", 29: "כט", 30: "ל",
        31: "לא", 32: "לב", 33: "לג", 34: "לד", 35: "לה", 36: "לו", 37: "לז", 38: "לח", 39: "לט", 40: "מ",
        41: "מא", 42: "מב", 43: "מג", 44: "מד", 45: "מה", 46: "מו", 47: "מז", 48: "מח", 49: "מט", 50: "נ",
        51: "נא", 52: "נב", 53: "נג", 54: "נד", 55: "נה", 56: "נו", 57: "נז", 58: "נח", 59: "נט", 60: "ס",
        61: "סא", 62: "סב", 63: "סג", 64: "סד", 65: "סה", 66: "סו", 67: "סז", 68: "סח", 69: "סט", 70: "ע",
        71: "עא", 72: "עב", 73: "עג", 74: "עד", 75: "עה", 76: "עו", 77: "עז", 78: "עח", 79: "עט", 80: "פ",
        81: "פא", 82: "פב", 83: "פג", 84: "פד", 85: "פה", 86: "פו", 87: "פז", 88: "פח", 89: "פט", 90: "צ",
        91: "צא", 92: "צב", 93: "צג", 94: "צד", 95: "צה", 96: "צו", 97: "צז", 98: "צח", 99: "צט", 100: "ק"
    }
    
    # Handle numbers 1-100
    if num <= 100:
        return hebrew_numbers.get(num, str(num))
    
    # Handle numbers 101-200 (ק + remainder)
    elif num <= 200:
        remainder = num - 100
        if remainder == 0:
            return "ק"
        else:
            return f"ק{hebrew_numbers.get(remainder, str(remainder))}"
    
    # Handle numbers 201-300 (ר + remainder)
    elif num <= 300:
        remainder = num - 200
        if remainder == 0:
            return "ר"
        else:
            return f"ר{hebrew_numbers.get(remainder, str(remainder))}"
    
    # Handle numbers 301-400 (ש + remainder)
    elif num <= 400:
        remainder = num - 300
        if remainder == 0:
            return "ש"
        else:
            return f"ש{hebrew_numbers.get(remainder, str(remainder))}"
    
    # For numbers beyond 400, just return the number
    else:
        return str(num)

def create_prep_file():
    """Create the prep file with all URLs and metadata."""
    
    pages = generate_urls()
    
    prep_data = {
        "project_name": "Sefer HaMitzvot Download",
        "base_url": "https://he.wikisource.org/wiki",
        "main_page": "ספר_המצוות",
        "total_pages": len(pages["roots_pages"]) + len(pages["positive_mitzvot_pages"]) + len(pages["negative_mitzvot_pages"]) + 7,
        "structure": {
            "description": "Sefer HaMitzvot by Rashi - Complete structure for downloading",
            "main_sections": [
                "פתיחה (Introduction)",
                "הקדמה (Introduction)",
                "שרשים (Roots)",
                "מצוות עשה (Positive Commandments)",
                "מצוות לא תעשה (Negative Commandments)",
                "מקורות (Sources)",
                "קישורים חיצוניים (External Links)"
            ]
        },
        "download_queue": []
    }
    
    # Add main pages
    for section, url in pages["content"].items():
        prep_data["download_queue"].append({
            "type": "main_section",
            "section": section,
            "url": url,
            "filename": f"{section}.html"
        })
    
    # Add roots pages
    for page in pages["roots_pages"]:
        prep_data["download_queue"].append({
            "type": "root",
            "number": page["number"],
            "hebrew_number": page["hebrew_number"],
            "url": page["url"],
            "filename": f"root_{page['number']:02d}_{page['hebrew_number']}.html"
        })
    
    # Add sources and external links
    prep_data["download_queue"].append({
        "type": "reference",
        "section": "sources",
        "url": pages["sources"],
        "filename": "sources.html"
    })
    
    prep_data["download_queue"].append({
        "type": "reference", 
        "section": "external_links",
        "url": pages["external_links"],
        "filename": "external_links.html"
    })
    
    # Add positive mitzvot pages
    for page in pages["positive_mitzvot_pages"]:
        prep_data["download_queue"].append({
            "type": "positive_mitzvah",
            "number": page["number"],
            "hebrew_number": page["hebrew_number"],
            "url": page["url"],
            "filename": f"positive_mitzvah_{page['number']:03d}_{page['hebrew_number']}.html"
        })
    
    # Add negative mitzvot pages
    for page in pages["negative_mitzvot_pages"]:
        prep_data["download_queue"].append({
            "type": "negative_mitzvah",
            "number": page["number"],
            "hebrew_number": page["hebrew_number"],
            "url": page["url"],
            "filename": f"negative_mitzvah_{page['number']:03d}_{page['hebrew_number']}.html"
        })
    
    return prep_data

def save_prep_file(prep_data, filename="sefer_hamitzvot_prep.json"):
    """Save the prep data to a JSON file."""
    
    output_path = Path(filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(prep_data, f, ensure_ascii=False, indent=2)
    
    print(f"Prep file saved to: {output_path}")
    print(f"Total pages to download: {prep_data['total_pages']}")
    print(f"Roots: {len([p for p in prep_data['download_queue'] if p['type'] == 'root'])}")
    print(f"Positive mitzvot: {len([p for p in prep_data['download_queue'] if p['type'] == 'positive_mitzvah'])}")
    print(f"Negative mitzvot: {len([p for p in prep_data['download_queue'] if p['type'] == 'negative_mitzvah'])}")
    print(f"Reference pages: {len([p for p in prep_data['download_queue'] if p['type'] in ['main_section', 'reference']])}")

def main():
    """Main function to generate the prep file."""
    print("Generating Sefer HaMitzvot prep file...")
    
    prep_data = create_prep_file()
    save_prep_file(prep_data)
    
    print("\nPrep file generation complete!")
    print("You can now use this file to download all pages systematically.")

if __name__ == "__main__":
    main() 