# Import your libraries
import pandas as pd

# Start writing code
airbnb_search_details.head()

# logging data count to check if missing values exists
print(airbnb_search_details['host_response_rate'].isnull().sum())

# returning data for entries with missing data
missing_data_host_response_rate = airbnb_search_details[airbnb_search_details['host_response_rate'].isnull()]
print(missing_data_host_response_rate)
