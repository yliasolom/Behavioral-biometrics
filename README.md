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

flowchart LR

subgraph Preprocessing
  A((Видео))
  B((Маска силуэта))
  A --> B
end

subgraph "Распознавание по походке"
  B --> C{silhouette score}
  C --> D(Модуль 1)
end

subgraph "Идентификация по лицу"
  B --> E(YOLO)
  E --> F(Модуль 2)
end

subgraph "Совместная обработка"
  D --> G(Результат 1)
  F --> G
  G --> H(Weighted Average)
end

H --> I((Personal ID))




