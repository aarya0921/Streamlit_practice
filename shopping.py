import streamlit as st


st.set_page_config(page_title="Shopping Cart", page_icon=":shopping_cart:", layout="centered")  #Page configuration
if "cart" not in st.session_state: #Cart is stored in session state(Live data)
    st.session_state.cart = []

st.title("SHOPPING CART")
colm1,colm2,colm3=st.columns(3) #divides the screen into 3 columns

with colm1:
    st.subheader("Iphone")
   
    st.image("https://images.pexels.com/photos/1693627/pexels-photo-1693627.jpeg",width=200) #image
    if st.button("Add to Cart",key="Iphone"):
        st.success("Item added to cart")
        st.session_state.cart.append("Iphone")

with colm2:
    st.subheader("Samsung")
    st.image("https://images.pexels.com/photos/214488/pexels-photo-214488.jpeg",width=200)
    if st.button("Add to Cart",key="Samsung"):
        st.success("Item added to cart")
        st.session_state.cart.append("Samsung")


with colm3:
    st.subheader("Realme")
    st.image("https://images.pexels.com/photos/27359750/pexels-photo-27359750.jpeg",width=200)
    if st.button("Add to Cart",key="Realme"):
        st.success("Item added to cart")
        st.session_state.cart.append("Realme")

st.sidebar.text_input("Enter your name",key="name")
st.sidebar.text_input("Enter your email",key="email")
st.sidebar.text_input("Enter your pin code",key="pincode")
st.sidebar.write("Cart Summary")
if st.session_state.cart:   # Check if cart is not empty
    with st.sidebar.expander("View Cart"):  #Expander to view cart items
        for item in st.session_state.cart:
            st.write(item) 

    if st.sidebar.button("Clear Cart"):
        st.session_state.cart = []
        st.sidebar.success("Cart cleared!")
else:
    st.sidebar.write("Your cart is empty.")


