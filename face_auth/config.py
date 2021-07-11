# -------------------------------------- profile_detection ---------------------------------------
detect_frontal_face = 'face_auth/profile_detection/haarcascades/haarcascade_frontalface_alt.xml'
detect_perfil_face = 'face_auth/profile_detection/haarcascades/haarcascade_profileface.xml'

# -------------------------------------- emotion_detection ---------------------------------------
path_model = 'face_auth/emotion_detection/Models/model_dropout.hdf5'
w,h = 48,48
rgb = False
labels = ['angry','disgust','fear','happy','neutral','sad','surprise']


EYE_AR_THRESH = 0.23 #baseline
EYE_AR_CONSEC_FRAMES = 1

eye_landmarks = "face_auth/blink_detection/model_landmarks/shape_predictor_68_face_landmarks.dat"
