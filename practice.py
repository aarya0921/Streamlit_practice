import streamlit as st
st.set_page_config(page_title="Practice", page_icon=":pencil2:", layout="centered")
st.title("Practice Page")
st.subheader("this is a practice page")
st.write("To display text,JSON file,plots etc")
st.text("Only text can be displayed ")
st.success("This is a success message")
st.error("This is an error message")
 

 #Widgets
if st.button("Click Me",key="button1"):  #key is used to identify the widget
       st.success("Button clicked!") 

check=st.checkbox("Check me",key="checkbox1")
if check:
    st.write("Checkbox is checked") 

fav_char=st.radio("Please select your fav character",["Thor","Captain America","Iron man"],index=0)

st.selectbox("Country:",["India","USA","UK","China"],index=0) #index for deafault selection

st.slider("Select a number",0,100,50)  #min,max,default
st.select_slider("Select a range of numbers",options=list(range(0,101)),value=(20,80)) #range of numbers


no_of_pro=st.number_input("Enter number of products",min_value=1,max_value=100,value=10,step=1)
print("Number of products:", no_of_pro)
st.text_input("Enter your name",placeholder="Name",key="name_input")
st.text_area("Enter your address",placeholder="Address",key="address_input")
st.date_input("Select a date",value=None,key="date_input")
st.time_input("Select a time",value=None,key="time_input")
st.file_uploader("Upload a file",type=["csv","txt","pdf"],key="file_uploader")
st.color_picker("Pick a color",value="#00f900",key="color_picker")
st.multiselect("Select your hobbies",["Reading","Traveling","Cooking","Gaming"],default=["Reading"],key="multiselect")

