import streamlit as st
import cv2
import numpy as np
from PIL import Image

@st.cache()
def get_thresh(image):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh_result, thresh_image = cv2.threshold(
        image_gray, 
        0, 255, 
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU 
    )
    return thresh_image

@st.cache()
def get_contours(thresh_img):
    mode = cv2.RETR_TREE
    method = cv2.CHAIN_APPROX_NONE
    contours, hierarchy = cv2.findContours(
        image=thresh_img,
        mode=mode,
        method=method
    )
    return contours

@st.cache()
def count_dots(contours, card):
    xs = np.array([contour.shape[0] for contour in contours])
    
    if len(contours)==2 or np.std(xs)<2:
        return 0

    # Where the input image is only one card
    if card == 'Single':
        xs_mean = np.mean(xs)
        xs_dot = xs[xs < xs_mean]

    # Use the tolerance value if the input image is more than one card
    else:
        tolerance = 3
        most_freq = max(set(list(xs)), key=list(xs).count)
        dot_ranges = range(most_freq, most_freq+tolerance)
        xs_dot = [x_dot for x_dot in xs if x_dot in dot_ranges]

    return len(xs_dot)

st.title('Dot Counter')

st.sidebar.title('Menu')

app_mode = st.sidebar.selectbox(
    'Choose the app menu',
    ['Run the app', 'About app']
)

if app_mode == 'About app':
    st.markdown('This web app implements a docker image that contains a program to count the number of domino points.')

elif app_mode == 'Run the app':
    st.sidebar.markdown('---')
        
    st.markdown("**Detected Dots**")
    dots_text = st.markdown(
        f"<h1 style='text-align: center; color: red;'>{None}</h1>", 
        unsafe_allow_html=True
    )
    st.markdown('---')

    card = st.sidebar.radio(
        "How many cards do you want to upload",
        ('Single', 'Multiple')
    )

    st.sidebar.markdown('---')

    img_file_buffer = st.sidebar.file_uploader(
        "Upload an image", 
        type=[ "jpg", "jpeg",'png']
    )
    
    if img_file_buffer is not None:
        image = np.array(Image.open(img_file_buffer))
        st.sidebar.text('Original Image')
        st.sidebar.image(image)
    
        # Dashboard
        thresh_image = get_thresh(image)
        contours = get_contours(thresh_image)
        dots = count_dots(contours, card)

        dots_text.write(
            f"<h1 style='text-align: center; color: green;'>{dots}</h1>", 
            unsafe_allow_html=True
        )

        st.markdown("**Finding Contours**")
        image_copy = image.copy()
        out_image = cv2.drawContours(
            image=image_copy, 
            contours=contours, 
            contourIdx=-1, 
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_AA
        )
        st.image(out_image,use_column_width= True)