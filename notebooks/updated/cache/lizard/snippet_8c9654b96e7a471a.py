def assign_notification_from_gvm(self, model, prop_name, info):
    if info['method_name'] in ['set_locked_variable'] or info['result'
        ] is Exception:
        return
    if info['method_name'] in ['lock_variable', 'unlock_variable']:
        key = info.kwargs.get('key', info.args[1]) if len(info.args
            ) > 1 else info.kwargs['key']
        if key in self.list_store_iterators:
            gv_row_path = self.list_store.get_path(self.
                list_store_iterators[key])
            self.list_store[gv_row_path][self.IS_LOCKED_AS_STRING_STORAGE_ID
                ] = str(self.model.global_variable_manager.is_locked(key))
    elif info['method_name'] in ['set_variable', 'delete_variable']:
        if info['method_name'] == 'set_variable':
            key = info.kwargs.get('key', info.args[1]) if len(info.args
                ) > 1 else info.kwargs['key']
            if key in self.list_store_iterators:
                gv_row_path = self.list_store.get_path(self.
                    list_store_iterators[key])
                self.list_store[gv_row_path][self.VALUE_AS_STRING_STORAGE_ID
                    ] = str(self.model.global_variable_manager.
                    get_representation(key))
                self.list_store[gv_row_path][self.
                    DATA_TYPE_AS_STRING_STORAGE_ID
                    ] = self.model.global_variable_manager.get_data_type(key
                    ).__name__
                return
        self.update_global_variables_list_store()
    else:
        logger.warning('Notification that is not handled')