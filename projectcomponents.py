projects = {    
                "project1": {
                    "title": "Automated Content Summarizer in Databricks",
                    "tools_used": ["Python", "Databricks"],
                    "additional_skills": ["Artificial Intelligence", "Job automation"],
                    "icon": "📝",
                    "link": "pages/ContentSummarizerDatabricks.py",
                    "main_image": "assets/databricks0.png",
                    "description": """
                    This is an AI-driven content summarization pipeline in Databricks that transforms YouTube videos into readable insights. 
                    The system extracts audio, transcribes it into text, and uses an AI model to generate summaries. 
                    Everything runs through Databricks notebooks and is orchestrated using Jobs to automate the entire process.
                    A key feature is that every part of the pipeline is on cloud, including the AI model, which is hosted on Databricks.
                    """,
                    "resources": """
                    - Link to notebooks used: https://github.com/JYNgithub/Automated-Content-Summarizer-Databricks
                    """,
                    "add_image1": "assets/databricks3.png",
                    "add_image2": "assets/databricks1.png",
                    "add_image3": "assets/databricks2.png",
                    "add_image4": "assets/databricks5.png",
                    "documentation": """
                    **1) Extract Youtube Audio**\n
                    The script first extracts a YouTube video's audio using yt-dlp. It uses a cookies.txt file for authentication, which is required when running in a cloud environment.
                    The best available audio stream is extracted and saved in .m4a format. 
                    
                    **2) Transcribe Audio to Text**\n
                    The downloaded audio is then converted to a .wav file using ffmpeg to match the input requirements of the Whisper transcription model. This ensures consistent sample rate and format for accurate speech recognition.
                    The Whisper model (base version) is used to transcribe the WAV audio file into text. A custom audio loading function replaces Whisper's default loader to improve compatibility with ffmpeg and ensure reliable decoding.

                    **3) Content Summarization using AI**\n
                    The transcribed text is sent to an AI model hosted on Databricks using the OpenAI client interface. The model receives a prompt asking for a summary that includes explanation and key points.
                    """
                },
                "project2": {
                    "title": "Automated Pipeline To Databricks Workspaces",
                    "tools_used": ["Python", "Databricks"],
                    "additional_skills": ["Prefect", "Data pipeline automation", "Cloud computing"],
                    "icon": "🖇️",
                    "link": "pages/AutomatedPipelineToDatabricksWorkSpace.py",
                    "main_image": "assets/databrickworkspace0.png",
                    "description": """
                    This is a fully cloud-based pipeline using **Prefect Cloud** to automate data pipelines to **Databricks** workspaces without any manual input. 
                    The project can be scaled to migrate large volumes of files into **Databricks** workspaces for development. 
                    \n
                    Note: A simple audio file is used as an example of source data, due to the fact that I am running the Free/Hobby Edition for both tools with clear limitations.
                    """,
                    "resources": """
                    - Link to GitHub: https://github.com/JYNgithub/Automated-Pipeline-To-DataBricks
                    """,
                    "add_image1": "assets/databrickworkspace1.png",
                    "add_image2": "assets/databrickworkspace2.png",
                    "add_image3": "assets/databrickworkspace3.png",
                    "documentation": """
                    **1) Setting up Prefect Cloud**\n
                    **Prefect Cloud** is a cloud-based workflow management system that allows users to build, run and monitor automated data pipelines. Python scripts
                    are used to set up the tasks and flows needed for the pipeline. Furthermore, a work pool is constructed using a **prefect.yaml** file to enable full automation on cloud. **Prefect** provides
                    developers the ability to seperate code storage and execution, providing both flexibility and security. In this case, the project uses **Prefect** managed servers to run
                    the pipeline.
                    
                    **2) GitHub Repository as Remote Code Storage**\n
                    Since **Prefect** does not store the code for the pipeline, a remote code storage is needed to run the pipeline on cloud. The project chooses GitHub repository 
                    as the most straightforward option. Note that the repository can either be public, or private for security purposes. This option can change according to the needs of the organization.
                    
                    **3) Setting up Databricks Workspaces**\n
                    **Databricks** contains **Workspaces** which are essentially a cloud-based file system that allows users to store and manage files, notebooks, and other resources.
                    For confidential information such as the **Databricks Token**, the project stores it in a local .env file. But for production use, it is recommended to store the token in **Prefect Secrets** system.
                    """
                },
                "project3": {
                    "title": "iBilik.my Web Scraper",
                    "tools_used": ["Python"],
                    "additional_skills": ["ScrapeGraphAI", "Large Language Models (LLM)", "Artificial Intelligence"],
                    "icon": "🕸️",
                    "link": "pages/IBilikmyWebScraper.py",
                    "main_image": "assets/iws1.jpg",
                    "description": """
                    This is a web scraper for extracting data on rooms for rent from [iBilik.my](https://www.ibilik.my/) using 
                    ScrapeGraphAI which integrates Large Language Models (LLMs) and direct graph logic to 
                    create AI-powered scraping pipelines. The easiest way to try it out is to follow the steps in the GitHub repository below.
                    """,
                    "resources": """
                    - Link to GitHub: https://github.com/JYNgithub/IBilik-WebScraper-using-Scrapegraphai
                    - 1-Minute Demo: https://www.youtube.com/watch?v=TOv1kbwljIg
                    - 100 Rows of Scraped Data on Rooms for Rent in Cyberjaya, Selangor (as of 12 July 2024): https://github.com/JYNgithub/IBilik-WebScraper-using-Scrapegraphai/blob/main/example_scraped_data.csv
                    - Link to ScrapeGraphAI GitHub: https://github.com/ScrapeGraphAI/Scrapegraph-ai
                    """,
                    "add_image1": "assets/iws2.jpg",
                    "add_image2": "assets/iws3.jpg",
                    "add_image3": "assets/iws4.png",
                    "documentation": """
                    1) Data Source\n
                    All data scraped from [iBilik.my](https://www.ibilik.my/) are legal and 
                    open to public. No user info has been extracted or utilized. The data is 
                    only used for personal and educational purposes.
                    2) Explaination\n
                    Using ScrapeGraphAI, web scraping is now as easy as providing simple prompts for LLMs to 
                    scrape any data from the web, even for those unfamiliar with web development.\n
                    First, the location of rental rooms to be scraped is identified. The will lead to multiple pages of results, 
                    with each page having a certain number of rooms. There are mandatory requirements for the web scraper to function 
                    properly, which includes an API key, name of LLM model, number of pages and rooms to be scraped and the prompts to
                    be executed.\n
                    Next, upon running the web scraper, the URL of rooms in each page will be obtained. By accessing each URL, it can
                    obtain precise data on each room by scraping the required data as prompted.\n
                    The scraping pipeline will produce a csv file that contains all the scraped data in a readable format. \n
                    3) Additional Notes\n
                    Having learnt the fundamentals of web scraping using Beautiful Soup, I was excited to learn about ScrapeGraphAI.
                    It was widely discussed a few months ago before I started this project, and I immediately knew I had to give it a try.
                    Web scraping just by providing simple prompts is now a reality, the issue is to identify a high-end LLM model that is 
                    both cost-effective and can scale for enterprise use. Of course, legal issues surrounding web scraping must also
                    be respected.
                    """
                },
                "project4": {
                    "title": "Hospital KPI Dashboard For Executives",
                    "tools_used": ["Power BI", "Python"],
                    "additional_skills": ["Power Query"],
                    "icon": "📊",
                    "link": "pages/HospitalKPIDashboard.py",
                    "main_image": "assets/hkpid1.jpg",
                    "description": """
                    This is a top level KPI Dashboard for Maven Hospital to give stakeholders 
                    visibility into the hospital’s recent performance. This is a submission for the 
                    [Maven Hospital Challenge](https://mavenanalytics.io/challenges/maven-hospital-challenge/facee4d2-8369-4c87-a55e-e6c7ed2a42d8)
                    by Maven Analytics.
                    """,
                    "resources": """
                    - Link to Dashboard: [Click here](https://app.powerbi.com/view?r=eyJrIjoiNDllZTRjMDQtOWZhOC00MmZjLWJkMzYtYzVkNDAxNGM2ODhhIiwidCI6IjdmMDQ4ZmMxLTJlYTMtNDhlNC1hYzkyLTkxZDFlYjA5ODA3YyIsImMiOjEwfQ%3D%3D)
                    """,
                    "add_image1": "assets/hkpid2.jpg",
                    "add_image2": "assets/hkpid3.jpg",
                    "add_image3": "assets/hkpid4.jpg",
                    "documentation": """
                    1) Data Cleaning\n
                    Data exploration and cleaning are conducted in Python using Pandas. A mastery of Pandas to clean the dataset has been
                    crucial for building this project. Techniques such as modifying string values, splitting date/time values, mapping 
                    of values for better clarity, conversion of state codes to state names were utilized.\n
                    2) Data Modelling and Visualization\n
                    Data modelling and transformation of the data are all conducted in PowerBI and Power Query. The fundamentals of Power 
                    Query using various formulas were required.\n
                    Lastly, the dashboard in built using Power BI with page navigation and user interactivity.\n
                    3) Insights\n
                    As required by the challenge, several questions were able to be solved using this dashboard:\n
                        1) How many patients have been admitted or readmitted over time?\n
                        A total of 103 patients have been admitted and readmitted in 2022, 
                        indicating that every patient had to make an appointment more than once to visit the hospital. 
                        In 2021, a total of 649 patients are admitted and among them, 636 have been readmitted.\n
                        2) How long are patients staying in the hospital, on average?\n
                        On average, patients have to spend about 1.16 hours in the hospital in 2022.\n
                        3) How much is the average cost per visit?\n
                        The average cost per visit for our hospital is about $3.14k per patient in 2022.\n
                        4) How many procedures are covered by insurance?\n
                        A majority of them are covered by insurance. Out of 268 procedures in 2022, 
                        169 have been covered by insurance fully or partially.\n
                        5) Who are the major demographic group?\n
                        Most patients are elderly from later generations, white females that are covered by insurance.\n
                        6) Which insurance has covered the highest cost?\n
                        Medicare. In 2022, they have covered a sum of about $187000k for our patients. \n
                    4) Additional Notes\n
                    This was a good opportunity for me to learn Power Query. It was a productive experience being able to utilize Power
                    Query and it has become another alternative tool for my future projects whenever data cleaning or transformation is required.
                    """
                },
                "project5": {
                    "title": "Global Data Science and ML Salary Dashboard",
                    "tools_used": ["Python"],
                    "additional_skills": ["Plotly Dash"],
                    "icon": "📊",
                    "link": "pages/GlobalDSandMLDashboard.py",
                    "main_image": "assets/dsml1.png",
                    "description": """
                    This dashboard is built using Dash with visualizations constructed using Plotly. It aims 
                    to a comprehensive view on the salary trends of the most popular job titles in the data science and
                    machine learning industry. Each visualization provides useful information by looking into various aspects 
                    that is related to the distribution of salary such as experience level, company size and year. 
                    """,
                    "resources": """
                    - As of August 2025, the dashboard is only available via local deployment and is no longer accessible online. This is to redirect my focus on newer projects instead. \n
                    - Link to GitHub: https://github.com/JYNgithub/global-salary-dashboard
                    """,
                    "add_image1": "assets/dsml2.png",
                    "add_image2": "assets/dsml3.png",
                    "add_image3": "assets/dsml4.png",
                    "documentation": """
                    1) Data Source\n
                    Data is sourced from [ai-jobs.net](https://ai-jobs.net/salaries/). This dataset is published in the public domain under CC0.\n
                    It is free to copy, modify, and distribute, even for commercial purposes without asking permission.\n
                    
                    2) Data Wrangling\n
                    Using pandas in Python, basic data exploration is conducted by identifying the shape of the dataset, missing values,
                    frequency of each job title.\n
                    Then, the data is filtered to the selected job titles, which are Data Scientist, Data Engineer, Data Analyst, 
                    Machine Learning Engineer, AI Engineer and Business Intelligence Analyst. Columns and certain values are renamed for 
                    better clarity. Moreover, the data is enriched by adding a country name column according to the company location
                    to build a map.\n
                    For further details, please enter the ['About'](https://global-salary-dashboard.onrender.com/about) section of the dashboard to download the complete wrangling zip file. 
                    
                    3) Exploratory Data Analysis\n
                    EDA is mainly conducted using visualizations to identify the most suitable visualization to represent the data. 
                    The visualizations are built using the Plotly Graph Objects library as it provides high customizability and
                    also allows user interaction.
                    
                    4) Dashboard\n
                    The dashboard is built using Dash by Plotly, along with its other components such as Dash Bootstrap Components to
                    customize the dashboard for a more engaging look. It is published using [Render](https://render.com/).
                    
                    5) Additional Notes\n
                    This is my first project using Dash after self-learning and admittedly, there is still much room for improvement. I
                    came to learn how complex Dash can be compared to Streamlit in building web apps, even though Dash offers more options
                    for customization. The learning curve can be quite steep at first to find a good look for the web app but 
                    building interactive visualizations using Plotly is definitely a fun and valuable learning experience.
                    For more information, please check out the dashboard!
                    """
                },
                "project6": {
                    "title": "Interactive Sales Dashboard For Managers",
                    "tools_used": ["Tableau", "Excel", "SQL"],
                    "additional_skills": ["-"],
                    "icon": "📊",
                    "link": "pages/InteractiveSalesDashboard.py",
                    "main_image": "assets/salesd1.jpg",
                    "description": """
                    This is an interactive dashboard that enables sales managers to track their team's quarterly performance. This is a submission for the 
                    [Maven Sales Challenge](https://mavenanalytics.io/challenges/maven-sales-challenge/8f59bcfa-d310-4947-b3d8-917b3cce270e)
                    by Maven Analytics. The data contains B2B sales opportunities from a CRM database for a fictitious company 
                    that sells computer hardware, including information on accounts, products, sales teams, and sales opportunities.  
                    """,
                    "resources": """
                    Link to Dashboard: [Click here](https://public.tableau.com/views/MavenSalesChallenge2024/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
                    """,
                    "add_image1": "assets/salesd2.jpg",
                    "add_image2": "assets/salesd3.jpg",
                    "add_image3": "   ",
                    "documentation": """
                    1) Data Cleaning\n
                    The data is cleaned using Microsoft Excel. Missing values are in the dataset are first handled by replacing the
                    empty cells as 'NA'. Invalid data caused by spelling mistakes are also identified and cleaned.\n
                    2) Data Preperation\n
                    The datasets are stored and merged using PostgreSQL. An entity relationship diagram is shown above to display the 
                    relationships between each tables/relations.\n
                    3) Data Visualization\n
                    The dashboard is constructed using Tableau.
                    """
                },
                "project7": {
                    "title": "Data Engineer Jobs Analysis",
                    "tools_used": ["SQL"],
                    "additional_skills": ["PostgreSQL", "SQLTools (extension)", "Plotly"],
                    "icon": "📈",
                    "link": "pages/SQLLukeBarousse.py",
                    "main_image": "assets/sqllb0.png",
                    "description": """
                    The project aims to provide insights into the data engineering job market using data visualizations.
                    The project showcases intermediate skills in SQL and Python, using PostgreSQL as the database and VS Code with SQLTools extension for database management.
                    Partially guided by [Luke Barousse's SQL for Data Analytics](https://youtu.be/7mz73uXD9DA?si=xRTipzSlpzKb3has), the project is mostly my own work. 
                    """,
                    "resources": """
                    Link to GitHub: https://github.com/JYNgithub/Project-SQL-LukeBarousse
                    """,
                    "add_image1": "assets/sqllb1.png",
                    "add_image2": "assets/sqllb2.png",
                    "add_image3": "assets/sqllb3.png",
                    "add_image4": "assets/sqllb4.png",
                    "documentation": """

                    **Workflow**\n
                    The entire workflow is executed in VS code using the 'SQLTools' extension to connect to PostgreSQL.
                    1. The database and tables are first created using SQL in the 'sql_load' folder.
                    2. The database from PostgreSQL is connected to VS Code using the SQLTools extension.
                    3. The data is queried using SQL in the 'sql_queries' folder for concise data for analysis and visualizations.
                    4. Queried data are converted to CSV files temporarily stored in 'queried_csv' folder.
                    5. The data is visualized using the Python library Plotly in the 'visualizations' folder.

                    **Findings**\n
                    1. What is the typical hourly pay rate for a Data Engineer?\n
                    A majority of Data Engineer roles pay for 52.5 - 57.5 USD per hour, followed by 57.5 - 62.5 and 62.5 - 67.5. 
                    This is much higher than the average hourly pay in the US of 28.2 - 35.5 USD according to news sources.
                    
                    2. What are the top-paying jobs available for Data Engineers?\n
                    Top paying jobs for Data Engineer roles can reach up to 117.50 USD per hour. Furthermore, half of the top paying jobs for Data Engineer roles does not specify requiring a degree in their job postings.
                    
                    3. What are the top skill types based on salary for Data Engineers?\n
                    To nobody's surprise, SQL and Python remain the most demanded skills among Data Engineer roles, which are fundamentals for building data pipelines and ensuring data integrity in any organization. Modern platforms with database services such as AWS and Azure should also be noted.
                    
                    4. What are the most high-demand AND high-paying skills in the field of Data Engineering?\n
                    It is observed that SQL and Python are the most demanded skills, but they are not the highest-paying skills.
                    In terms of demand, Azure and Spark are almost equal, but Spark offers more opportunities for higher paying jobs.
                    Another interesting point is Databricks, which is the highest paying skill yet low in demand. This could be because Databricks is still a new skill in the market, but is definitely acknowledge as employers are willing to pay a high amount for this expertise.
                    """
                },
                "project8": {
                    "title": "Sustainable City Dashboard",
                    "tools_used": ["R"],
                    "additional_skills": ["Rshiny", "Linear Regression", "Forecasting"],
                    "icon": "📊",
                    "link": "pages/SustainableCityDashboard.py",
                    "main_image": "assets/scd1.png",
                    "description": "This is a dashboard built using R to analyze city data in terms of quality of life and sustainability. ",
                    "resources": """
                    Dashboard Demo: https://www.youtube.com/watch?v=Z-Nlcof9QG4 (please skip to 1:58 for the demo)
                    """,
                    "add_image1": "assets/scd2.png",
                    "add_image2": "assets/scd3.png",
                    "add_image3": "assets/scd4.png",
                    "documentation": """
                    Note:\n
                    This is a university group project and my first Rshiny projects 3 months into learning R. Please refer to the YouTube video for a showcase of the dashboard.\n
                    1) Data Cleaning\n
                    Data cleaning was conducted in R by dropping irrelevant columns and removing rows with missing data.\n
                    2) Data Visualization\n
                    The visualizations are mainly constructed using the 'ggplot2' library. The full dashboard is built using Rshiny.\n
                    3) Linear Regression\n
                    Linear regression is a common skill for data analysts to identify the relationship between two variables.
                    In this case, R is capable of conducting linear regression and also calculating its P-value and R squared value
                    to determine the reliability of the results.
                    4) Forecasting\n
                    Forecasting is done in R using the 'forecast' library.

                    """
                }
            }