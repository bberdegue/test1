import scrape_and_customize
import resume_customizer
import cover_letter_generator
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python main.py <LinkedIn URL>")
        sys.exit(1)
    linkedin_url = sys.argv[1]
    
    # Call the functions from respective modules
    scrape_and_customize.scrape(linkedin_url)
    resume_customizer.customize(linkedin_url)
    cover_letter_generator.generate(linkedin_url)
