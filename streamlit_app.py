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

    /* Tab styling for better visual distinction */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #000000 !important;
        padding: 10px 0;
        border-bottom: 2px solid #333333;
    }

    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding: 0px 24px;
        background-color: #1a1a1a !important;
        border: 2px solid #333333 !important;
        border-radius: 8px 8px 0px 0px !important;
        color: #cccccc !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        margin-right: 4px;
    }

    .stTabs [data-baseweb="tab"]:hover {
        background-color: #2a2a2a !important;
        border-color: #555555 !important;
        color: #ffffff !important;
        transform: translateY(-2px);
    }

    .stTabs [aria-selected="true"] {
        background-color: #333333 !important;
        border-color: #666666 !important;
        color: #ffffff !important;
        border-bottom: 2px solid #333333 !important;
    }

    /* Tab content area */
    .stTabs [data-baseweb="tab-panel"] {
        background-color: transparent !important;
        border: none !important;
        padding: 20px !important;
        margin-top: -2px;
    }

    /* Remove background from tab content containers */
    .stTabs [data-baseweb="tab-panel"] > div {
        background-color: transparent !important;
        background: transparent !important;
    }

    /* Target any nested containers within tabs */
    .stTabs [data-baseweb="tab-panel"] * {
        background-color: transparent !important;
    }

    /* Override Streamlit's default container backgrounds within tabs */
    .stTabs .element-container {
        background-color: transparent !important;
    }

    .stTabs .stMarkdown {
        background-color: transparent !important;
    }

    /* Remove black backgrounds from text elements in tabs */
    .stTabs [data-testid="stMarkdownContainer"] {
        background-color: transparent !important;
        background: transparent !important;
    }

    .stTabs [data-testid="stText"] {
        background-color: transparent !important;
        background: transparent !important;
    }

    .stTabs [data-testid="stHeader"] {
        background-color: transparent !important;
        background: transparent !important;
    }

    /* Remove backgrounds from all block elements in tabs */
    .stTabs div[data-testid="block-container"] {
        background-color: transparent !important;
        background: transparent !important;
    }

    .stTabs div[data-testid="stVerticalBlock"] {
        background-color: transparent !important;
        background: transparent !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Must be the first Streamlit command
st.set_page_config(
    page_title="Horizon Scanning Dashboard",
    page_icon="📡",
    layout="wide"
)

# Optional: keep your dark theme CSS (put yours here if you have it)
# st.markdown("""<style> ... your dark CSS ... </style>""", unsafe_allow_html=True)

# --- HEADER: Title + Smaller Logo ---
hcol1, hcol2 = st.columns([0.85, 0.15])  # tweak ratios as you like
with hcol1:
    st.markdown(
        "<h1 style='margin:0; color:#ffffff;'>🌏 Horizon Scanning Dashboard</h1>"
        "<div style='color:#ccc;'>Interactive modelling • Visual analytics • Custom presets</div>",
        unsafe_allow_html=True
    )
with hcol2:
    logo_path = os.path.join("static", "SAS_logo.png")  # put your file here
    if os.path.exists(logo_path):
        # 👇 control logo size with width (e.g., 80 px)
        st.image(logo_path, width=100)
    else:
        st.empty()

st.markdown("<hr style='opacity:0.25; margin-top:0.5rem;'>", unsafe_allow_html=True)
# ====== END HEADER ======
raw_data = pd.read_csv(os.path.join("data", "ALL_RAW.csv"))

###Sidebar menu
st.sidebar.title("Menu")
st.sidebar.write("Add in buttons and sliders etc")
sidebar_input = st.sidebar.text_input("Write something here to show in main page")

# App title
st.set_page_config(page_title="Horizon Scanning Dashboard", layout="wide")

# Define tab structure
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Horizon Scanning",
    "Data Preparation",
    "Model Selection",
    "Chart",
    "Results Drivers"
])


