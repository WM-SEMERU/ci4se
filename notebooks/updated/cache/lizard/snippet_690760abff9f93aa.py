def brightness(sequence_number, brightness):
    return MessageWriter().string('brightness').uint64(sequence_number).uint8(
        int(brightness * 255)).get()