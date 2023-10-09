# HCI - Accessibility Research

Conducted research on ASL facial expressions using [Mediapipe](https://developers.google.com/mediapipe). Investigated privacy techniques such as dynamic video filters to mask non-essential facial details during sign language data collection. This data can be used to enhance AI models for sign language recognition and translation.

![image 1](https://github.com/franklin-wu-hci/accessibility-research/blob/main/images/image_1.png)
![image 2](https://github.com/franklin-wu-hci/accessibility-research/blob/main/images/image_2.png)
![image 3](https://github.com/franklin-wu-hci/accessibility-research/blob/main/images/image_3.png)

**Note:** Reference video used for this research can be found [here](https://www.youtube.com/@sign-language).

The above images are from the research papers and video materials I referenced for my study on this topic.

## Overview of Research Method
1. Use [Mediapipe](https://developers.google.com/mediapipe) to extract body movement data from the target video to primarily focus on the changes in the facial expressions.
2. Compare the extracted facial data between video learners and instructor, such as through similarity comparisons using this data to support further research on Human-Computer Interaction.
3. Utilize this data for learning-science research.

## Methodology
- Pre-processing for data collection targets: Enhance the clarity of ASL videos, frame interpolation, slow-motion, adjust highlights, shadows, contrast, and sharpness and adjust the confidence interval of Mediapipe code.
  - **Data Collection**
    - Estimate of Sample Size
      - Objective: Determine the number of communication groups videos to capture using Mediapipe to validate our research.
      - Statistical Power: Our goal is to maintain a statistical power typically set at 0.80. This implies that our study has an 80% probability of identifying an effect when it's present.
      - Significance Level: Expected to be 0.05. As we aim to compare facial expressions similarity between teachers and learners, correlation or regression analysis might be employed. Based on these, the required number for a correlation analysis is around 64-85 communication groups, while regression necessitates about 100 groups. For smaller effect sizes, a larger sample might be needed.
  - **Capturing Facial Changes**
    - Method: Utilize Mediapipe to document facial expression variations of both instructors and learners in the videos. Mediapipe establishes 468 landmark points on every face, logging the 3D coordinate positions of each.

  - **Data Analysis**
    - Post-collection Landmark Correction
      - Objective: Rectify any deviation in 3D coordinates due to different face orientations or positions in the video frames.
      - Translation: Adjust the coordinates by subtracting a reference point (e.g., face center or landmark on the nose – landmark No.4) from all other points. This aligns faces to the same frame position.
      - Scaling: Modify the coordinates to standardize a specific distance, correcting for variations caused by varying distances from the camera.
      - Rotation: Implement Procrustes analysis or similar to find the optimal alignment of facial landmarks by translating, scaling, and rotating them.

![image 4](https://github.com/franklin-wu-hci/accessibility-research/blob/main/images/image_4.png)

  - **Evaluating Learning & Imitation Accuracy**
    - Euclidean Distance
      - Compute the Euclidean distance between corresponding landmarks for instructor-learner pairs.
      - Averaging these distances throughout the expression duration will provide similarity measures, with smaller distances suggesting higher resemblance.
    - Temporal Alignment
      - Using Dynamic Time Warping (DTW), synchronize landmark position sequences of both instructors and learners to account for possible expression speed variations.
      - Subsequently, compute the average Euclidean distance.
    - Direction of Movement Analysis
      - Evaluate the movement direction for each landmark across successive frames and compare these between the instructor and learner.
      - Implement cosine similarity to measure the cosine of angles between two vectors, assessing direction accuracy.
