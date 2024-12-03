import emoji
import re
from Dictionaries import arabic_dict, num_dict, sign_dict, emoji_dict, english_dict


class TextPreprocessor:
    def __init__(self):
        self.arabic_dict = arabic_dict
        self.num_dict = num_dict
        self.sign_dict = sign_dict

        self.emoji_dict = emoji_dict
        self.english_dict = english_dict

    def find_emoji(self, df):
        for index, row in df['Comment'].items():
            if any(char in emoji.EMOJI_DATA for char in row):
                continue

            if len(row.strip()) < 3:
                continue
        return df

    def remove_url(self, text):
        # Remove links
        text = re.sub('http[s]?://\S+', '', text)
        return text

    def remove_elements(self, text):
        if isinstance(text, float):
            return ''

        # Remove mentions followed by dot
        text = re.sub(r'@(\w+\.)*\w+', '', text)

        # Remove mentions
        text = re.sub(r'@\w+', '', text)

        # Remove hashtags
        text = re.sub(r'#\w+', '', text)

        # Remove newline characters in one line
        text = text.replace('\n', ' ')

        # Remove multiple space characters
        text = re.sub('\s+', ' ', text)

        # Convert to lowercase
        text = text.lower()

        return text

    def separate_cases(self, text):
        if len(text) <= 1:
            return ' '
        new_text = ""
        last_char_all_num = text[0].isalnum()

        for char in text:
            if char.isalnum() != last_char_all_num and char.isalnum():
                new_text += " " + char
            else:
                new_text += char

            last_char_all_num = char.isalnum()
        return new_text

    def remove_consecutive_duplicates(self, text):
        # Remove three consecutive duplicates
        pattern = r'(\w)\1{1,}'
        return re.sub(pattern, r'\1\1', text)

    def pre_process(self, text):
        text = text.lower()

        dictionaries = [self.emoji_dict,
                        self.sign_dict,
                        self.arabic_dict,
                        self.num_dict,
                        self.english_dict,
                        ]
        for dictionary in dictionaries:
            for key, value in dictionary.items():
                text = re.sub(
                    re.escape(key),
                    value,
                    text
                )

        for emoji_text, emojis in emoji_dict.items():
            text = re.sub(re.escape(emoji_text), emojis, text)

        for sign, signs in sign_dict.items():
            text = re.sub(re.escape(sign), signs, text)

        for arabic, persian in arabic_dict.items():
            text = re.sub(re.escape(arabic), persian, text)

        for num, nums in num_dict.items():
            text = re.sub(re.escape(num), nums, text)

        for english_name, english_names in english_dict.items():
            text = re.sub(re.escape(english_name), english_names, text)

        text = re.sub("\s+", ' ', text)

        text = text.strip()
        return text

    def process_column(self, column):
        column = column.apply(self.remove_elements)
        column = column.apply(self.remove_url)
        column = column.apply(self.separate_cases)
        column = column.apply(self.remove_consecutive_duplicates)
        column = column.apply(self.pre_process)
        return column
