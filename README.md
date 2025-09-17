# ChartMySurvey
Upload your survey, get instant insights in charts . ChartMySurvey is a Django-based web application that allows users to upload survey data in Excel format and instantly visualize the responses as interactive graphs. 

Instead of manually counting and analyzing survey results, this app automatically processes the uploaded file and displays the results in a clear and graphical format.  

Features
User Authentication – Register, Login, and Logout securely.  
File Upload – Upload Excel survey files easily.  
Automated Analysis – Detects single-choice & multiple-choice responses.  
Response Aggregation – Combines counts for multi-choice answers.  
Interactive Charts – Results displayed in graphical format using Chart.js.  
File-based Results – Analyzed results stored as JSON for quick access.  

Tech Stack
Backend: Django (Python)  
Frontend: HTML, CSS, Bootstrap   
Data Handling: Pandas (Excel analysis)  
Database: SQLite (default Django authentication)  

How It Works
1. Register or login to your account.  
2. Upload an Excel survey file.  
3. The app analyzes the data using Pandas.  
4. Results are saved as a JSON file.  
5. Graphs are displayed instantly with Chart.js.  

Future Enhancements
Export graphs as PDF/PNG reports
Support for CSV & Google Sheets import 
 
Author
Developed by Jeethu Koppal  

If you like this project,star the repo and contribute! 
