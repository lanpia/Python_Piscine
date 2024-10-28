#!/bin/bash

# 패키지 이름과 버전 설정
PACKAGE_NAME="ft_package"
PACKAGE_VERSION="0.0.1"

# 작업 디렉토리 설정
WORK_DIR="ex09"
PACKAGE_DIR="$WORK_DIR/$PACKAGE_NAME"
DIST_DIR="$WORK_DIR/dist"

# 작업 디렉토리와 패키지 디렉토리 생성
mkdir -p "$PACKAGE_DIR"

# main.py 파일 생성
cat << EOF > "$PACKAGE_DIR/main.py"
def count_in_list(items, target):
    \"\"\"
    주어진 리스트에서 특정 요소(target)의 개수를 반환합니다.
    \"\"\"
    return items.count(target)
EOF

# __init__.py 파일 생성
cat << EOF > "$PACKAGE_DIR/__init__.py"
from .main import count_in_list
EOF

# README.md 파일 생성
cat << EOF > "$WORK_DIR/README.md"
# ft_package

A sample test package for counting items in a list.

## Usage
\`\`\`python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 출력: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 출력: 0
\`\`\`
EOF

# LICENSE 파일 생성
cat << EOF > "$WORK_DIR/LICENSE"
MIT License
EOF

# pyproject.toml 파일 생성
cat << EOF > "$WORK_DIR/pyproject.toml"
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "$PACKAGE_NAME"
version = "$PACKAGE_VERSION"
description = "A sample test package for counting items in a list."
authors = [{name = "Your Name", email = "your_email@example.com"}]
dependencies = []
EOF

# 빌드 디렉토리로 이동
cd "$WORK_DIR"

# 빌드 도구 설치 (필요한 경우)
pip install --upgrade build > /dev/null

# 패키지 빌드
python -m build

# 패키지 설치
pip install "$DIST_DIR/${PACKAGE_NAME}-${PACKAGE_VERSION}-py3-none-any.whl"

# 설치 확인 및 테스트
echo "패키지가 설치되었습니다. 테스트를 시작합니다."

python3 - << EOF
from ft_package import count_in_list

# 테스트 코드 실행
print(count_in_list(["toto", "tata", "toto"], "toto"))  # Expected output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Expected output: 0
EOF

# 패키지 정보 확인
pip show -v "$PACKAGE_NAME"

echo "패키지 빌드, 설치 및 테스트가 완료되었습니다."
