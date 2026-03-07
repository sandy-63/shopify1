# Shopify Automation

Selenium-based automation to search a product on a Shopify store and add it to the cart.

---

## Project Structure

```
shopify-automation/
│
├── src/
│   └── main.py          # automation script
│
├── tests/
│   └── test.py          # test cases
│
├── requirements.txt     # project dependencies
└── report.txt           # test run logs
```

---

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/your-username/shopify-automation.git
cd shopify-automation
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Make sure ChromeDriver is installed and matches your Chrome version**
- Download from: https://chromedriver.chromium.org/downloads

---

## Running the Automation Script

```bash
python src/main.py
```

---

## Running Tests

Run tests and print results in terminal:
```bash
python -m pytest tests/test.py -v
```

Run tests and save results to report.txt:
```bash
python -m pytest tests/test.py -v >> report.txt
```
