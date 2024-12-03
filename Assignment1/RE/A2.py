import re

text = """
پیامبر اسلام (ص) به مکه آمد. امام خمینی (ره) در سال ۱۳۵۷ انقلاب کرد (یا شاید هم این طور نیست).(مثلاً) این واقعه (ع) در سال (ق.م) (ب.م) اتفاق افتاد (رضوان الله تعالی علیه). او در سال ۱۳۶۰ (س) درگذشت.
"""

# Define the regex pattern for abbreviations and phrases
pattern = r'\((?:[\u0600-\u06FF]{1,3}(?:\.[\u0600-\u06FF]{1,3})?|(?:ص|عج?|ره|ق\.م|ه\.ق|ه\.ش|س|رضوان الله تعالی علیه|رهی))\)'
# Find all matches in the text
matches = re.findall(pattern, text)

# Print results
for match in matches:
    print(match)
