import streamlit as st

def show_home():
    # Embedding CSS for styling the home page at the beginning to avoid redundancy
    st.markdown("""
        <style>
            .stApp {
    background: linear-gradient(to bottom, 
        #dfe6ec,  /* lighter grey-blue */
        #bdc3c7,  /* soft grey */
        #aebbc6,  /* even softer grey */
        #99aab5,  /* very soft blue */
        #dfe6ec); /* repeat the first color for a smooth transition */
}

            h1, h2, h3, .big-font, .stMarkdown {
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            }
            .big-font {
                font-size:20px !important;
                font-weight: bold;
            }
            h1 {
                text-align: center;
            }
            h2 {
                padding-top: 0.5em;
                color: #4a4a4a;
            }
            .text-content, .features-list {
                padding: 10px;
                text-align: justify;
                line-height: 1.5;
            }
            .features-list li {
                margin-bottom: 10px; /* Space between list items */
            }
            .features-list li strong {
                color: #4a4a4a; /* Dark grey color for bold text */
            }
            .stImage, .stVideo {
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .notification {
                padding: 10px;
                background-color: #f8d7da;
                color: #721c24;
                border: 1px solid #f5c6cb;
                border-radius: 4px;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.header('Welcome to Our Object Detection App')
    col1, col2 = st.columns(2)

    with col1:
        st.header("Explore Object Detection with YOLOv8")
        st.markdown("""
            <div class="text-content">
                This app leverages YOLOv8, the latest in the series of YOLO (You Only Look Once) models, known for its exceptional speed and accuracy in real-time object detection. YOLOv8 enhances detection with improved model architectures and training strategies, making it ideal for practical applications in AI.
                Upload your files and witness the AI pinpoint various objects with remarkable precision.
                <br><br>
                <a href="https://github.com/ultralytics/ultralytics" target="_blank">YOLOv8 GitHub Repository</a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image("explore.png", caption="Explore AI", use_column_width=True)

    st.write("---")
    st.header("Features of the App")
    st.image("features.png", caption="App Features", use_column_width=True)
    st.markdown("""
        <div class="text-content">
            <ul class="features-list">
                <li><strong>Image Detection:</strong> Upload images to detect objects.</li>
                <li><strong>YouTube Integration:</strong> Provide a YouTube link to analyze videos directly from YouTube. Pause and take screenshots for image processing in the image option.</li>
                <li><strong>Interactive Results:</strong> View and interact with the image detection results.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.subheader("Get Started")
    st.markdown("""
        <div class="notification">
            Navigate through the sidebar to access the different functionalities of the app. Please note that only the image will be processed for object detection.
        </div>
    """, unsafe_allow_html=True)
    st.image("tumblr_mg4rofgfuY1qc8m6fo1_500.gif", caption="See It in Action", use_column_width=True)

