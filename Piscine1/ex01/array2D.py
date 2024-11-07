import numpy as np

def slice_me(family: list, start: int, end: int) -> np.ndarray:
    """
    주어진 2D 배열의 shape를 출력하고, 지정된 start와 end 인덱스에 따라 슬라이싱한 새 배열을 반환합니다.
    """
    # 입력이 2D 배열인지 확인
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise ValueError("Input must be a 2D list.")

    # 각 행의 길이가 같은지 확인
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All rows in the 2D array must have the same length.")
    
    # numpy 배열로 변환
    family_array = np.array(family)

    # 배열의 초기 크기 출력
    print(f"My shape is : {family_array.shape}")

    # 슬라이싱 수행
    sliced_array = family_array[start:end]

    # 슬라이싱 후 크기 출력
    print(f"My new shape is : {sliced_array.shape}")
    
    return sliced_array