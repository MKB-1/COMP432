from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.neural_network import MLPRegressor


class RegressionTrainer:
    def __init__(self, common_args={}):
        # Intializing models
        self.lr = LogisticRegression(*common_args)
        self.sv = SVR(*common_args)
        self.dt = DecisionTreeRegressor(*common_args)
        self.rf = RandomForestRegressor(*common_args)
        self.knn = KNeighborsRegressor(*common_args)
        self.ab = AdaBoostRegressor(*common_args)
        self.g = GaussianProcessRegressor(*common_args)
        self.nn = MLPRegressor(*common_args)


rt = RegressionTrainer()
