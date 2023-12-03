import pickle
import streamlit as st
import requests
from PIL import Image 

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

img=Image.open('movies-80.png')
st.set_page_config(page_title='Movie Recommendation System',page_icon=img)
# Display the content using st.markdown
# Read the CSS file
# css = """run app.py

#           <link rel="stylesheet" type="text/css" href="style">
# """

css = """
            <link rel="stylesheet"  href="style.css">
       """



# Apply the CSS file to the app
st.markdown(css, unsafe_allow_html=True)

# # Read the CSS file
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# # Apply the CSS file to the app
# local_css("style.css")


# st.header('Movie Recommender System')

# Title of the application
st.write(
    f"""
    <div style="text-align:center;margin-top: -10px;">
        <h1 style="text-align:center;margin-top: -20px;margin-bottom:40px;">
        <code style='font-size: 40px;'>
        Movie Recommender System
        </code>
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

movies = pickle.load(open('model/movie_list.pkl','rb'))
similarity = pickle.load(open('model/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

# Center-align the "Show Recommendation" button
# st.write(
#     f"""
#     <div style="text-align: center; margin-top: 20px; margin-bottom: 20px;">
#         <button style="padding: 10px 20px; font-size: 16px;" type="button" onclick="document.getElementById('recommendation_form').submit();">Show Recommendation</button>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


if st.button('Show Recommendation', key='recommendation_button', help='Click to show recommendations'):
    with st.form(key='recommendation_form'):
        st.form_submit_button(label='Submit')
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])

        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])

st.write(
    f"""
    <div style="text-align:center; margin-top: 30px;"><br><br>
        <p>Made With <span style='color: red;'>&#10084;</span> 
        <br>
        <i>
        by 
        </i>
        <br> 
        <code style='font-size: 24px;'><b> Subhransu Priyaranjan Nayak </b>  </code>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