# Sample data
np.random.seed(42)
n = 30
df = pd.DataFrame({
    "X": np.random.uniform(-50, 50, n),
    "Y": np.random.uniform(-50, 50, n),
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
    We will do a descrition of what horizon scanning is and how it can be used to identify trends and opportunities.
    Horizon scanning is a systematic process of identifying and analyzing emerging trends, risks, and opportunities that
    may impact an organization or sector in the future. It involves gathering information from various sources,
    including scientific literature, news articles, expert opinions, and social media, to detect patterns and
    signals of change. By systematically scanning the horizon, organizations can proactively adapt their strategies,
    make informed decisions, and seize opportunities before they become mainstream. This process is crucial for
    staying ahead in a rapidly changing world, enabling organizations to anticipate challenges and leverage emerging
    trends to their advantage.
    """)
    uploaded_file = st.file_uploader("Upload CSV data for scanning", type="csv")
    if uploaded_file:
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

    if sidebar_input:
        st.write(f"you have written:{sidebar_input}")

# Tab 2: Data Preparation
with tab2:
    st.header("Data Preparation")

    # Show variable summary
    st.subheader("Variable Summary")
    summary = []
    for col in raw_data.columns:
        if np.issubdtype(raw_data[col].dtype, np.number):
            stats = {
                "Variable": col,
                "Type": "Numeric",
                "Min": np.nanmin(raw_data[col]),
                "Max": np.nanmax(raw_data[col]),
                "Mean": np.nanmean(raw_data[col]),
                "Std": np.nanstd(raw_data[col])
            }
        else:
            stats = {
                "Variable": col,
                "Type": "Categorical",
                "Min": "",
                "Max": "",
                "Mean": "",
                "Std": ""
            }
        summary.append(stats)
    st.dataframe(pd.DataFrame(summary))

    # Data processing
    st.subheader("Process Variables")
    processed_data = raw_data.copy()
    for col in raw_data.columns:
        if np.issubdtype(raw_data[col].dtype, np.number):
            if st.button(f"Standardize {col}"):
                processed_data[col] = (raw_data[col] - raw_data[col].mean()) / raw_data[col].std()
        else:
            if st.button(f"Assign Levels to {col}"):
                processed_data[col] = raw_data[col].astype('category').cat.codes

    st.subheader("Processed Data Preview")
    st.dataframe(processed_data.head())

# Tab 3: Model Selection
with tab3:
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
# Tab 4: Chart
with tab4:
    st.header("📊 Chart")
    st.markdown("This section will display the 3D bubble chart once data and model selections are made.")

    # Category selection
    categories = df["Category"].unique().tolist()
    selected_cats = st.multiselect("Select Categories:", categories, default=categories)

    # Filter data
    filtered_df = df[df["Category"].isin(selected_cats)]

    # Create bubble chart
    fig = px.scatter(
        filtered_df,
        x="X", y="Y", size="Z", color="Category",
        hover_name="Label", size_max=40
    )

    # Update layout for quadrants
    fig.update_layout(
        title="Interactive Bubble Chart (Quadrants)",
        xaxis=dict(
            range=[-50, 50],
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='gray',
            title="X Axis",
            showgrid=False
        ),
        yaxis=dict(
            range=[-50, 50],
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='gray',
            title="Y Axis",
            showgrid=False
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=800,  # Increase chart height for better visibility
        width=800    # Optional: Force a larger width
    )

    # Show chart
    st.plotly_chart(fig, use_container_width=True)

# Tab 5: Results Drivers
with tab5:
    st.header("🔍 Results Drivers")
    st.markdown("Explore the key drivers behind results by geography and metric.")

    # ---------- Dummy data (replace with your real data) ----------
    import pandas as pd
    import plotly.express as px

    # Map data (lat/lon for 5 fake locations)
    map_df = pd.DataFrame({
        "Region": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide"],
        "lat": [-33.8688, -37.8136, -27.4698, -31.9505, -34.9285],
        "lon": [151.2093, 144.9631, 153.0251, 115.8605, 138.6007],
        "value": [50, 70, 40, 55, 35]
    })

    # Bar chart data
    bar_df = pd.DataFrame({
        "Driver": [f"Driver {i}" for i in range(1, 6)],
        "Contribution": [30, 45, 20, 55, 40]
    })

    # Line chart data
    line_df = pd.DataFrame({
        "Month": [f"2025-{m:02d}" for m in range(1, 13)],
        "Index": [80, 82, 79, 85, 88, 90, 87, 92, 95, 97, 99, 101]
    })

    # Pie chart data
    pie_df = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Share": [35, 25, 20, 20]
    })

    # ---------- Layout: row 1 (Map | Bar) ----------
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("🗺️ Map (placeholder)")
        fig_map = px.scatter_mapbox(
            map_df, lat="lat", lon="lon", size="value", color="Region",
            hover_name="Region", zoom=3, height=420
        )
        fig_map.update_layout(mapbox_style="open-street-map", margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig_map, use_container_width=True)

    with c2:
        st.subheader("📊 Bar Chart (placeholder)")
        fig_bar = px.bar(
            bar_df, x="Driver", y="Contribution", text="Contribution",
            title=None, template="plotly_dark"
        )
        fig_bar.update_traces(textposition="outside")
        fig_bar.update_layout(yaxis_title="Contribution", xaxis_title="Driver", height=420)
        st.plotly_chart(fig_bar, use_container_width=True)

    # ---------- Layout: row 2 (Line | Pie) ----------
    c3, c4 = st.columns(2)

    with c3:
        st.subheader("📈 Line Chart (placeholder)")
        fig_line = px.line(
            line_df, x="Month", y="Index", markers=True, title=None, template="plotly_dark"
        )
        fig_line.update_layout(yaxis_title="Index", xaxis_title="Month", height=420)
        st.plotly_chart(fig_line, use_container_width=True)

    with c4:
        st.subheader("🥧 Pie Chart (placeholder)")
        fig_pie = px.pie(
            pie_df, names="Category", values="Share", hole=0.3 , template="plotly_dark"
        )
        fig_pie.update_layout(height=420)
        st.plotly_chart(fig_pie, use_container_width=True)

 
    # Apply dark theme to all plots
for f in [fig_map, fig_bar, fig_line, fig_pie]:
    f.update_layout(template="plotly_dark")



###adding in an image
###st.image(os.path.join(os.getcwd(), "static", "green_red_gradient.png"))
