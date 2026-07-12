# Python Webview Digital Clock

A modern desktop **digital clock application** built with **Python**, **pywebview**, and **HTML/CSS/JavaScript**.

The application uses Python as the backend and a web interface for the UI, providing a modern and customizable desktop experience.

---

## 📌 Features

* Real-time digital clock (HH : MM : SS)
* Current date display
* Auto-update every second
* Modern HTML/CSS user interface
* Python and JavaScript communication using pywebview
* Lightweight desktop application
* Custom window size support
* Ready to package as Windows `.exe`

---

## 🖥️ Preview

The interface displays:

* **Application Title**: Time Now
* **Date**: Current day, month, and year
* **Time**: Live hours, minutes, and seconds

Example:

```
        Time Now

   Sunday, 12 July 2026

        18:45:30
```

---

## 🛠️ Technologies Used

### Backend

* Python
* pywebview

### Frontend

* HTML5
* CSS3
* JavaScript

---

## 📦 Installation

### 1. Clone the project

```bash
git clone <your-repo-url>
cd <your-project-folder>
```

### 2. Install requirements

```bash
pip install pywebview
```

---

## ▶️ Run the Application

Make sure your project contains:

```
project/
│
├── main.py
│
└── web/
    ├── index.html
    ├── style.css
    └── script.js
```

Run:

```bash
python main.py
```

---

## 🧩 Project Structure

```
DigitalClock/
│
├── main.py              # Python backend and desktop window
│
├── web/
│   ├── index.html       # Application interface
│   ├── style.css        # UI design
│   └── script.js        # Clock logic and Python communication
│
├── icon.ico             # Application icon
│
└── README.md
```

---

## 🧠 How It Works

The application is divided into two parts:

### Python Backend

* Creates the desktop window using pywebview
* Provides date and time data
* Communicates with JavaScript

### Web Interface

* HTML creates the page structure
* CSS controls the design and style
* JavaScript updates the clock every second

Communication:

```
Python
  |
  | pywebview API
  |
JavaScript
  |
  |
HTML/CSS Interface
```

---

## 📦 Build Windows EXE

Install PyInstaller:

```bash
pip install pyinstaller
```

Build:

```bash
pyinstaller --noconsole --onefile --add-data "web;web" main.py
```

The executable will be created inside:

```
dist/
```

---

## 🚀 Future Improvements

Possible features:

* Dark / Light mode
* World clock with multiple countries
* Calendar
* Alarm system
* Stopwatch
* Timer
* Custom themes
* Windows notifications

---

## 📄 License

This project is open-source — feel free to modify, improve, or use it in your own applications.

---

## 🙌 Author

Created by **Oussema**.