from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def find_id(need_id, category_name):
        return [el for el in category_name if el.id == need_id][0]

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        if self.categories:
            find_category_id = self.find_id(category_id, self.categories)
            find_category_id.id = category_id
            find_category_id.family_name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        if self.topics:
            find_topic_id = self.find_id(topic_id, self.topics)
            find_topic_id.topic = new_topic
            find_topic_id.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        if self.documents:
            find_document_id = self.find_id(document_id, self.documents)
            find_document_id.file_name = new_file_name

    def delete_category(self, category_id):
        find_category_id = self.find_id(category_id, self.categories)
        self.categories.remove(find_category_id)

    def delete_topic(self, topic_id):
        find_topic_id = self.find_id(topic_id, self.topics)
        self.topics.remove(find_topic_id)

    def delete_document(self, document_id):

        find_document_id = self.find_id(document_id, self.documents)
        self.documents.remove(find_document_id)

    def get_document(self, document_id):
        find_get_document_id = self.find_id(document_id, self.documents)
        return find_get_document_id

    def __repr__(self):
        result = '\n'.join([repr(c) for c in self.categories])
        result += '\n'.join([repr(b) for b in self.topics])
        result = '\n'.join([repr(c) for c in self.documents])
        return result
