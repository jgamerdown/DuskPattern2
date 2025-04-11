from ultralytics import YOLO
from PIL import Image


def get_pred_img(model: YOLO, img_path, save_dir):
    results = model(img_path)
    for result in results:
        im_array = result.plot()
        im = Image.fromarray(im_array[..., ::-1])
        # im.show()
        im.save(f'{save_dir}/results.jpg')


def get_text_bboxes(model: YOLO, img_path):
    results = model(img_path)

    filtered_boxes = []
    for result in results:
        for box in result.boxes:
            if box.cls == 4 or box.cls == 6:
                filtered_boxes.append(box.xyxy)

    return filtered_boxes
