from . import CONN, CURSOR

class Highscore():

    # high_scores = high_scores_data['high_scores']


    def __init__(self, user, score, id:int=None):
        self.id = id
        self.user = user
        self.score = score


    def __repr__(self):
        return f"Highscore(user={self.user}, score={self.score})"

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS scores (
        id INTEGER PRIMARY KEY, 
        user_name TEXT, 
        score INTEGER
        )"""
    
        CURSOR.execute(sql)
        CONN.commit()
    
    def add_score(self):
        sql ="""INSERT INTO scores (user_name, score) VALUES(?,?)"""
        CURSOR.execute(sql, [self.user, self.score])
        CONN.commit()

        last_row_sql = """SELECT * FROM scores ORDER BY id DESC LIMIT 1"""
        self.id = CURSOR.execute(last_row_sql).fetchone()[0]


    @classmethod
    def get_high_scores(cls):
        sql = """SELECT user_name, score FROM scores ORDER BY score DESC LIMIT 5"""
        sql_return = CURSOR.execute(sql)
        top_5 = []
        for i in sql_return:
            top_5.append(i)
        return top_5
    
    
    ##For maintenance purposes
    @classmethod
    def clean_score_records(cls):
        sql = """DELETE FROM scores WHERE score NOT IN (SELECT score FROM scores ORDER BY score DESC LIMIT 5)"""
        CURSOR.execute(sql)
        CONN.commit()
    
    # ##For maintenance purposes
    # @classmethod
    # def destroy_score_records(cls):
    #     sql = """DELETE FROM scores"""
    #     CURSOR.execute(sql)
    #     CONN.commit()

    @classmethod
    def initialize_scores(cls, user, score):
        sql = """INSERT INTO scores (user_name, score) VALUES(?,?)"""
        CURSOR.execute(sql, [user, score])
        CONN.commit()


    


    ##Getter setter logic for class input validation
    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, value):
        if type(value) == str:
            self._user = value
        else:
            raise TypeError("user value needs to be a string")

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        if type(value) == int:
            self._score = value
        else:
            raise TypeError("score must be an integer")
    ##End of getter setter logic