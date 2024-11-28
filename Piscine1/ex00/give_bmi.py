import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """주어진 신장(height)과 체중(weight)을 통해 각각의 BMI를 계산하여
    numpy 배열로 반환합니다."""
    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)
    if height_array.size != weight_array.size:
        raise ValueError("Height and weight lists must be of the same length.")
    bmi_array = weight_array / (height_array**2)
    return bmi_array


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """BMI numpy 배열과 제한값(limit)을 받아 제한을 초과하는 경우 True,
    그렇지 않으면 False를 반환하는 numpy 배열을 생성합니다."""
    return bmi > limit
