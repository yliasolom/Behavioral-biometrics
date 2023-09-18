# MANUAL:
1. CLONE this repo
1. INSTALL  `pip install git+https://github.com/paoloripamonti/face-recognition` - maybe there might be some troubles, in this case just clone this repo
2. DOWNLOAD weights to folder weights/ by this link: [model.pkl](https://drive.google.com/file/d/1-FCShfmCxACnNUySTAHCRpkGo_ExXMz2/view?usp=sharing)
3. FOR prediction run `python src/predict.py` with path to image --image-path [my_testing.jpg](https://i.pinimg.com/originals/9e/1c/c9/9e1cc9329b82ad0084d5c4c30757d469.jpg)

  see example in notebook how it might work



# Behavioral-biometrics
Person identification of gait and related factors in behavioral biometrics

### Team:
- Kirill Sheshulin
- Kirill Zarubin
- Nikita Shubny
- Julia Solomennikowa

Visual surveillance has exponentially increased the growth of security devices and systems in the digital era. Gait- and face-recognition-based person identification is an emerging biometric modality for automatic visual surveillance and monitoring as the walking patterns highly correlate to the subject’s identity. The scientific research on person identification using gait and low-resolution face has grown dramatically over the past two decades due to its several benefits. It does not require active collaboration from users and can be performed without their cooperation.

A face and & identification program intended to detect & identify faces from pictures that are of size 30x30 pixels using EDSR image super-resolution, whereas gait recognition
The input for gait recognition is a set of silhouettes (there are NOT ANY constrains on an input, which means it can contain any number of non-consecutive silhouettes filmed under different viewpoints with different walking conditions).

```mermaid
flowchart LR

subgraph Preprocessing
  A((Видео))
  B((YOLO))
  A --> B
end

subgraph "Процессинг кадров" 
  B --> C(Нарезание кадров)
  C --> D(Маска силуэта)
end

subgraph "Распознавание по походке"
  D --> E(GaitRecognition)
end

subgraph "Идентификация по лицу"
  D --> G(FaceRecognition)
end

subgraph "Совместная обработка"
  E --> H((Weighted Average))
  G --> H
end

H --> J((Personal ID))





