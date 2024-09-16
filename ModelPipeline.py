# due to the fitting problem cannot be skip, at here will create a custom pipeline by accessing 3 value as parameter 
class ModelPipeline:
    
    def __init__(self, encoder_path, scaler_path, model_path):
        # load the encoder, scaler and model by using joblib
        self.encoder = joblib.load(encoder_path)
        self.scaler = joblib.load(scaler_path)
        self.model = joblib.load(model_path)
    
    def predict(self, input_data):
        # due to input data is in dictionary type so need to do convert
        df = pd.DataFrame([input_data])
        
        # get the encode feature from encoder, to ensure consistency 
        categorical_columns = self.encoder.feature_names_in_

        # col that in int or float datatype
        continuous_columns = [col for col in df.columns if col not in categorical_columns]

        # encoder 
        df[categorical_columns] = self.encoder.transform(df[categorical_columns])

        # scaler
        x = df.values
        x_transform = self.scaler.transform(x)
        
        # model
        predictedY = self.model.predict(x_transform)
        
        return int(predictedY[0])