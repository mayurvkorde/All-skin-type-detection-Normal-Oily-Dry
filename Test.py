import ktrain

predictor = ktrain.load_predictor(r'C:\Users\mayurk\Desktop\dark_circle')

skinType = predictor.predict_filename(r'C:\Users\mayurk\Desktop\qq.jpg')

detectSkinType = None
if skinType == ['C:\\Users\\mayurk\\Desktop\\Skin type images\\1']:
    detectSkinType = "Oily Skin"

elif skinType == ['C:\\Users\\mayurk\\Desktop\\Skin type images\\2']:
    detectSkinType = "Dry Skin"

else:
    detectSkinType = "Normal Skin"
