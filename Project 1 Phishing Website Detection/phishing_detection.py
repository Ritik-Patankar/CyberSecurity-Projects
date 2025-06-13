import re
import pandas as pd

# Rule-based phishing detection function
def is_phishing_url(url):
    rules = [
        r"http[s]?://[0-9.]+",             # IP address in URL
        r"@+",                             # @ symbol in URL
        r"-",                              # Hyphens in domain
        r"//.*//",                         # Multiple redirects
        r"https?://(www\.)?[^.]*\.co",     # Common fake TLDs
        r"https?://(www\.)?[^.]*\.tk",     # Cheap/free domain
    ]
    
    for rule in rules:
        if re.search(rule, url):
            return "Phishing"
    return "Legit"

# Sample URLs
urls = [
    "http://192.168.0.1/login",
    "https://secure-login.com@evil.com",
    "https://your-bank-login.tk",
    "https://www.google.com",
    "https://paypal-login.com",
    "http://www.goodsite.com"
]

# Create DataFrame
df = pd.DataFrame(urls, columns=["URL"])
df["Result"] = df["URL"].apply(is_phishing_url)

# Output
print(df)
