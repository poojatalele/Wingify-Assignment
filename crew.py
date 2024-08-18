import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from pdf_to_text import pdf_to_text
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool,
    PDFSearchTool
)

# Load environment variables from .env file
load_dotenv()

# Set up API keys from environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

os.environ["SERPER_API_KEY"] = SERPER_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["OPENAI_MODEL_NAME"] = OPENAI_MODEL_NAME

# Define file paths
pdf_path = r'C:\Users\pooja\Wingify\data\blood_sample_report.pdf'
txt_path = r'C:\Users\pooja\Wingify\data\blood_sample_report.txt'

# Convert the PDF to text for processing
pdf_to_text(pdf_path, txt_path)

# Instantiate tools
docs_tool = DirectoryReadTool(directory=r'C:\Users\pooja\Wingify\data')
file_tool = FileReadTool()
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()
pdf_read_tool = PDFSearchTool()

# Agent 1: Research Manager
research_manager = Agent(
    role='Research Manager',
    goal='Coordinate the analysis, research, and recommendation process',
    backstory='You are a seasoned research manager with expertise in health and wellness, overseeing a team of AI specialists.',
    tools=[file_tool, pdf_read_tool, docs_tool],
    allow_delegation=True,
    verbose=True
)

# Agent 2: Blood Report Analyst
blood_report_analyst = Agent(
    role='Blood Report Analyst',
    goal='Analyze the blood report and extract critical health information',
    backstory='You are an AI specialist with deep knowledge of medical diagnostics and blood chemistry.',
    tools=[file_tool, pdf_read_tool, docs_tool],
    allow_delegation=False,
    verbose=True,
)

# Agent 3: Health Researcher
health_researcher = Agent(
    role='Health Researcher',
    goal='Search for articles related to the findings from the blood report',
    backstory='You are an AI expert in medical research, capable of finding and summarizing relevant information from a wide range of sources.',
    tools=[search_tool, web_rag_tool, docs_tool],
    allow_delegation=False,
    verbose=True,
)

# Agent 4: Health Recommendation Specialist
health_recommendation_specialist = Agent(
    role='Health Recommendation Specialist',
    goal='Generate personalized health recommendations based on the analysis and research',
    backstory='You are an AI expert in health recommendations, with a focus on diet, lifestyle, and preventive care.',
    tools=[file_tool, docs_tool],
    allow_delegation=False,
    verbose=True,
)

# Define tasks for each agent
analyse_report_task = Task(
    description='The Blood Report Analyst will analyze the blood test report provided in the input file. The analysis will focus on summarizing key health indicators and findings from the blood test.',
    expected_output='A summary report of the key points identified in the blood test.',
    agent=blood_report_analyst
)

search_articles_task = Task(
    description='The Health Researcher will search for relevant articles based on the blood report findings.',
    expected_output='A list of relevant articles and their summaries.',
    agent=health_researcher,
    context=[analyse_report_task]
)

generate_recommendations_task = Task(
    description='The Health Recommendation Specialist will provide personalized health recommendations based on the findings of the Blood Report Analyst and related articles.',
    expected_output='Detailed health recommendations with URLs of the articles used as references.',
    agent=health_recommendation_specialist,
    context=[search_articles_task],
    output_file=r'C:\Users\pooja\Wingify\data\recommendations.json'
)

# Assemble the crew
crew = Crew(
    agents=[research_manager, blood_report_analyst, health_researcher, health_recommendation_specialist],
    tasks=[analyse_report_task, search_articles_task, generate_recommendations_task],
    verbose=True,
    process=Process.sequential
)

# Define input
inputs = {
    'text_file': txt_path
}

# Execute tasks
crew.kickoff(inputs=inputs)
