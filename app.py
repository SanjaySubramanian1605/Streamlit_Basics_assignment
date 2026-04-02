import streamlit as st
import pandas as pd

# Title and subheader
st.title("📊 Sales Summary Dashboard")
st.subheader("Filter and explore sales data by product category")

# Hardcoded dataset
data = {
    "Product": ["Laptop", "Mouse", "Desk", "Monitor", "Keyboard", "Chair", "Webcam"],
    "Category": ["Electronics", "Electronics", "Furniture", "Electronics", "Electronics", "Furniture", "Electronics"],
    "Sales": [1200, 25, 450, 300, 75, 600, 90],
}
df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("🔍 Filter Options")
categories = ["All"] + sorted(df["Category"].unique().tolist())
selected_category = st.sidebar.selectbox("Select a Category", categories)

# Filter data
if selected_category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == selected_category]

# Main content
st.markdown(f"### Showing results for: *{selected_category}*")
st.dataframe(filtered_df, use_container_width=True)

st.markdown("### 📈 Sales Chart")
st.line_chart(filtered_df.set_index("Product")["Sales"])