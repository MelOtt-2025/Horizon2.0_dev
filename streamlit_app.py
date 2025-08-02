import streamlit as st
import pandas as pd
import plotly as pl
import os
import numpy as np
import plotly.express as px



# App title
st.set_page_config(page_title="Horizon Scanning Dashboard", layout="wide")

# Define tab structure
tab1, tab2, tab3, tab4 = st.tabs([
    "Horizon Scanning",
    "Model Selection",
    "Chart",
    "Results Drivers"
])

# Sample data
np.random.seed(42)
n = 100
df = pd.DataFrame({
    "X": np.random.uniform(0, 100, n),
    "Y": np.random.uniform(0, 100, n),
    "Z": np.random.uniform(10, 50, n),
    "Category": np.random.choice(["Category A", "Category B", "Category C"], n),
    "Label": [f"Point {i}" for i in range(n)]
})

# Tab 1: Horizon Scanning
with tab1:
    st.header("🌐 Horizon Scanning")
    st.markdown("""
    This section provides an overview of horizon scanning data, including structured and unstructured inputs.
    You can upload datasets, define axes, and explore the evolving landscape of strategic themes.
    """)
    uploaded_file = st.file_uploader("Upload CSV data for scanning", type="csv")
    if uploaded_file:
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

# Tab 2: Model Selection
with tab2:
    st.header("🧠 Model Selection")

    model = st.selectbox("Select a model:", ["Strategic Environment", "Technology", "Aviation", "Custom"])
    year = st.selectbox("Select year:", ["2025", "2026", "2027", "2028"])

    if model == "Custom":
        st.markdown("### ⚖️ Set Variable Weights for Custom Model")

        # Dummy variable names
        x_vars = ["X_Factor1", "X_Factor2", "X_Factor3", "X_Factor4", "X_Factor5"]
        y_vars = ["Y_Risk1", "Y_Risk2", "Y_Risk3", "Y_Risk4", "Y_Risk5"]
        z_vars = ["Z_Cap1", "Z_Cap2", "Z_Cap3", "Z_Cap4", "Z_Cap5"]

        # Sub-tabs for axis weights
        x_tab, y_tab, z_tab = st.tabs(["X Axis Variables", "Y Axis Variables", "Z Axis Variables"])

        with x_tab:
            st.subheader("📈 X Axis - Connection Variables")
            x_weights = {var: st.slider(f"Weight for {var}", 1, 10, 5) for var in x_vars}

        with y_tab:
            st.subheader("📉 Y Axis - Risk Variables")
            y_weights = {var: st.slider(f"Weight for {var}", 1, 10, 5) for var in y_vars}

        with z_tab:
            st.subheader("🧪 Z Axis - Capability Variables")
            z_weights = {var: st.slider(f"Weight for {var}", 1, 10, 5) for var in z_vars}

        # Display weights in tables
        st.markdown("### 🧾 Summary of Selected Weights (Tabular Format)")

        x_df = pd.DataFrame(list(x_weights.items()), columns=["X Variable", "Weight"])
        y_df = pd.DataFrame(list(y_weights.items()), columns=["Y Variable", "Weight"])
        z_df = pd.DataFrame(list(z_weights.items()), columns=["Z Variable", "Weight"])

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("#### X Axis Weights")
            st.table(x_df)
        with col2:
            st.markdown("#### Y Axis Weights")
            st.table(y_df)
        with col3:
            st.markdown("#### Z Axis Weights")
            st.table(z_df)
    else:
        st.info("Preset models will be configured in future steps.")


# Tab 3: Chart
with tab3:
    st.header("📊 Chart")
    st.markdown("This section will display the 3D bubble chart once data and model selections are made.")
    st.markdown("To be implemented: Bubble plot visualization using Plotly or Altair.")

    # Category selection
    categories = df["Category"].unique().tolist()
    selected_cats = st.multiselect("Select Categories:", categories, default=categories)

# Filter data
    filtered_df = df[df["Category"].isin(selected_cats)]

# Create bubble chart
    fig = px.scatter(
    filtered_df, x="X", y="Y", size="Z", color="Category",
    hover_name="Label", size_max=40
)

    fig.update_layout(
    title="Interactive Bubble Chart",
    xaxis=dict(range=[0, 100], zeroline=True, zerolinewidth=2, zerolinecolor='gray'),
    yaxis=dict(range=[0, 100], zeroline=True, zerolinewidth=2, zerolinecolor='gray'),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Show chart
    st.plotly_chart(fig, use_container_width=True)





# Tab 4: Results Drivers
with tab4:
    st.header("🔍 Results Drivers")
    st.markdown("""
    This section shows the key drivers behind the results. You’ll be able to explore contributions
    of different factors to the model outcomes and drill down into regional or thematic trends.
    """)
    st.markdown("To be implemented: Driver ranking and factor breakdown visualization.")



###adding in an image
###st.image(os.path.join(os.getcwd(), "static", "green_red_gradient.png"))
