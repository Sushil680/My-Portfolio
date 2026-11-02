# Sushil Nath Yogi — Personal Portfolio Website

A responsive personal portfolio and web application built using **Python (Flask)**, **Bootstrap**, **JavaScript (Isotope, Waypoints)**, and **ReportLab**. Designed to showcase academic background, data science projects, Python applications, and creative graphic design work.

---

## 🌟 Key Features

- **Responsive Hero Section**: Fluid responsive typography with interactive glitch effect and dynamic animated typewriter cycling through professional roles.
- **Dynamic Portfolio Filtering**: Interactive portfolio gallery powered by Isotope and imagesLoaded with real-time filtering for Python Projects, Machine Learning, and Graphic Design.
- **CV / Resume Download**: Includes an automated CV generator (`generate_cv.py`) producing a professional 1-page PDF (`static/assets/cv.pdf`).
- **Interactive Contact Form**:
  - Validates user input safely.
  - Supports both standard browser submissions and AJAX with instant notifications.
  - Emails notifications using secure SMTP (`EmailMessage`).
  - **Local Fallback Storage**: Submissions are automatically saved to `contact_messages.json` so messages are never lost if email credentials are not configured or offline.
- **Custom Interactive 404 Page**: Dark interactive torch exploration page with mouse/touch spotlight effect and direct return navigation.
- **Comprehensive Unit Tests**: Built-in test suite covering page routing, asset delivery, form validation, and error handlers.

---

## 🛠️ Tech Stack

- **Backend**: Python 3, Flask, Jinja2
- **PDF Generation**: ReportLab
- **Frontend**: HTML5, CSS3, Bootstrap 4, JavaScript (jQuery, Isotope, Waypoints)
- **Styling**: Responsive custom CSS, Google Fonts (Raleway, Nunito Sans)

---

## 🚀 Getting Started

### 1. Prerequisites

Ensure you have Python 3.10+ installed.

### 2. Environment Setup

Clone or open the repository folder and create a virtual environment:

```bash
python3 -m venv env
source env/bin/activate    # On Linux/macOS
# or: env\Scripts\activate # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Generate CV PDF (Optional)

To regenerate or customize the downloadable CV:

```bash
python generate_cv.py
```

### 4. Run the Application

```bash
python app.py
```

The web server will start at `http://127.0.0.1:5000/`.

---

## ⚙️ Environment Variables (Optional)

Configure email credentials to receive direct email alerts on form submission:

| Variable | Description | Default |
|---|---|---|
| `EMAIL_PASS` | Gmail App Password for SMTP authentication | *None (saves locally)* |
| `MAIL_USERNAME` | Sender email address | `wantech010@gmail.com` |
| `MAIL_RECIPIENT` | Recipient email address | `sushilyogi56@gmail.com` |
| `SECRET_KEY` | Flask session secret key | *Development key* |
| `PORT` | Web server port | `5000` |

---

## 🧪 Running Tests

Execute the automated test suite:

```bash
python -m unittest discover tests
```

---

## 👤 Author

- **Name**: Sushil Nath Yogi
- **Email**: [sushilyogi56@gmail.com](mailto:sushilyogi56@gmail.com)
- **GitHub**: [@Sushil680](https://github.com/Sushil680)
- **LinkedIn**: [linkedin.com/in/sushil-yogi](https://www.linkedin.com/in/sushil-yogi/)
