# COVID-19 Dashboard

## Introduction
Welcome to the COVID-19 Dashboard, a Python-based project developed using Dash and Plotly. This dashboard visualizes cumulative confirmed cases and deaths from COVID-19 across different countries. It offers interactive visualizations to track the progression of the pandemic over time.

## Features
- **Country-wise COVID-19 Tracking**: Select any country from the dropdown menu to view its cumulative COVID-19 confirmed cases and deaths.
- **Interactive Graphs**: The dashboard provides dynamic line charts to visualize the trends in COVID-19 cases and deaths for the selected country.
- **Real-time Data**: The data used in this dashboard is based on historical time series records of confirmed cases and deaths.

## Files and Instructions

### Files
- `covid.py`: The main script that runs the COVID-19 Dashboard.
- `time_series_19-covid-Confirmed_archived_0325.csv`: Dataset containing the time series data of confirmed COVID-19 cases.
- `time_series_19-covid-Deaths_archived_0325.csv`: Dataset containing the time series data of COVID-19 deaths.

### Instructions to Run
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/COVID-19-Dashboard.git
   ```

2. Next navigate to the directory where you cloned it and the run the following commands:
```bash
   cd COVID-19-Dashboard
   python3 covid.py
```

3. The next lines should appear like :


4. Now you just have to follow the link which might look like:
   ```bash
      http://127.0.0.1:8050/
   ```

   Open the link in your web browser to view the dashboard.

## Website Features
Once the dashboard is running, you can explore the following features:

- **Dropdown Menu**: The top dropdown allows you to select any country. The graphs below will update in real-time to display cumulative confirmed cases and deaths for the selected country.

- **Cumulative COVID-19 Cases Graph**: This graph shows the trend of confirmed COVID-19 cases in the selected country. You can hover over points on the graph to see detailed case numbers for specific dates.

- **Cumulative COVID-19 Deaths Graph**: This graph displays the number of deaths due to COVID-19 in the selected country. Similar to the cases graph, you can hover over points to see specific death counts on different dates.

## Example Output

Here are screenshots of the dashboard in action:

### COVID-19 Dashboard Main View
screenshot soon

### Country-Wise Case Graph
screenshot soon

### Country-Wise Death Graph
screenshot soon



## 🧠 Technologies Used
- **Dash**: For building the interactive web dashboard.
- **Plotly**: For creating dynamic graphs and visualizations.
- **Pandas**: For data manipulation and preprocessing.

## 📊 Datasets
The data used for this project is sourced from the publicly available [COVID-19 time series datasets](https://github.com/CSSEGISandData/COVID-19/tree/master) provided by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University. The datasets include historical records of confirmed cases and deaths.

## 🚀 Future Enhancements
- 🌍 **Real-time Data**: Integrate APIs to pull real-time COVID-19 data for live tracking.
- 🧭 **Advanced Filters**: Add filters to compare multiple countries simultaneously.
- 📈 **Additional Metrics**: Include metrics like recoveries, active cases, and vaccination data.

🤝 **Contributing**: Contributions are welcome! Feel free to open issues or submit pull requests to enhance the dashboard.
