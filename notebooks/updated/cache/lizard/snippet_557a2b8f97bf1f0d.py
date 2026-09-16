def delete(self, url):
    try:
        res = requests.delete(url, headers=self.headers)
        return json.loads(res.text)
    except Exception as e:
        print(e)
        return 'error'