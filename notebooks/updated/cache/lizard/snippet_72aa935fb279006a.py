def image_to_tf_summary_value(image, tag):
    curr_image = np.asarray(image, dtype=np.uint8)
    height, width, n_channels = curr_image.shape
    if n_channels == 1:
        curr_image = np.reshape(curr_image, [height, width])
    s = io.BytesIO()
    matplotlib_pyplot().imsave(s, curr_image, format='png')
    img_sum = tf.Summary.Image(encoded_image_string=s.getvalue(), height=
        height, width=width, colorspace=n_channels)
    return tf.Summary.Value(tag=tag, image=img_sum)