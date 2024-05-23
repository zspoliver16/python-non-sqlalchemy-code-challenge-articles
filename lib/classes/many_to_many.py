# import ipdb
class Article:
    #class that reps article in mag domain
    #has an author, a magazine, an a title
    def __init__(self, author, magazine, title):
        #Initialize the Article instance with an Author instance, a Magazine instance, and a title
        self.title = title
        self.author = author
        self.magazine = magazine

    @property
    def title(self):
        #property that gets and sets the title of the aarticle instance
        return self._title

    @title.setter
    def title(self, value):
        #property setter that sets the title of the article instance
        if isinstance(value, str) and 5 <= len(value) <= 50: #if title is not a string between 5 and 50 chars ling, raise attribute error
            self._title = value
        elif hasattr(self, '_title') and self._title is not None:
            pass
        else:
            raise AttributeError("Article title must be a string between 5 and 50 characters long.")

    @property
    def author(self):
        #property that gets the author of the article instance
        return self._author

    @author.setter
    def author(self, value):
        #property setter that sets the author of the article instance
        if isinstance(value, Author):
            self._author = value
            value._articles_list.append(self)
        elif hasattr(self, '_author') and self._author is not None:
            pass
        else:
            raise AttributeError("Author must be an instance of the Author class.")

    @property
    def magazine(self):
        #propery that gets the magazine the article belongs too
        return self._magazine
# ipdb.set_trace()
    @magazine.setter
    def magazine(self, value):
        #property setter that sets the magazine the article belongs too
        if isinstance(value, Magazine):
            self._magazine = value
            value._articles_list.append(self)
        elif hasattr(self, '_magazine') and self._magazine is not None:
            pass
        else:
            raise AttributeError("Magazine must be an instance of the Magazine class.")



class Author:
    def __init__(self, name):
        #initializde the author instance with a name
        self._name = None
        self._articles_list = []
        self._magazines_list = []
        self.name = name

    @property
    def name(self):
        #property that gets and sets the name of the author
        return self._name

    @name.setter
    def name(self, value):
        #property setter that sets the name of the author
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        elif hasattr(self, '_name') and self._name is not None:
            pass
        else:
            raise AttributeError("Author name must be a non-empty string.")

    def articles(self):
        #get the list of the articles written by the author
        return self._articles_list

    def magazines(self):
        #get the list of magazines the author has contributed too
        return list(set([article.magazine for article in self._articles_list]))

    def add_article(self, magazine, title):
        #add an article written by the author to the magazine
        article = Article(self, magazine, title)
        self._articles_list.append(article)
        return article #returns the article added

    def topic_areas(self):
        if self._articles_list:
            #get the list of topic areas the author has written about
            return list(set([article.magazine.category for article in self._articles_list]))
        else:
            return None


class Magazine:
    def __init__(self, name, category):
        #initialize the magazine instance with anmae and a category
        self._articles_list = []
        self.all = []
        self.name = name
        self.category = category
        self.all.append(self)

    @property
    def name(self):
        #property that gets and sets the name of the magazine
        return self._name

    @name.setter
    def name(self, value):
        #property setter that sets the name of the magazine
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
        elif hasattr(self, '_name') and self._name is not None:
            pass
        else:
            raise AttributeError("Magazine name must be a string between 2 and 16 characters long.")
# ipdb.set_trace()
    @property
    def category(self):
        #property that gets and sets the category of the magazine
        return self._category

    @category.setter
    def category(self, value):
        #property setter that sets the category of the magazine
        if isinstance(value, str) and len(value) > 0:
            self._category = value
        elif hasattr(self, '_category') and self._category is not None:
            pass
        else:
            raise AttributeError("Magazine category must be a non-empty string.")

    def articles(self):
        #get the list of articles in the magazine
        return self._articles_list

    def contributors(self):
        #get the list of contributers to the magazine
        return list(set([article.author for article in self._articles_list]))

    def article_titles(self):
        #get the tiles of all the articles in teh magazine
        return [article.title for article in self._articles_list] if self._articles_list else None

    def contributing_authors(self):
        #get the authors who have contributed more that teo articles to the magazine
        if self._articles_list:
            authors = [author for author in self.contributors() if len([article for article in self._articles_list if article.author == author]) > 2]
            return authors if authors else None
        else:
            return None

    @classmethod
    def top_publisher(cls):
        #get the magazine with the most articles
        if cls.all:
            return max(cls.all, key=lambda x: len(x.articles()))
        else:
            return None