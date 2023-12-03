

<a name="readme-top"></a>

<div align="center">
  
# Movie-Recommendation-System
#### This project focuses on data cleaning, exploratory data analysis (EDA), machine learning, and natural language processing (NLP) in conjunction with a web application.  

<img src="https://machinelearninggeek.com/wp-content/uploads/2022/01/image-2.png" width="700" height='400' />

  </div>

## `About`

- This project uses machine learning to set up a system that suggests movies to watch.
- The system uses a collection of movie overviews and movie features to suggest movies to users based on what they like and how they behave.
- Users can get unique movie suggestions from the recommendation system, which uses content-based filtering.

See the implementation details with <a href="https://github.com/NayakSubhransu/Movie-Recommendation-System/blob/main/Movie_Recommendation_System.ipynb">IPython Notebook</a>

### __Installation__
To use the app on the local machine, open Anaconda Prompt and run the following commands:

1. Clone the Repository
```sh
git clone git@github.com:NayakSubhransu/Movie-Recommendation-System.git
```

2. Change Working Directory
```sh
cd Movie-Recommendation-System
```

3. If needed create a Virtual Environment and activate it
```sh
conda create -n environment_name python=3.10
conda activate environment_name
```
### OR 
```For Windows

py -3 -m venv venv
venv\Scripts\activate```

```For macOS and Linux

python3 -m venv venv
source venv/bin/activate```



4. Install the requirements
```sh
python -m pip install -r requirements.txt
```

5. Run the App
```sh
streamlit run app.py
```

6. Open the URL generated in a browser to use the App

7. To Run the application on CLI, install the following packages
 ```sh
 pip install pandas requests rich
 ```
8. Run the following Commands in the terminal:

To see the movie list, Run the following Command

```python app_cli.py --movie list --page_number 2(default)```

To predict the top 5 movies according to your selected movie, Run the following Command

```python app_cli.py --movie "YourMovieTitle" --num_recommendations 5(default)```


## `Key Features`

- Implements The content based Filtering Algorithm
- Implements Cosine Similarity Algorithm and Vectorization of Textual Documents 
- Utilizes user-based and item-based collaborative filtering techniques
- Provides movie suggestions based on user preferences and movie similarities
    
## `Dataset`

The system utilizes a movie dataset containing movie features and Movie credits. The dataset is preprocessed to extract relevant features and ratings, which are then used to train and evaluate the recommendation system.

## `Requirements`
- Jupyter Notebook
- Pandas
- Numpy
- nltk
- sklearn
- pickle
- streamlit

  
## `Usage`

The recommendation system can be used to provide movie suggestions for new and existing users. Users can input their preferences, and the system will generate a list of recommended movies based on their input and historical data.

## `Future Improvements`

- Incorporate deep learning models for better recommendation accuracy
- Enhance the user interface for a more user-friendly experience
- Integrate additional data sources for improved recommendations

## `Contributing`

Contributions to the movie recommendation system are welcome. If you find any issues or would like to add new features, please feel free to open an issue or submit a pull request.

## `Acknowledgements`

- The project was inspired by the need to provide users with personalized movie recommendations.
- We would like to thank the open-source community for providing valuable resources and tools that facilitated the development of this system.


<p align="right">
(<a href="#readme-top">back to top</a>)
</p>
