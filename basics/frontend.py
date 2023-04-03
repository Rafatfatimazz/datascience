from sqlalchemy.orm import sessionmaker
from sql import UserInput, Prediction
from sqlalchemy import create_engine
import streamlit as st 
engine=create_engine("sqlite:///project_db.sqlite3")
Session=sessionmaker(bind=engine)
sess=Session()
 # to run :streamlit run foldername\filename

st.title("using database with SQLALCHEMY")
area=st.number_input("enter area in sqrfeet",
                        max_value=10000, 
                        min_value=100,
                        value=400)
rooms=st.number_input("enter no of rooms",
                        max_value=50, 
                        min_value=2,
                        value=5) 
age=st.number_input("enter year of house manf.",
                        max_value=10, 
                        min_value=1,
                        value=2)
location=st.text_area("enter location address")   
submit =st.button("make predictions")   

if submit and location :
    try:
        entry=UserInput(house_area=area,
                       no_of_rooms=rooms,
                       age=age,
                       location=location)
        sess.add(entry)
        sess.commit()
        st.success("data added to database")
    except Exception as e:
        st.error(f"some error occured:{e}")  
if st.checkbox("veiw data"):
    results=sess.query(UserInput).all()
    for item in results:
        st.subheader(item.location)  
        st.text(item.location) 
        st.text(item.house_area)  
        st.text(item.age)  
        st.text(item.no_of_rooms)  
                    

    #st.write("we got input")                                                                