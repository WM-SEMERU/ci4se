def face_landmarks(face_image, face_locations=None, model='large'):
    landmarks = _raw_face_landmarks(face_image, face_locations, model)
    landmarks_as_tuples = [[(p.x, p.y) for p in landmark.parts()] for
        landmark in landmarks]
    if model == 'large':
        return [{'chin': points[0:17], 'left_eyebrow': points[17:22],
            'right_eyebrow': points[22:27], 'nose_bridge': points[27:31],
            'nose_tip': points[31:36], 'left_eye': points[36:42],
            'right_eye': points[42:48], 'top_lip': points[48:55] + [points[
            64]] + [points[63]] + [points[62]] + [points[61]] + [points[60]
            ], 'bottom_lip': points[54:60] + [points[48]] + [points[60]] +
            [points[67]] + [points[66]] + [points[65]] + [points[64]]} for
            points in landmarks_as_tuples]
    elif model == 'small':
        return [{'nose_tip': [points[4]], 'left_eye': points[2:4],
            'right_eye': points[0:2]} for points in landmarks_as_tuples]
    else:
        raise ValueError(
            "Invalid landmarks model type. Supported models are ['small', 'large']."
            )