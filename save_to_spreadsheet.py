import gspread
from google.oauth2.service_account import Credentials

# Fungsi untuk menyimpan DataFrame ke Google Spreadsheet
def save_to_spreadsheet(df, spreadsheet_name, sheet_name):
    # Scope yang diperlukan untuk mengakses Google Sheets
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Load credentials dari file credential.json
    creds = Credentials.from_service_account_file('credential.json', scopes=scope)

    # Buat client gspread
    client = gspread.authorize(creds)

    # Buat atau buka spreadsheet
    try:
        spreadsheet = client.open(spreadsheet_name)
    except gspread.SpreadsheetNotFound:
        spreadsheet = client.create(spreadsheet_name)

    # Buat atau buka worksheet
    try:
        worksheet = spreadsheet.worksheet(sheet_name)
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(title=sheet_name, rows="100", cols="20")

    # Bersihkan worksheet sebelum menulis data baru
    worksheet.clear()

    # Simpan header
    worksheet.append_row(df.columns.tolist())

    # Simpan data
    worksheet.append_rows(df.values.tolist())

    print(f"Data berhasil disimpan ke Google Spreadsheet: {spreadsheet_name} - {sheet_name}")

# Contoh penggunaan
if __name__ == "__main__":
    import pandas as pd

    # Baca file Excel hasil scraping
    bukit_vista_df = pd.read_excel('data_bukit_vista.xlsx')
    property_description_df = pd.read_excel('property_description.xlsx')

    # Simpan ke Google Spreadsheet
    save_to_spreadsheet(bukit_vista_df, "Bukit Vista Scraping Results", "Properties")
    save_to_spreadsheet(property_description_df, "Bukit Vista Scraping Results", "Descriptions")