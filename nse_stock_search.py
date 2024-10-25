import requests
import pandas as pd
import streamlit as st

# Function to fetch data from NSE API with proper session handling
def fetch_nse_indices():
    url = "https://www.nseindia.com/api/allIndices"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.nseindia.com/",
        "DNT": "1"
    }

    # Create a session to handle cookies and session data
    session = requests.Session()
    session.headers.update(headers)

    # Initial request to set the session
    session.get("https://www.nseindia.com")

    # Now make the actual request to the API endpoint
    response = session.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Convert the response to JSON format
    else:
        st.error(f"Failed to fetch data from NSE. Status code: {response.status_code}")
        return None

# Function to display the indices data in Streamlit
def display_indices_data():
    st.title("NSE Indices Data")

    # Fetching NSE indices data
    data = fetch_nse_indices()

    if data:
        # Creating a DataFrame from the indices data
        indices_list = data['data']
        indices_df = pd.DataFrame(indices_list)

        # Display the DataFrame as a table in Streamlit
        st.write(indices_df)

        # Option to download the data as an Excel file
        st.download_button(
            label="Download data as CSV",
            data=indices_df.to_csv(index=False).encode('utf-8'),
            file_name='nse_indices.csv',
            mime='text/csv'
        )

# Main app execution
if __name__ == "__main__":
    display_indices_data()
