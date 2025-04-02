import streamlit as st
import nbformat
import os
import pandas as pd
import json
import base64

# Set Streamlit Page Config
st.set_page_config(page_title="📊 EDA Report Viewer", layout="wide")

# Title
st.title("📊 Exploratory Data Analysis (EDA) Report Viewer")

# Define the folder containing Jupyter Notebooks


notebook_folder = "../notebook" if os.path.exists("../notebook") else "./notebook"

notebooks = [f for f in os.listdir(notebook_folder) if f.endswith(".ipynb")]
notebooks.sort()

# Check if notebooks exist
if not notebooks:
    st.warning("⚠️ No EDA reports found in the 'ipynb' folder. Please generate and save an EDA notebook.")
else:
    # Dropdown to select a notebook
    selected_notebook = st.selectbox("Select an EDA Notebook:", notebooks,index=0)

    # Load and parse the selected notebook
    notebook_path = os.path.join(notebook_folder, selected_notebook)

    with open(notebook_path, "r", encoding="utf-8") as f:
        notebook = nbformat.read(f, as_version=4)

    # Extract and display cells
    st.subheader(f"📖 Notebook: {selected_notebook}")

    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            st.markdown(cell.source)  # Render Markdown content
        
        elif cell.cell_type == "code":
            st.code(cell.source, language="python")  # Show code
            
            # Display code outputs
            if "outputs" in cell:
                for output in cell.outputs:
                    if "text" in output:
                        st.text(output["text"])  # Show text output
                    elif "data" in output:
                        if "text/plain" in output["data"]:
                            st.text(output["data"]["text/plain"])
                        if "text/html" in output["data"]:
                            st.markdown(output["data"]["text/html"], unsafe_allow_html=True)
                        if "image/png" in output["data"]:
                            img_data = base64.b64decode(output["data"]["image/png"])
                            st.image(img_data, caption="Output Image")
                        if "application/json" in output["data"]:
                            json_data = json.loads(output["data"]["application/json"])
                            st.json(json_data)
                        if "text/csv" in output["data"]:
                            csv_data = output["data"]["text/csv"]
                            df = pd.read_csv(pd.compat.StringIO(csv_data))
                            st.dataframe(df)  # Display CSV as DataFrame

    # Provide a download button
    with open(notebook_path, "rb") as file:
        st.download_button(label="📥 Download Notebook", data=file, file_name=selected_notebook, mime="application/json")
