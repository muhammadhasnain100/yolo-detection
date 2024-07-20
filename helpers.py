from PIL import ImageDraw, ImageFont
import yt_dlp
from ultralytics import YOLO
def get_youtube_stream_url(youtube_url):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'no_warnings': True,
            'quiet': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            return info['url']
    except Exception as e:
        return None

# Function to load the model
def load_model():
    # Load YOLO model
    return YOLO("yolov8n.pt")

# Function to perform prediction and visually annotate the image
def predict_and_annotate(model, image):
    results = model(image)
    detected_class_indices = results[0].boxes.cls.cpu().numpy().astype(int)
    detected_class_names = [results[0].names[i] for i in detected_class_indices]
    bounding_boxes = results[0].boxes.xyxy.cpu().numpy()

    draw = ImageDraw.Draw(image)
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
    font = ImageFont.truetype(font_path, 50)
    colors = ["red", "blue", "green", "yellow", "purple", "black"]

    for i, (class_name, bbox) in enumerate(zip(detected_class_names, bounding_boxes)):
        color = colors[i % len(colors)]
        draw.rectangle([bbox[0], bbox[1], bbox[2], bbox[3]], outline=color, width=5)
        text_size = draw.textsize(class_name, font=font)
        draw.text((bbox[0], bbox[1] - text_size[1]), class_name, fill=color, font=font)

    return image

