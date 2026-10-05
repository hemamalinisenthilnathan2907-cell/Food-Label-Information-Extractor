import streamlit as st
from PIL import Image

from ocr import extract_text
from embedding import create_embeddings
from attention import calculate_attention
from extractor import extract_information

st.set_page_config(
    page_title="Food Label Information Extractor",
    page_icon="🍱",
    layout="wide"
)

st.title("🍱 Food Label Information Extractor")

st.write(
    "Upload a food product label image to extract "
    "information using OCR, Embedding and Attention Mechanism."
)

uploaded_file = st.file_uploader(
    "Upload Food Label Image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file)

    st.subheader("🖼️ Uploaded Image")

    st.image(
        image,
        caption="Food Label",
        use_container_width=True
    )

    if st.button(
        "🔍 Extract Food Information",
        type="primary"
    ):

        with st.spinner(
            "Reading food label using OCR..."
        ):

            text = extract_text(image)


        st.subheader("📄 OCR Extracted Text")

        if text.strip():

            st.text_area(
                "Detected Text",
                text,
                height=250
            )

        else:

            st.error(
                "No text could be detected from the image."
            )

            st.stop()

        with st.spinner(
            "Creating text embeddings..."
        ):

            sentences, embeddings = create_embeddings(
                text
            )


        st.subheader("🔢 Text Embedding")

        if embeddings is not None:

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Number of Text Lines",
                    len(sentences)
                )

            with col2:

                st.metric(
                    "Embedding Dimension",
                    embeddings.shape[1]
                )

            st.success(
                "OCR text successfully converted "
                "into numerical embeddings."
            )

        with st.spinner(
            "Calculating attention scores..."
        ):

            attention_result = calculate_attention(
                embeddings
            )


        st.subheader("🧠 Attention Mechanism")

        if attention_result is not None:

            attention_weights, attention_output, importance_scores = (
                attention_result
            )

            st.write(
                "The attention score represents the "
                "relative importance of each extracted text line."
            )

            for sentence, score in zip(
                sentences,
                importance_scores
            ):

                st.write(
                    f"**{sentence}**  →  "
                    f"Attention Score: `{score:.4f}`"
                )

        with st.spinner(
            "Extracting food information..."
        ):

            information = extract_information(
                text
            )


        st.subheader("📋 Food Information")

        if information["weight"]:

            st.write(
                "⚖️ **Weight:** "
                + ", ".join(
                    information["weight"]
                )
            )

        else:

            st.write(
                "⚖️ **Weight:** Not detected"
            )

        if information["calories"]:

            st.write(
                "🔥 **Calories:** "
                + ", ".join(
                    information["calories"]
                )
            )

        else:

            st.write(
                "🔥 **Calories:** Not detected"
            )

        if information["dates"]:

            st.write(
                "📅 **Dates:** "
                + ", ".join(
                    information["dates"]
                )
            )

        else:

            st.write(
                "📅 **Dates:** Not detected"
            )

        if information["protein"]:

            st.write(
                "💪 **Protein:** "
                + ", ".join(
                    information["protein"]
                )
            )

        else:

            st.write(
                "💪 **Protein:** Not detected"
            )

        if information["fat"]:

            st.write(
                "🥑 **Fat:** "
                + ", ".join(
                    information["fat"]
                )
            )

        else:

            st.write(
                "🥑 **Fat:** Not detected"
            )

        if information["carbohydrates"]:

            st.write(
                "🍞 **Carbohydrates:** "
                + ", ".join(
                    information["carbohydrates"]
                )
            )

        else:

            st.write(
                "🍞 **Carbohydrates:** Not detected"
            )

        st.write("🥗 **Ingredients:**")

        if information["ingredients"]:

            for ingredient in information["ingredients"]:

                st.write(
                    f"- {ingredient}"
                )

        else:

            st.write(
                "Ingredients section not detected."
            )

        st.success(
            "✅ Food label analysis completed successfully!"
        )
