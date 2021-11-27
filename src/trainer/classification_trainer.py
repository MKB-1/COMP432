from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier


class ClassificationTrainer:
    def __init__(self, common_args={}):
        # Intializing models
        self.lr = LogisticRegression(*common_args)
        self.sv = SVC(*common_args)
        self.dt = DecisionTreeClassifier(*common_args)
        self.rf = RandomForestClassifier(*common_args)
        self.knn = KNeighborsClassifier(*common_args)
        self.ab = AdaBoostClassifier(*common_args)
        self.g = GaussianNB(*common_args)
        self.nn = MLPClassifier(*common_args)
