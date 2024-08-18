# Blood Report Analysis with CrewAI

This project uses the CrewAI framework to analyze blood test reports and provide personalized health recommendations based on the analysis and relevant internet articles. It integrates various tools for reading files, searching the web, and processing data to deliver actionable insights.

## Approach

### Setting Up the Environment:
- The environment was correctly configured by setting up the necessary environment variables for the API keys, ensuring seamless access to external tools and services required for the task.

### Defining and Initializing Tools:
- Necessary tools were identified and initialized, including tools for reading PDFs and text files, as well as web resources for medical information.
- The SerperDevTool was integrated to enable the agent to perform internet searches for relevant information.

### Creating the Agents:
1. **Research Manager**: Coordinates the entire process, ensuring smooth operation among the other agents.
2. **Blood Report Analyst**: Analyzes the blood test report and summarizes key health indicators and findings.
3. **Health Researcher**: Searches the internet for articles related to the findings from the blood report.
4. **Health Recommendation Specialist**: Generates personalized health recommendations based on the analysis and research.

### Defining Tasks and Crew:
- Detailed task descriptions were created for each agent. The crew was assembled and configured to execute tasks sequentially.

### Executing the Task:
- The process was initiated, with each agent using its defined role, goals, and tools to analyze the blood test report, search for relevant articles, and provide personalized health recommendations.

## Setup

### Prerequisites
- **Python**: Version 3.6 or higher
- **Required Python packages**: 
  - `crewai`
  - `crewai_tools`
  - `pyPDF2`
  - `openai`

### API Key Configuration

Replace the API keys in the .env file with your actual API keys for Serper and OpenAI.

```python
os.environ["SERPER_API_KEY"] = "your-serper-api-key"
os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"
```

This is the reccomendations.json provided.
```
Based on the findings from the blood sample report, it is evident that the individual, a male in his 30s, has undergone various tests including a lipid screen. The lipid screen results indicate the following:
- Total Cholesterol: 105 mg/dL (normal range <200 mg/dL)
- Triglycerides: 130 mg/dL (normal range <150 mg/dL)
- HDL Cholesterol: 46 mg/dL (normal range >40 mg/dL)
- LDL Cholesterol: 33 mg/dL (normal range <100 mg/dL)
- VLDL Cholesterol: 26 mg/dL (normal range <30 mg/dL)
- Non-HDL Cholesterol: 59 mg/dL (normal range <130 mg/dL)

These results are crucial indicators of cardiovascular health. The individual is advised to focus on maintaining a healthy lipid profile by following these recommendations:
1. Ensure a balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats.
2. Limit intake of saturated fats, trans fats, and cholesterol.
3. Engage in regular physical activity to help manage weight and improve lipid levels.
4. Quit smoking and limit alcohol consumption.
5. Monitor blood pressure and blood sugar levels regularly.
6. Consider additional tests or consultations as recommended by healthcare providers for further evaluation and management.

For more information on lipid screen results and cardiovascular health, refer to the Lipid Association of India's guidelines and recommendations at [https://www.lipidindia.org/].

It is essential to consult a healthcare professional for personalized advice and treatment based on individual health status and risk factors.
```
