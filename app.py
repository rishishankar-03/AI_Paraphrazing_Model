import streamlit as st
from transformers import PegasusTokenizer, PegasusForConditionalGeneration, pipeline
from nltk.tokenize import PunktSentenceTokenizer
import nltk
import torch

# Set page config as the very first Streamlit command
st.set_page_config(page_title="AI Text Humanizer", layout="centered")

# Download NLTK punkt tokenizer
nltk.download('punkt')

# Load the Pegasus model and tokenizer with caching
@st.cache_resource
def load_model():
    tokenizer = PegasusTokenizer.from_pretrained("tuner007/pegasus_paraphrase")
    model = PegasusForConditionalGeneration.from_pretrained("tuner007/pegasus_paraphrase")
    device = 0 if torch.cuda.is_available() else -1
    paraphrase_pipeline = pipeline('text2text-generation', model=model, tokenizer=tokenizer, device=device)
    return paraphrase_pipeline

nlp = load_model()

st.title("🤖 AI Text Humanizer")
st.write("Paste AI-generated or robotic text below. We'll make it sound more human-like.")

user_input = st.text_area("Enter paragraph here:", height=200)

if st.button("Paraphrase"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        # Sentence tokenization
        sentence_tokenizer = PunktSentenceTokenizer()
        sentences = sentence_tokenizer.tokenize(user_input)

        max_len = nlp.tokenizer.model_max_length
        st.info("Paraphrasing... Please wait.")
        paraphrased_sentences = []

        for sentence in sentences:
            # Tokenize sentence and truncate if too long
            tokens = nlp.tokenizer.tokenize(sentence)
            if len(tokens) > max_len:
                tokens = tokens[:max_len]
                truncated_sentence = nlp.tokenizer.convert_tokens_to_string(tokens)
            else:
                truncated_sentence = sentence

            # Generate paraphrase
            result = nlp(truncated_sentence, max_length=100, num_return_sequences=1, truncation=True)
            paraphrased_sentences.append(result[0]['generated_text'])

        final_output = ' '.join(paraphrased_sentences)

        st.success("Here is the paraphrased (human-like) version:")
        st.text_area("Output:", value=final_output, height=200)
