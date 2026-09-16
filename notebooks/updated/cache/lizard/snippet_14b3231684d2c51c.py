def get_error_messages(self):
    try:
        error_elms = self.get_elms(class_name='error')
    except NoSuchElementException:
        return []
    else:
        try:
            error_values = [error_elm.get_attribute('error') for error_elm in
                error_elms]
        except Exception:
            error_values = [error_elm.text for error_elm in error_elms]
        finally:
            return error_values