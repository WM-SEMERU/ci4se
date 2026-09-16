def get_image_output(self):
    saved_image = self.workflow.exported_image_sequence[-1].get('path')
    image_name = get_image_upload_filename(self.workflow.
        exported_image_sequence[-1], self.workflow.builder.image_id, self.
        platform)
    metadata = self.get_output_metadata(saved_image, image_name)
    output = Output(file=open(saved_image), metadata=metadata)
    return metadata, output