import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
from PIL import Image
from ultralytics import YOLO
import random
import io

app = FastAPI()
# model = YOLO("/models/currencymodel.pt")
model = YOLO("/app/models/currencymodel.pt")
classes = list(model.names.values())


def annotate_image(image, results):
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0]
        cls_id = int(box.cls[0])
        label = f"{results[0].names[cls_id]}"
        color = class_colors[results[0].names[cls_id]]

        cv2.rectangle(image, (x1, y1), (x2, y2), color, 3)

        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 4, 2)
        cv2.rectangle(image, (x1, y1 - h - 10), (x1 + w, y1), color, -1)
        cv2.putText(
            image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 0), 2
        )

    return image


def generate_colors(num_colors):
    return [tuple(random.randint(0, 255) for _ in range(3)) for _ in range(num_colors)]


class_colors = {
    cls: color for cls, color in zip(classes, generate_colors(len(classes)))
}


@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <html>
        <head>
            <title>Jordanian Currency Detection Model</title>
        </head>
        <body>
            <h1>Jordanian Currency Detection Model</h1>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept="image/*">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """
    return HTMLResponse(content=content)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    results = model(image_cv)
    annotated_image = annotate_image(image_cv, results)
    annotated_image_pil = Image.fromarray(
        cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    )
    img_byte_arr = io.BytesIO()
    annotated_image_pil.save(img_byte_arr, format="JPEG")
    img_byte_arr.seek(0)

    return StreamingResponse(
        img_byte_arr,
        media_type="image/jpeg",
        headers={"Content-Disposition": "attachment; filename=annotated_image.jpg"},
    )
