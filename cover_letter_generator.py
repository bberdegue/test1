import os

# Function to read job description and resume

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to generate a customized cover letter

def generate_cover_letter(job_description, resume):
    # Customize these paragraphs based on job_description and resume
    intro = f"Dear Hiring Manager,\n\nI am writing to express my interest in the position advertised. "
    skills = "I believe my skills align well with the requirements listed in the job description, especially in areas such as [specific skills]."
    conclusion = f"\n\nI am eager to bring my background in [related experience] to your team and contribute to [company's goals]. Thank you for considering my application."  

    return f"{intro}\n{skills}\n{conclusion}"  

# File paths
job_description_path = 'job_description.txt'
resume_path = 'original_resume.txt'
output_path = 'cover_letter.txt'

# Read job description and resume
job_description = read_file(job_description_path)
resume = read_file(resume_path)

# Generate cover letter
cover_letter = generate_cover_letter(job_description, resume)

# Write cover letter to file
with open(output_path, 'w') as output_file:
    output_file.write(cover_letter)