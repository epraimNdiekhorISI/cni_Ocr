import cv2
from app.preprocessing.image_processor import preprocess_image


def test_preprocess_image_returns_valid_array(sample_image_path):
    result = preprocess_image(sample_image_path)
    assert result is not None
    assert result.ndim in (2, 3)          # image niveaux de gris ou couleur
    assert result.shape[0] > 0 and result.shape[1] > 0


def test_preprocess_image_improves_contrast(sample_image_path):
    original = cv2.imread(sample_image_path, cv2.IMREAD_GRAYSCALE)
    processed = preprocess_image(sample_image_path)
    assert processed.std() >= original.std() * 0.8