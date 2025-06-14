import streamlit as st
import pandas as pd

st.set_page_config(page_title="Excel Tab Viewer", layout="wide")
st.title("📑 Excel Tab Viewer")

# Upload Excel file
uploaded_file = st.file_uploader("Upload your Excel file (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Load Excel file
        xls = pd.ExcelFile(uploaded_file)
        sheet_names = xls.sheet_names

        st.sidebar.header("Settings")

        # Dropdown to select sheet
        selected_sheet = st.sidebar.selectbox(
            "Select Sheet (Tab)", sheet_names, index=0
        )

        # Load selected sheet
        df = pd.read_excel(xls, sheet_name=selected_sheet)

        # Sheet info
        st.subheader(f"📄 Sheet: {selected_sheet}")
        st.caption(f"Rows: {df.shape[0]} | Columns: {df.shape[1]}")
        with st.expander("🔍 Data Preview"):
            st.dataframe(df, use_container_width=True)

        # Sidebar filters
        st.sidebar.subheader("Filter Data")
        filters = {}

        for col in df.columns:
            if pd.api.types.is_numeric_dtype(col):
                min_val, max_val = float(df[col].min()), float(df[col].max())
                selected_range = st.sidebar.slider(
                    f"{col} range", min_val, max_val, (min_val, max_val)
                )
                filters[col] = selected_range

            elif pd.api.types.is_string_dtype(df[col]) or pd.api.types.is_object_dtype(df[col]):
                unique_vals = df[col].dropna().unique().tolist()
                if len(unique_vals) <= 100:
                    selected_vals = st.sidebar.multiselect(f"{col} filter", unique_vals)
                    if selected_vals:
                        filters[col] = selected_vals

        # Apply filters
        filtered_df = df.copy()

        for col, condition in filters.items():
            if isinstance(condition, tuple):
                filtered_df = filtered_df[
                    filtered_df[col].between(condition[0], condition[1])
                ]
            else:
                filtered_df = filtered_df[filtered_df[col].isin(condition)]

        # Display filtered data
        st.subheader("📊 Filtered Data")
        st.dataframe(filtered_df, use_container_width=True)

        # Download filtered data
        if not filtered_df.empty:
            csv = filtered_df.to_csv(index=False).encode('utf-8')
            st.download_button(
                "Download CSV",
                data=csv,
                file_name=f"{selected_sheet}_filtered.csv",
                mime="text/csv"
            )
        else:
            st.warning("⚠️ No data to download after applying filters.")

    except Exception as e:
        st.error(f"❌ Error loading sheet {selected_sheet}: {e}")

else:
    st.info("⬆️ Upload an Excel (.xlsx) file to begin.")
