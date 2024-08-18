from model import model
import joblib



if __name__ == "__main__":
    nlpModel = model('data/rev.csv')

    joblib.dump(nlpModel, 'nlpModel')

