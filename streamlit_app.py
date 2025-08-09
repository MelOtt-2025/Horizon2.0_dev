import streamlit as st
import pandas as pd
import plotly as pl
import os
import numpy as np
import plotly.express as px

st.markdown(
    """
    <style>
    /* Set body and html to black */
    html, body {
        background-color: #000000 !important;
        color: #ffffff !important;
    }

    /* Streamlit main container background */
    [data-testid="stAppViewContainer"] {
        background-color: #000000 !important;
    }

    /* Main content block */
    [data-testid="stVerticalBlock"] {
        background-color: #000000 !important;
    }

    /* Sidebar background */
    [data-testid="stSidebar"] {
        background-color: #111111 !important;
    }

    /* Tabs and widget text */
    [class^="st-"], [class*="st-"] {
        color: #ffffff !important;
        background-color: #000000 !important;
    }

    /* Table styling */
    .stTable th, .stTable td {
        color: #ffffff !important;
        background-color: #111111 !important;
    }

    /* Text input labels and other controls */
    label, div[data-testid="stText"], div[data-testid="stMarkdownContainer"] {
        color: #ffffff !important;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }

    /* Slider background */
    .stSlider > div[data-baseweb="slider"] {
        background: #333333 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

###Sidebar menu
st.sidebar.title("Menu")
st.sidebar.write("Add in buttons and sliders etc")
sidebar_input = st.sidebar.text_input("Write something here")

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

    if sidebar_input:
        st.write(f"you have written:{sidebar_input}")

# Tab 2: Model Selection
with tab2:
    st.header("🧠 Model Selection")

    # Load preset weights
    preset_path = os.path.join("data", "model_weights.csv")
    if os.path.exists(preset_path):
        preset_df = pd.read_csv(preset_path)
    else:
        preset_df = pd.DataFrame(columns=["Model", "Axis", "Variable", "Weight"])

    # Dropdowns
    model = st.selectbox("Select a model:", ["Strategic Environment", "Technology", "Aviation", "Custom"])
    year = st.selectbox("Select year:", ["2025", "2026", "2027", "2028"])

    if model == "Custom":
        st.markdown("### ⚖️ Create a Custom Model")

        model_name = st.text_input("Enter a name for your custom model:", value="Custom_Aug2025")

        x_vars = [f"X_Factor{i}" for i in range(1, 6)]
        y_vars = [f"Y_Risk{i}" for i in range(1, 6)]
        z_vars = [f"Z_Cap{i}" for i in range(1, 6)]

        # One form, three columns: X, Y, Z
        with st.form("custom_form"):
            col_x, col_y, col_z = st.columns(3)

            with col_x:
                st.subheader("📈 X Axis")
                x_weights = {v: st.slider(f"{v}", 0, 10, 0, key=f"x_{v}") for v in x_vars}

            with col_y:
                st.subheader("📉 Y Axis")
                y_weights = {v: st.slider(f"{v}", 0, 10, 0, key=f"y_{v}") for v in y_vars}

            with col_z:
                st.subheader("🧪 Z Axis")
                z_weights = {v: st.slider(f"{v}", 0, 10, 0, key=f"z_{v}") for v in z_vars}

            submit = st.form_submit_button("💾 Save Custom Model")

        custom_path = os.path.join("data", "custom_model_weights.csv")

        if submit:
            rows = (
                [(model_name, "X", k, v) for k, v in x_weights.items()] +
                [(model_name, "Y", k, v) for k, v in y_weights.items()] +
                [(model_name, "Z", k, v) for k, v in z_weights.items()]
            )
            new_df = pd.DataFrame(rows, columns=["Model", "Axis", "Variable", "Weight"])

            overwrite = True
            if os.path.exists(custom_path):
                existing = pd.read_csv(custom_path)
                if model_name in existing["Model"].unique():
                    overwrite = st.checkbox(f"⚠️ Model '{model_name}' exists. Overwrite?", value=False)

                if overwrite:
                    existing = existing[existing["Model"] != model_name]
                    combined = pd.concat([existing, new_df], ignore_index=True)
                    combined.to_csv(custom_path, index=False)
                    st.success(f"✅ Saved and overwritten `{model_name}`.")
                else:
                    st.warning("❌ Save cancelled.")
            else:
                new_df.to_csv(custom_path, index=False)
                st.success(f"✅ Custom model `{model_name}` saved!")

            if overwrite:
                st.markdown("#### Saved Weights")
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.write("X Axis")
                    st.table(new_df.query("Axis == 'X'")[["Variable", "Weight"]])
                with c2:
                    st.write("Y Axis")
                    st.table(new_df.query("Axis == 'Y'")[["Variable", "Weight"]])
                with c3:
                    st.write("Z Axis")
                    st.table(new_df.query("Axis == 'Z'")[["Variable", "Weight"]])

        # Load & manage saved custom models
        st.divider()
        st.markdown("### 🗂️ Manage Saved Custom Models")

        if os.path.exists(custom_path):
            saved_df = pd.read_csv(custom_path)
            models = saved_df["Model"].unique().tolist()
            if models:
                selected = st.selectbox("📂 Load a Saved Custom Model", models)
                st.markdown(f"#### 🔍 Weights for `{selected}`")
                c1, c2, c3 = st.columns(3)
                with c1:
                    st.write("X Axis")
                    st.table(saved_df.query("Model == @selected and Axis == 'X'")[["Variable", "Weight"]])
                with c2:
                    st.write("Y Axis")
                    st.table(saved_df.query("Model == @selected and Axis == 'Y'")[["Variable", "Weight"]])
                with c3:
                    st.write("Z Axis")
                    st.table(saved_df.query("Model == @selected and Axis == 'Z'")[["Variable", "Weight"]])

                if st.button(f"🗑️ Delete `{selected}`"):
                    saved_df = saved_df[saved_df["Model"] != selected]
                    saved_df.to_csv(custom_path, index=False)
                    st.success(f"✅ Deleted model `{selected}`. Refresh to update.")
            else:
                st.info("No saved custom models.")
        else:
            st.info("No saved custom model file found.")

    else:
        st.markdown(f"### 📋 Preconfigured Weights for `{model}` Model")
        mdf = preset_df[preset_df["Model"] == model]
        c1, c2, c3 = st.columns(3)
        with c1:
            st.write("X Axis")
            st.table(mdf.query("Axis == 'X'")[["Variable", "Weight"]])
        with c2:
            st.write("Y Axis")
            st.table(mdf.query("Axis == 'Y'")[["Variable", "Weight"]])
        with c3:
            st.write("Z Axis")
            st.table(mdf.query("Axis == 'Z'")[["Variable", "Weight"]])
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
