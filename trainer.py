from custom.comparisons import MyBert
from chatterbot import languages, ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.response_selection import get_random_response
from custom.search import IndexedTextSearch

chatbot = ChatBot("chatbot",
                  read_only=True,
                  preprocessors=[
                      'chatterbot.preprocessors.clean_whitespace'
                  ],
                  logic_adapters=[
                      {
                          'import_path': 'chatterbot.logic.BestMatch',
                      }
                  ],
                  statement_comparison_function=MyBert,
                  response_selection_method=get_random_response,
                  search_algorithm_name=IndexedTextSearch.name,
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
                  tagger_language=languages.VIE,
                  database_uri='sqlite:///database.sqlite3'
                  )

if __name__ == "__main__":

    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train('./data/train_data.yml')
