import streamlit as st
from PIL import Image
import io

def resize_image(image, width, height):
    # Use LANCZOS filter for high-quality resizing
    return image.resize((width, height), Image.LANCZOS)

def main():
    # Title and header
    st.title("📷 Image Resizer Tool")
    st.markdown("""
    Upload an image and resize it easily. Adjust the dimensions to your preference and download the resized image.
    """)

    # Upload image 
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"], label_visibility="collapsed")
    
    if uploaded_file is not None:
        # Open and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        # Styling for Resize options
        st.sidebar.header("🔧 Resize Options")
        st.sidebar.markdown("""
        Use the sliders to resize the image. The default size is the current dimensions of the uploaded image.
        """)
        
        # sliders for resizing
        width = st.sidebar.slider("Width", min_value=1, max_value=2000, value=image.width, step=1)
        height = st.sidebar.slider("Height", min_value=1, max_value=2000, value=image.height, step=1)
        
        # Resize image based on the slider values
        resized_image = resize_image(image, width, height)
        
        # Show resized image 
        st.subheader("🖼 Resized Image")
        st.image(resized_image, caption="Resized Image", use_container_width=True)
        
        # Save resized image 
        buffered = io.BytesIO()
        resized_image.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()
        
        # download button
        st.sidebar.markdown("---")
        st.sidebar.download_button(
            label="⬇️ Download Resized Image",
            data=img_bytes,
            file_name="resized_image.png",
            mime="image/png",
            use_container_width=True
        )

if __name__ == "__main__":
    main()
