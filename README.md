
# 📑 Excel Tabs to App

A simple Streamlit app to preview, filter, and export Excel files with multiple sheets — all managed through a clean sidebar dropdown (no bottom tabs like Excel).

---

## 🚀 Features

- Upload `.xlsx` Excel files
- Select sheets via sidebar dropdown
- Preview full sheet data with shape info
- Apply filters dynamically:
  - 🔢 Numeric columns → Range sliders
  - 🔤 Text/object columns → Multiselect
- View filtered data
- Download filtered data as CSV

---

## 🛠️ Installation

### 1. Clone the repo

```bash
git clone git@github.com:Errec/excel-tabs-to-app.git
cd excel-tabs-to-app
```

### 2. Create and activate a virtual environment (Recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 💻 Usage

1. Upload an Excel file (`.xlsx`).
2. Choose the sheet using the **sidebar dropdown**.
3. Apply filters from the sidebar (range sliders or multiselects depending on the column type).
4. Preview filtered data in the main view.
5. Download the filtered results as a CSV.

---

## 📂 Folder Structure

```
excel-tabs-to-app/
├── app.py
├── requirements.txt
├── README.md
└── .venv/ (optional, local virtual environment)
```

---

## 🧠 Requirements

- Python 3.9+
- Tested on Debian 12, macOS, Ubuntu, and Windows

---

## ⚙️ Dependencies

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [OpenPyXL](https://openpyxl.readthedocs.io/)

---

## 🤝 Contributions

PRs are welcome. Open an issue if you'd like to discuss improvements or features.

---

## 🏷️ License

MIT License — free to use, modify, and distribute.

---

## 🔥 Demo Screenshot

*(Insert screenshot here if desired)*

---

Made with ❤️ by [@Errec](https://github.com/Errec)
