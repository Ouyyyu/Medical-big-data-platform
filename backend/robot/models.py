from .question_classifier import *
from .question_parser import *
from .answer_search import *

'''问答类'''


class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是小妤智能助理，希望可以帮到您。'

        res_classify = self.classifier.classify(sent)  ##解析问题类型

        if not res_classify:
            return answer

        res_sql = self.parser.parser_main(res_classify)  ##返回sqls

        final_answers = self.searcher.search_main(res_sql)  ##根据sqls搜索答案
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)
