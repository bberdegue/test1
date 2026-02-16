import asyncio
from playwright.async_api import async_playwright

async def run(link):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Navigate to LinkedIn Job Page
        await page.goto(link)

        # Wait for the jobs to load
        await page.wait_for_selector('.jobs-search-results__list-item')

        # Extract job details
        job_posts = await page.query_selector_all('.jobs-search-results__list-item')
        job_details = []

        for job in job_posts:
            title = await job.query_selector('h3')
            company = await job.query_selector('.job-card-container__company-name')
            location = await job.query_selector('.job-card-container__metadata-item')

            # Get text content
            title_text = await title.inner_text() if title else 'N/A'
            company_text = await company.inner_text() if company else 'N/A'
            location_text = await location.inner_text() if location else 'N/A'

            job_details.append({
                'title': title_text,
                'company': company_text,
                'location': location_text
            })

        # Save job details to file
        with open('job_description.txt', 'w') as f:
            for job in job_details:
                f.write(f"{job['title']} at {job['company']} - {job['location']}\n")

        await browser.close()

if __name__ == '__main__':
    # Example LinkedIn jobs page link
    linked_in_jobs_link = 'https://www.linkedin.com/jobs/search/'  # You should replace this with the desired URL
    asyncio.run(run(linked_in_jobs_link))
