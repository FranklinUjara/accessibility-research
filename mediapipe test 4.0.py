import cv2
import mediapipe as mp
import csv

# Function to flatten landmark data


def extract_landmark_data(landmarks):
    data = []
    for landmark in landmarks:
        # Append x, y, z coordinates
        data += [landmark.x, landmark.y, landmark.z]
    return data


# Create a MediaPipe Holistic instance
mp_holistic = mp.solutions.holistic

# Prepare Drawing Utilities
mp_drawing = mp.solutions.drawing_utils

# Prepare DrawingSpec for landmarks and connections
landmark_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
connection_drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)

# Load the video
cap = cv2.VideoCapture("video.mp4")

# Frame counter
frame_number = 0

# List to store landmarks of each frame
data = []

with mp_holistic.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.8) as holistic:
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break  # Exit the loop if the video is over

        # Recolor Feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False    # Make the image unwritable to save resources

        # Make Detections
        results = holistic.process(image)

        # Extract landmarks
        if results.face_landmarks is not None:
            face_landmarks = results.face_landmarks.landmark
            face_data = extract_landmark_data(face_landmarks)
        else:
            face_data = []

        if results.pose_landmarks is not None:
            pose_landmarks = results.pose_landmarks.landmark
            pose_data = extract_landmark_data(pose_landmarks)
        else:
            pose_data = []

        # Flatten landmarks and append frame data to list
        data.append(
            {'frame': frame_number, 'face': face_data, 'pose': pose_data})

        frame_number += 1

        # Recolor image back to BGR for rendering
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw face landmarks
        mp_drawing.draw_landmarks(image, results.face_landmarks,
                                  mp_holistic.FACEMESH_TESSELATION, landmark_drawing_spec, connection_drawing_spec)

        # Pose Detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks,
                                  mp_holistic.POSE_CONNECTIONS, landmark_drawing_spec, connection_drawing_spec)

        cv2.imshow('MediaPipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

# Write data to CSV file
with open('landmarks.csv', 'w', newline='') as csvfile:
    fieldnames = ['frame', 'face', 'pose']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)
