import streamlit as st
from transformers import MT5ForConditionalGeneration, MT5Tokenizer

# Set page configuration
st.set_page_config(
    page_title="English to Persian Translator",
    page_icon="🌍",
    layout="centered"
)

# Cache the model and tokenizer so they load only once
@st.cache_resource
def load_model_and_tokenizer():
    model_size = "large"
    model_name = f"persiannlp/mt5-{model_size}-parsinlu-translation_en_fa"
    tokenizer = MT5Tokenizer.from_pretrained(model_name, legacy=False)
    model = MT5ForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

# Display a spinner while the model loads
with st.spinner("Loading model..."):
    tokenizer, model = load_model_and_tokenizer()

# After the model is loaded, we proceed with rendering the rest of the app
st.success("Model loaded successfully!")

# Translation function using the preloaded model
def translate(text):
    input_ids = tokenizer.encode(text, return_tensors="pt")
    res = model.generate(input_ids, max_length=512, num_beams=4, early_stopping=True)
    output = tokenizer.batch_decode(res, skip_special_tokens=True, clean_up_tokenization_spaces=False)
    return output[0]

# Sidebar for navigation between pages
page = st.sidebar.selectbox("Choose a page", ["Sentence page", "File page"])
import re  # To help identify timestamps

# Function to simulate translation to "سلام"
if page == "Sentence page":
    st.title("🌍 Sentence Translation Page")

    # Store translations (this will persist across re-runs)
    if 'translations' not in st.session_state:
        st.session_state['translations'] = []

    # Text input box for English sentence
    input_text = st.text_area("Enter the English sentence you want to translate:", "", height=150)

    # Translation button
    translate_button = st.button("Translate", key="translate_button")

    # Clear button
    clear_button = st.button("Clear", key="clear_button")

    # When the "Clear" button is clicked, remove all previous translations
    if clear_button:
        st.session_state['translations'] = []

    # When translate button is clicked, save the sentence and its translation at the top of the list
    if translate_button and input_text:
        translation = translate(input_text)
        st.session_state['translations'].insert(0, {  # Insert at the beginning
            "English": input_text,
            "persian": translation
        })

    # Display all translations stored in the session state in reverse order (newest on top)
    if st.session_state['translations']:
        for entry in st.session_state['translations']:
            st.markdown(f"<div class='english-text'>😄: {entry['English']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='persian-text'><span>🤓: </span> {entry['persian']} </div>", unsafe_allow_html=True)
            st.markdown("<hr>", unsafe_allow_html=True)

# File Page
elif page == "File page":
    st.title("🌍 File Translation Page")

    # File uploader
    uploaded_file = st.file_uploader("Upload an SRT file", type=["srt"])

    # File translation button
    translate_file_button = st.button("Translate File")

    # Regex to detect time stamps
    timestamp_pattern = re.compile(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}")

    # If a file is uploaded and the translation button is clicked
    if uploaded_file is not None and translate_file_button:
        # Read the file and process it (placeholder for actual SRT processing logic)
        srt_content = uploaded_file.read().decode("utf-8")  # Decode bytes to string

        # Initialize an empty list to store the translated content
        translated_lines = []
        extra_translated_lines = []

        # Loop through the SRT file, line by line
        for line in srt_content.splitlines():
            line = line.strip()  # Remove leading/trailing whitespace
            if not line:  # Skip empty lines
                extra_translated_lines.append(line)
            elif line.isdigit():  # Skip digit lines (subtitle index)
                extra_translated_lines.append(line)
            elif timestamp_pattern.match(line):  # Skip time stamp lines
                extra_translated_lines.append(line)
            else:
                # For the content lines, apply translation
                translated_text = translate(line)
                translated_lines.append(f"{line} -> {translated_text}")
        print(translated_lines)
        print(extra_translated_lines)

        # Display translated SRT content
        for line in translated_lines:
            if "->" in line:
                partitioned_line = line.partition("->")
                english_text = partitioned_line[0].strip()
                persian_text = partitioned_line[2].strip()

                st.markdown(f"<div class='english-text'>😄: {english_text}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='persian-text'> <span>🤓: </span> {persian_text}</div>", unsafe_allow_html=True)
            else:
                # For non-translated lines (like digit/timestamp), show as is
                st.markdown(f"<div>{line}</div>", unsafe_allow_html=True)

            st.markdown("<hr>", unsafe_allow_html=True)
