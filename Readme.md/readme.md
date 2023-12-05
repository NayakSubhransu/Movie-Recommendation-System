

# movie_recommender_cli_rich.py

## To find the CLI version of the Project , follow the Following Steps in sequence:

## create a Virtual Environment using the following Command:
   ### For Windows
   py -3 -m venv venv
   venv\Scripts\activate

   ### For macOS and Linux
   python3 -m venv venv
   source venv/bin/activate

   ### Bypass the Execution Policy:
```Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass```
   
   ### Then install necessary libraries
   pandas,requests,rich 

## Then run the following command in the Terminal:
```python app_cli.py --movie "YourMovieTitle" --num_recommendations 5```
```python app_cli.py --movie list --page_number 2```

# To Run The project on the web:

## Run the Following command in the terminal
```streamlit run app.py```