def images():
    if request.method == 'POST':
        file_upload = request.files['file']
        if file_upload:
            image = dict()
            image['filename'] = secure_filename(file_upload.filename)
            full_path = os.path.join(session['img_input_dir'], image[
                'filename'])
            file_upload.save(full_path)
            image['uid'] = session['image_uid_counter']
            session['image_uid_counter'] += 1
            current_app.logger.debug('File %d is saved as %s', image['uid'],
                image['filename'])
            session['image_list'].append(image)
            return jsonify(ok='true', file=image['filename'], uid=image['uid'])
        return jsonify(ok='false')
    if request.method == 'GET':
        return jsonify(images=session['image_list'])