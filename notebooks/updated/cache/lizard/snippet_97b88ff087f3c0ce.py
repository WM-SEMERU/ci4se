def map_images_in_tex(tex_files, image_mapping, output_directory, context=False
    ):
    extracted_image_data = []
    for tex_file in tex_files:
        partly_extracted_image_data = extract_captions(tex_file,
            output_directory, image_mapping.keys())
        if partly_extracted_image_data:
            cleaned_image_data = prepare_image_data(partly_extracted_image_data
                , output_directory, image_mapping)
            if context:
                extract_context(tex_file, cleaned_image_data)
            extracted_image_data.extend(cleaned_image_data)
    return extracted_image_data