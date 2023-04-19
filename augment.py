import cv2
# given a input low res high res image pair, augment both to generate more training data

def create_dataset(lr, hr):
    # lr: low resolution image
    # hr: high resolution image (goal image size not ground truth)
    # return: a list of augmented low res and high res image pairs
    rotateCodes=[cv2.ROTATE_180,
    cv2.ROTATE_90_COUNTERCLOCKWISE,
    cv2.ROTATE_90_CLOCKWISE]
    images=[(lr,hr)]
    for rotate in rotateCodes:
        lr_rotated = cv2.rotate(lr, rotate)
        hr_rotated = cv2.rotate(hr, rotate)
        images.append((lr_rotated, hr_rotated))
        images.append((cv2.flip(lr_rotated,1),cv2.flip(hr_rotated,1)))
        images.append((cv2.flip(lr_rotated,0),cv2.flip(hr_rotated,0)))

    return images