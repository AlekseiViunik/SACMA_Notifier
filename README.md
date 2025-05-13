# 🚨 SACMA Notifier

**SACMA Notifier** is a simple utility designed to monitor expiration dates of licenses and certificates stored in an Excel file.  
When a document is expired or nearing expiration, the program sends a notification email to the person responsible for updating it.

> ⚙️ Designed to work with an autolauncher that runs the app at predefined intervals.

---

## ✅ Requirements

- 📄 Excel file in the expected format  
- 📧 Email server access  
- 🐍 Python 3.10+  
- 📦 Required packages (`requirements.txt`)

---

## 📁 Project Structure
**SACMA_Notifier/**<br/>
├── **main.py** # Entry point of the application<br/>
├── **consts.py** # Constants used throughout the project<br/>
├── **settings.json** # Configuration file (Excel path, email settings, etc.)<br/>
├── **files/** # Example Excel file<br/>
├── **logic/** # Core logic: Excel parsing, mailing, JSON handling<br/>
└── **logs/** # Log files created during execution<br/>

## ⚙️ `settings.json` Format

```json
{
  "filepath": "relative_path_to_excel_file",
  "workers": {
    "<name>": {
      "start_column": "C",
      "end_column": "G",
      "email": "abc@abc.com"
    }
  }
}
```

## ▶️ How to Run
```bash
python main.py
```

## 📦 Build .exe (Windows Only)
```bash
pyinstaller --noconfirm --onefile main.py
```
