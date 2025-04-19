🚲 CityBike Activity Tracker

This project tracks bike-sharing activity in major cities around the world using the CityBikes API. It collects, processes, and analyzes real-time data on bike availability, 
then displays it through an interactive dashboard built with Tableau Desktop.


📌 Project Goals

    Automatically download real-time data from CityBike stations.

    Analyze the data to compute:

        The active bike frequency per minute.

        The percentage variation in available bikes over the last 15 minutes.

    Visualize insights in a dynamic and user-friendly way, including:

        City-level, country-level, and continent-level rankings.

        Proportional comparisons by region.



🛠️ Technologies Used

    Python 🐍 for data fetching and processing:

        requests, pandas, datetime, os, csv

    CityBikes API for real-time station data.

    Tableau Desktop for interactive dashboards.

    Google Drive to store and sync processed CSV data.

    GitHub Actions for automated hourly data updates.



📁 Project Structure  
.  
├── getting/  
│   └── _*.csv                       # Downloaded data files  
├── live/  
│   └── .csv                         # Validated data file  
├── .github/  
│   └── workflows/  
│       └── data-pipelines.yml      # GitHub Action for hourly automation  
|       └── upload.yml              # GitHub Action for hourly automation  
├── GetData.py                     # Downloaded data script  
├── PrepaData.py                    # Validated data script  
├── upload_drive.py                # Update data in drive  
├── README.md  
├── requirements.txt  
└── LICENSE  

<br/>
<br/>
<br/>
  
🚀 How to Run Locally

Clone the repository:
git clone https://github.com/black-jacgua/Bike-station.git
cd citybike-tracker


Install dependencies:
pip install -r requirements.txt


Run the scripts manually:
python getData.py
python prepaData.py

Open the Tableau dashboard and connect it to the updated CSV files.





📊 Tableau Dashboard

Interactive dashboard published on Tableau Public:  
https://public.tableau.com/app/profile/rotshill.jb/viz/Bike_station_17450466535500/Dashboard1



🔄 Automated Execution

A GitHub Actions workflow is scheduled to run every hour, triggering both data collection and processing scripts. 
Updated results are synced to Google Drive, enabling real-time dashboards without manual updates.




📄 License

Distributed under the MIT License. See the LICENSE file for more information.



✨ Future Improvements

    Power BI integration

    Predictive analytics on bike trends

    Mobile-optimized dashboard version
