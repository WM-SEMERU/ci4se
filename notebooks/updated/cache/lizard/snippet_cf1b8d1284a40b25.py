def version(self):
    url = 'http://{master_addr}:{master_port}/dir/status'.format(master_addr
        =self.master_addr, master_port=self.master_port)
    data = self.conn.get_data(url)
    response_data = json.loads(data)
    return response_data.get('Version')