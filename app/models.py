# -*- coding: utf-8 -*-
__author__ = 'kbson'
__blog__ = 'https://www.along.party'
__email__ = 'kbsonlong@gmail.com'

from app import db
from hashlib import md5


followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)
    followed = db.relationship('User',
                               secondary = followers,
                               primaryjoin = (followers.c.follower_id == id ),
                               secondaryjoin = (followers.c.followed_id == id),
                               backref = db.backref('followers',lazy = 'dynamic'),
                               lazy = 'dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    ##头像处理
    def avatar(self, size):
        return 'http://www.gravatar.com/avatar/' + md5(self.email.encode("utf8")).hexdigest() + '?&s=' + str(size)

    def __repr__(self):
        return '<User %r>' % (self.nickname)


    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() == None:
            return nickname
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname=new_nickname).first() == None:
                break
            version += 1
        return new_nickname
    """
        make_unique_nickname 这种方法简单地增加一个计数器为请求的昵称，直到找到一个唯一的名称。例如，如果用户名 “miguel”已经存在，
        这个方法将会建议使用 “miguel2”，如果这个还是存在，将会建议使用 “miguel3”，依次下去直至找到唯一的用户名。
        需要注意的是我们把这个方法作为一个静态方法，因为这种操作并不适用于任何特定的类的实例。
    """

    ###添加移除关注者
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
            return self

    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
            return self

    def is_following(self, user):
        return self.followed.filter(followers.c.followed_id == user.id).count() > 0

    def followed_posts(self):
        post_list = Post.query.join(followers, (followers.c.followed_id == Post.user_id)).filter(
            followers.c.follower_id == self.id).order_by(Post.timestamp.desc())
        return post_list




class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)