def generate_index(self, num_posts=5):
    posts = self.get_posts(num=num_posts)
    self.generate_page('index', template='index.html.jinja', posts=posts)