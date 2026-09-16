def initdb():
    from plnt.database import Blog, session
    make_app().init_database()
    blogs = [Blog('Armin Ronacher', 'http://lucumr.pocoo.org/',
        'http://lucumr.pocoo.org/cogitations/feed/'), Blog('Georg Brandl',
        'http://pyside.blogspot.com/',
        'http://pyside.blogspot.com/feeds/posts/default'), Blog(
        'Ian Bicking', 'http://blog.ianbicking.org/',
        'http://blog.ianbicking.org/feed/'), Blog('Amir Salihefendic',
        'http://amix.dk/', 'http://feeds.feedburner.com/amixdk'), Blog(
        'Christopher Lenz', 'http://www.cmlenz.net/blog/',
        'http://www.cmlenz.net/blog/atom.xml'), Blog('Frederick Lundh',
        'http://online.effbot.org/', 'http://online.effbot.org/rss.xml')]
    for blog in blogs:
        session.add(blog)
    session.commit()
    click.echo(
        'Initialized database, now run manage-plnt.py sync to get the posts')