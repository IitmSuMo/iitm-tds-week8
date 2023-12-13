import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

st.title("Find the largest among the 3 given numbers(value greater than the other two)")

a = st.number_input("Enter 1st number", value = 0.0)
b = st.number_input("Enter 2nd number", value = 0.0)
c = st.number_input("Enter 3rd number", value = 0.0)

if st.button("Find Largest"):
    n = find_largest(a, b, c)
    st.success(f'The largest number is {n}')


